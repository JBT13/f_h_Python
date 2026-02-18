--  Sports database 
--  Copyright (C) 2016-2026, Björn Þór Jónsson

-- DQL (Creating database structure)

CREATE DATABASE "exercise4";

DROP TABLE IF EXISTS Results;
DROP TABLE IF EXISTS People;
DROP TABLE IF EXISTS Sports;
DROP TABLE IF EXISTS Competitions;

CREATE TABLE People (
       ID INT,
       name VARCHAR(50),
       height FLOAT,
       PRIMARY KEY (ID)
);

CREATE TABLE Sports (
       ID INT,
       name VARCHAR(50),
       record FLOAT,
       PRIMARY KEY (ID),
       UNIQUE (name)
);

CREATE TABLE Competitions (
       ID INT,
       place VARCHAR(50),
       held DATE,
       PRIMARY KEY (ID)
);

CREATE TABLE Results (
       peopleID INT,
       competitionID INT,
       sportID INT,
       result FLOAT,
       PRIMARY KEY (peopleID, competitionID, sportID),
       FOREIGN KEY (peopleID) REFERENCES People (ID),
       FOREIGN KEY (competitionID) REFERENCES Competitions (ID),
       FOREIGN KEY (sportID) REFERENCES Sports (ID)
);

-- 1.
SELECT name, record
FROM Sports
ORDER BY name

-- 2.
SELECT Distinct name
FROM Sports ST
JOIN Results RS ON RS.sportID = ST.ID

-- 3. THEY DONT GOT results
SELECT count(Distinct peopleID)
FROM Results

-- 4.
SELECT Distinct PP.ID,  PP.name
FROM People PP
JOIN Results RS ON PP.ID = RS.peopleID 
JOIN Sports ON Sports.ID = RS.sportID
WHERE result = record 

-- 5.
SELECT Distinct PP.ID, PP.name
FROM People PP
JOIN Results RS ON PP.ID = RS.peopleID 
JOIN Competitions CP ON CP.ID = RS.competitionID
WHERE CP.place = 'Hvide Sande' AND extract(year FROM CP.held) = 2009

-- 6.
SELECT name
FROM People
WHERE name LIKE '% J%sen' 

-- 7. Highkey þurfti að googlea
SELECT PP.name, SP.name, CAST(ROUND((RS.result * 100.0) / SP.record) AS TEXT) || '%' AS percentage
FROM PEOPLE PP
JOIN Results RS ON PP.ID = RS.peopleID 
JOIN Sports SP ON SP.ID = RS.sportID
WHERE RS.result is NOT NULL


SELECT P.name AS Athlete, S.name AS Sport, CAST(ROUND((RE.result * 100.0) / S.record) AS TEXT) || '%' AS percentage
FROM Results AS RE 
JOIN People AS P ON P.ID = RE.peopleID
JOIN Sports AS S ON S.ID = RE.sportID

SELECT count(*) -- to check the amount of rows, if they match
FROM Results

-- 8.
SELECT count(Distinct peopleID)
FROM Results 
WHERE result IS NULL

-- 9.
SELECT PP.ID, PP.name
FROM PEOPLE PP
JOIN Results RS ON PP.ID = RS.peopleID
GROUP BY PP.ID 
HAVING count(result) >= 20

-- 10.
SELECT SP.ID, SP.name, max(result) as maxres
FROM Sports SP
JOIN Results RS ON SP.ID = RS.sportID
GROUP BY SP.ID,SP.name
ORDER BY SP.ID     

-- 11.
SELECT SP.name, count(Distinct peopleID) as numatheltes
FROM Sports SP
JOIN Results RS ON SP.ID = RS.sportID
WHERE SP.record = result
GROUP BY SP.ID

-- 12 man no chance hahahahah
SELECT PP.ID, PP.name
