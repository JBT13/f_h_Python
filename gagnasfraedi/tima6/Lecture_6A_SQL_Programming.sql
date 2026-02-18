

-- System functions?
select current_database();
select current_user;
select lastval();



-----------
-- VIEWS --
-----------


-- STANDARD VIEW
-- Example: Show stats for cities in countries

DROP VIEW IF EXISTS CountryCityStats;

CREATE VIEW CountryCityStats AS
SELECT
  C.Name,
  COUNT(CI.ID) AS city_count,
  COALESCE(SUM(CI.Population), 0) AS total_city_population,
  C.population as total_country_population
FROM Country C
LEFT JOIN City CI ON CI.CountryCode = C.code
GROUP BY C.code;

-- Use it like a table:
SELECT *
FROM CountryCityStats
ORDER BY total_city_population DESC;


-- CTE VIEW
-- Example: Show stats for cities in France

WITH CountryCityStats_ AS (
	SELECT
	C.Name,
	COUNT(CI.ID) AS city_count,
	COALESCE(SUM(CI.Population), 0) AS total_city_population,
	C.population as total_country_population
	FROM Country C
	LEFT JOIN City CI ON CI.CountryCode = C.code
	GROUP BY C.code
)
SELECT * 
FROM CountryCityStats_ CCS
WHERE CCS.name = 'France';


-- Cannot use it like a table:
SELECT *
FROM CountryCityStats_
ORDER BY total_city_population DESC;
-- ERROR: relation "countrycitystats_" does not exist



-- MATERIALIZED VIEW
-- Example: Show the population ratio between pairs of cities

DROP MATERIALIZED VIEW IF EXISTS PopulationRatio;

CREATE MATERIALIZED VIEW PopulationRatio
AS
SELECT CY1.countrycode, CY1.name AS id1, CY2.name AS id2, 1.0 * CY1.population / CY2.population AS ratio
FROM City CY1
JOIN City CY2 ON CY1.countrycode = CY2.countrycode;
	
-- Use it like a table
SELECT PR.id1, PR.id2, PR.ratio, PR.countrycode
FROM PopulationRatio PR
WHERE PR.ratio = (
	SELECT max(ratio) 
	FROM PopulationRatio
);
 
-- Inserting new data
INSERT INTO City VALUES (1234567,'Raufarhöfn','GBR','Wales', 25);

-- Not reflected in the materialized view!


-- Must refresh
REFRESH MATERIALIZED VIEW PopulationRatio;

-- Now reflected!




---------------
-- FUNCTIONS --
---------------

-- Example: Function to create a new city

CREATE OR REPLACE FUNCTION CreateCity(
  p_id integer,
  p_name varchar(35),
  p_country_code char(3),
  p_district varchar(20) DEFAULT '',
  p_population integer DEFAULT 0
)
RETURNS void AS 
$$
BEGIN

  INSERT INTO City(ID, Name, CountryCode, District, Population)
  VALUES (p_id, p_name, p_country_code, COALESCE(p_district, ''), p_population);
  
  EXCEPTION
  WHEN unique_violation THEN
    RAISE EXCEPTION 'City with ID=% already exists', p_id;

END
$$
LANGUAGE plpgsql;


-- Calling the function (Just like Python!)
 
-- Taken ID => User-friendly error message
SELECT CreateCity(1, 'Kókópöffs', 'ISL', '', 1);

-- Non-existing country => System error message
SELECT CreateCity(976543, 'Kókópöffs', 'XXX', '', 1);

-- Everything fixed
SELECT CreateCity(976543, 'Kókópöffs', 'ISL', '', 1);

-- Let's take a look:

select * 
from City


-- Example: What about when we are using generated IDs?

-- Let's create a temporary table
CREATE TABLE President (
	ID 		INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	Name 	VARCHAR NOT NULL
);

-- Insert some data

INSERT INTO President(Name) VALUES ('Emmanuel Macron');
INSERT INTO President(Name) VALUES ('Luiz Inácio Lula da Silva');
INSERT INTO President(Name) VALUES ('Cyril Ramaphosa');
INSERT INTO President(Name) VALUES ('Claudia Sheinbaum');
INSERT INTO President(Name) VALUES ('Lee Jae-myung');

SELECT * 
FROM President;

-- Function to create a new president
CREATE OR REPLACE FUNCTION CreatePresident(
	p_name varchar
)
RETURNS INT
AS $$
DECLARE
  v_id int;
BEGIN
  INSERT INTO President(Name)
  VALUES (p_name)
  RETURNING ID INTO v_id;

  RETURN v_id;
END
$$
LANGUAGE plpgsql;

-- Example call:
SELECT CreatePresident('Halla Tómasdóttir');  -- example name


-- Calling in a transaction

DO 
$$
BEGIN
	PERFORM CreatePresident('Halla Tómasdóttir');
END
$$;


--------------
-- TRIGGERS --
--------------


-- Example: Standardize cities (prevent negative population, turn fahrenheit into celcius)

DROP TRIGGER IF EXISTS StandardizeCity ON City; -- Must state table when dropping too
DROP FUNCTION IF EXISTS StandardizeCity();

CREATE FUNCTION StandardizeCity()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
  IF NEW.Population < 0 THEN
    RAISE EXCEPTION 'City population cannot be negative (ID=%)', NEW.ID;
  END IF;

  NEW.AvgTemp := (New.AvgTemp - 32) / (1.0 * 9/5); -- Fahrenheit to celsius formula
  RETURN NEW;
END;
$$;

CREATE TRIGGER StandardizeCity
BEFORE INSERT OR UPDATE ON City
FOR EACH ROW
EXECUTE FUNCTION StandardizeCity();

-- Testing

INSERT INTO City VALUES (674835, 'Fairview', 'USA', 'Connecticut', 500, 51.3);

SELECT *
FROM City 
WHERE name = 'Fairview'


-- Example: Ban language deletion

DROP TRIGGER IF EXISTS BanLanguageDelete ON Language;
DROP FUNCTION IF EXISTS BanLanguageDelete();

CREATE FUNCTION BanLanguageDelete()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
  RAISE EXCEPTION 'Deletion is not allowed for Language';
END;
$$;

CREATE TRIGGER BanLanguageDelete
BEFORE DELETE ON Language
FOR EACH ROW
EXECUTE FUNCTION BanLanguageDelete();

-- Testing

DELETE 
FROM Language 
WHERE Language = 'Danish';



-- Example: If a new/updated city is the most populous city in a country, make it the capital

DROP TRIGGER IF EXISTS CheckIfNewCapital ON City;
DROP FUNCTION IF EXISTS CheckIfNewCapital();

CREATE OR REPLACE FUNCTION CheckIfNewCapital()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
DECLARE
  v_current_max int;
BEGIN
  -- Find current maximum city population for that country (before inserting NEW row)
  SELECT MAX(Population)
  INTO v_current_max
  FROM City
  WHERE CountryCode = NEW.CountryCode;

  -- If no cities exist yet, MAX is NULL -> treat as 0
  IF v_current_max IS NULL THEN
    v_current_max := 0;
  END IF;

  -- If the new city is >= current max, make it the capital
  IF NEW.Population >= v_current_max THEN
    UPDATE Country
    SET Capital = NEW.ID
    WHERE Code = NEW.CountryCode;

  END IF;

  RETURN NEW;
END;
$$;

CREATE TRIGGER CheckIfNewCapital
BEFORE INSERT OR UPDATE ON City
FOR EACH ROW
EXECUTE FUNCTION CheckIfNewCapital();

-- Testing 
UPDATE City
SET population = '100000000'
WHERE name = 'Rouen'


SELECT *
FROM Country C
JOIN City CY on C.capital = CY.ID
WHERE C.name = 'France'


------------------
-- TRANSACTIONS --
------------------

-- Example: Want to test if my implementation of a query that fetches cities with pop. 
-- between 10 and 20 works, without affecting the data

BEGIN;

INSERT INTO City(ID, Name, CountryCode, District, Population)
VALUES (9999, 'TestCity', 'ISL', 'Test', 12);

-- Confirm it exists inside transaction
SELECT * 
FROM City 
WHERE population between 10 and 20;

ROLLBACK;

-- Gone after rollback
SELECT * FROM City WHERE ID = 9999;