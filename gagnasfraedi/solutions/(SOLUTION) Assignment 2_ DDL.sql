-- T-202-GAG1: Assignment 2
-- Student name(s): SOLUTION

DROP TABLE IF EXISTS Nominates;
DROP TABLE IF EXISTS PartOf;
DROP TABLE IF EXISTS Crew;
DROP TABLE IF EXISTS Follows;
DROP TABLE IF EXISTS Task;
DROP TABLE IF EXISTS FitTest;
DROP TABLE IF EXISTS Workout;
DROP TABLE IF EXISTS Completes;
DROP TABLE IF EXISTS Component;
DROP TABLE IF EXISTS Reviews;
DROP TABLE IF EXISTS EnrolledIn;
DROP TABLE IF EXISTS Program;
DROP TABLE IF EXISTS Coach;
DROP TABLE IF EXISTS Trainee;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Sponsee;
DROP TABLE IF EXISTS Discipline;


-- A
CREATE TABLE Discipline (
  ID                 INT PRIMARY KEY,
  name               VARCHAR NOT NULL,
  popularity_rank    INT NOT NULL,
  CHECK (popularity_rank BETWEEN 1 AND 10)
);


-- J
CREATE TABLE Sponsee (
  ID           INT PRIMARY KEY,
  grant_amount INT NOT NULL
);


-- C
CREATE TABLE Member (
  ID          INT PRIMARY KEY,
  name        VARCHAR NOT NULL,
  username    VARCHAR NOT NULL UNIQUE,
  email       VARCHAR NOT NULL UNIQUE
);

CREATE TABLE Trainee (
  ID                 INT PRIMARY KEY,
  last_login_date    DATE NOT NULL,
  fitness_level      VARCHAR NOT NULL,
  SponseeID          INT NULL,                    -- J (this is supposed to be this way, i.e. NOT NULL)
  FOREIGN KEY (ID) REFERENCES Member(ID),
  FOREIGN KEY (SponseeID) REFERENCES Sponsee(ID)  -- J
);

CREATE TABLE Coach (
  ID                 INT PRIMARY KEY,
  phone_number       VARCHAR NOT NULL UNIQUE, -- D
  availability_hours VARCHAR NOT NULL,        -- D
  bank               INT  NOT NULL,           -- D
  ledger_number      INT  NOT NULL,           -- D
  account_number     INT  NOT NULL,           -- D
  FOREIGN KEY (ID) REFERENCES Member(ID)
);


-- B
CREATE TABLE Program (
  ID                 INT PRIMARY KEY,
  name               VARCHAR(150) NOT NULL,
  start_date         DATE NOT NULL,
  difficulty_level   VARCHAR(30) NOT NULL,
  DID                INT NOT NULL,
  CID                INT NOT NULL,                -- D
  FOREIGN KEY (DID) REFERENCES Discipline(ID),
  FOREIGN KEY (CID) REFERENCES Coach(ID)          -- D
);


-- E
CREATE TABLE EnrolledIn (
  TID   INT,
  PID   INT,
  PRIMARY KEY (TID, PID),
  FOREIGN KEY (TID) REFERENCES Trainee(ID),
  FOREIGN KEY (PID) REFERENCES Program(ID)
);

CREATE TABLE Reviews (
  ID INT PRIMARY KEY,      -- Optional
  TID INT NOT NULL,
  CID INT NOT NULL,
  stars INT NOT NULL,
  CHECK ((TID <> CID)),
  CHECK (stars BETWEEN 1 AND 5),
  FOREIGN KEY (TID) REFERENCES Trainee(ID),
  FOREIGN KEY (CID) REFERENCES Coach(ID)
);


-- F
CREATE TABLE Component (
  ID      INT PRIMARY KEY,
  name    VARCHAR NOT NULL,
  PID     INT NOT NULL,
  FOREIGN KEY (PID) REFERENCES Program(ID)
);

CREATE TABLE Completes (
  CID INT,
  TID INT,
  PID INT,
  avg_heart_rate    INT NOT NULL,
  max_heart_rate    INT NOT NULL,
  PRIMARY KEY (CID, TID, PID),
  FOREIGN KEY (CID) REFERENCES Component(ID),
  FOREIGN KEY(TID, PID) REFERENCES EnrolledIn(TID, PID)
);


-- G
CREATE TABLE Workout (
  ID                INT PRIMARY KEY,
  intensity_level   INT NOT NULL,
  duration_minutes  INT NOT NULL,
  FOREIGN KEY (ID) REFERENCES Component(ID)
);

CREATE TABLE FitTest (
  ID                INT PRIMARY KEY,
  test_date         DATE NOT NULL,
  duration_minutes  INT NOT NULL,
  FOREIGN KEY (ID) REFERENCES Component(ID)
);


-- H
CREATE TABLE Task (
  FID               INT,
  number            INT,
  description       VARCHAR NOT NULL,
  intensity_level   INT NOT NULL,
  PRIMARY KEY (FID, number),
  FOREIGN KEY (FID) REFERENCES FitTest(ID)
);


-- I 
CREATE TABLE Follows (
  TID_follows     INT,
  TID_followed    INT,
  PRIMARY KEY (TID_follows, TID_followed),
  CHECK ((TID_follows <> TID_followed)),
  FOREIGN KEY (TID_follows) REFERENCES Trainee(ID),
  FOREIGN KEY (TID_followed) REFERENCES Trainee(ID)
);

CREATE TABLE Crew (
  ID        INT PRIMARY KEY,
  name      VARCHAR NOT NULL,
  address   VARCHAR NULL,                         -- (this is supposed to be this way, i.e. NOT NULL)
  DID       INT NULL,                             -- (this is supposed to be this way, i.e. NOT NULL)
  SponseeID INT NULL,                             -- J (this is supposed to be this way, i.e. NOT NULL)
  FOREIGN KEY (DID) REFERENCES Discipline(ID),
  FOREIGN KEY (SponseeID) REFERENCES Sponsee(ID)  -- J
);


CREATE TABLE PartOf (
  TID       INT,
  CID       INT,
  PRIMARY KEY (TID, CID),
  FOREIGN KEY (TID) REFERENCES Trainee(ID),
  FOREIGN KEY (CID) REFERENCES Crew(ID)
);


-- J
CREATE TABLE Nominates (
  CID INT,
  SID INT,
  year INT,
  PRIMARY KEY (CID, SID, year),
  FOREIGN KEY (CID) REFERENCES Coach(ID),
  FOREIGN KEY (SID) REFERENCES Sponsee(ID)
);


-- Unfulfilled constraints
-- C: "ALL members are coaches and/or trainees"
-- D: "A coach ALWAYS coaches one or more programs"
-- E: "Programs are cancelled if fewer than 5 trainees sign up"
-- F: "EACH program has at least one component"
-- G: "Components can be divided into EITHER Workouts OR FitTests"
-- I: "A crew is not a crew if it has no members"