--  Sports database 
--  Copyright (C) 2016-2026, Björn Þór Jónsson

-- DQL (Creating database structure)

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
--13
SELECT P.ID, P.name, count(*)
FROM People P
JOIN Results R ON R.peopleID = P.ID
JOIN Sports S ON S.ID = R.sportID
WHERE record = R.result
GROUP BY P.ID
HAVING COUNT(P.ID) > 2

--14
SELECT P.ID, P.name, P.height, R.result, S.name --Boolean yes or no
FROM People P
JOIN Results R ON R.peopleID = P.ID
JOIN Sports S ON S.ID = R.sportID
WHERE record = R.result 
GROUP BY P.ID,P.name, R.result, S.name
-- Vantar one line 

--15
SELECT P.ID, P.name
FROM People P
LEFT JOIN Results R ON R.peopleID = P.ID
WHERE R.peopleID IS NULL

--16
SELECT P.ID, P.name
FROM People P
JOIN Results R ON R.peopleID = P.ID
JOIN Sports S ON S.ID = R.sportID
WHERE record = R.result AND S.name = 'High Jump'
UNION 
SELECT P.ID, P.name
FROM People P
JOIN Results R ON R.peopleID = P.ID
JOIN Competitions C ON C.ID = R.competitionID
WHERE EXTRACT(Year FROM C.held) = 2002 AND EXTRACT(Month FROM C.held) = 6

--17
SELECT P.ID, P.name
FROM People P
JOIN Results R ON R.peopleID = P.ID
JOIN Sports S ON S.ID = R.sportID
WHERE record = R.result 
INTERSECT
SELECT P.ID, P.name
FROM People P
JOIN Results R ON R.peopleID = P.ID
JOIN Sports S ON S.ID = R.sportID
WHERE record = R.result 
GROUP BY P.ID
HAVING COUNT(P.ID) = 1 

--18
SELECT count(*)
FROM (
       SELECT peopleID
       FROM People P
       JOIN Results R ON R.peopleID = P.ID
       JOIN Competitions C on C.ID = R.competitionID
       GROUP BY R.peopleID
       HAVING count(DISTINCT place) >= 10
)

-- --19
-- SELECT *
-- from Results
-- SELECT s.ID, s.name, s.record,   
-- FROM (
--        SELECT .ID, s.name, s.record,
--        FROM Sports s, Results r

-- WHERE count()
-- GROUP BY s.ID this is not right 

