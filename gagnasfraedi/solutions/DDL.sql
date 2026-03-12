--  Sports database 
--  Copyright (C) 2016-2026, Björn Þór Jónsson

-- DQL (Creating database structure)

DROP TABLE IF EXISTS Results;
DROP TABLE IF EXISTS People;
DROP TABLE IF EXISTS Sports;
DROP TABLE IF EXISTS Competitions;

CREATE TABLE People (
       IDxa INT,
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