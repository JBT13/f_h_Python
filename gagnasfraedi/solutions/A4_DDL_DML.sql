-- Fictional Music Academy Management Database 
-- Copyright (C), Hildur Davíðsdóttir

-- Disclaimer:
-- Data is artificially and randomly generated, and may or may not represent reality.
-- The database and its contents may also intentionally be poorly designed, incomplete and missing.
-- The contents of this database are only intended for educational purposes in the field of database retrieval.

-- DDL

-- Cleanup

DROP TABLE IF EXISTS Needs;
DROP TABLE IF EXISTS Attends;
DROP TABLE IF EXISTS Class;
DROP TABLE IF EXISTS Equipment;
DROP TABLE IF EXISTS Type;
DROP TABLE IF EXISTS School;
DROP TABLE IF EXISTS Learner;
DROP TABLE IF EXISTS Instructor;


-- Creating tables
CREATE TABLE Instructor (
    ID INT,
    name VARCHAR(200) NOT NULL,
    phone INT NOT NULL UNIQUE,
    PRIMARY KEY(ID)
);

CREATE TABLE Learner (
    ID INT,
    name VARCHAR(200) NOT NULL,
    phone INT NOT NULL UNIQUE,
    IID INT NULL REFERENCES Instructor(ID),      -- Tutors relation
    PRIMARY KEY(ID)
);

CREATE TABLE School (
    ID INT,
    address VARCHAR(200) NOT NULL,
    email VARCHAR(200) NOT NULL,
    PRIMARY KEY(ID)
);

CREATE TABLE Type (
    ID INT,
    name VARCHAR(200) NOT NULL,
    capacity INT NOT NULL,
    PRIMARY KEY(ID)
);

CREATE TABLE Equipment (
    ID INT,
    name VARCHAR(200) NOT NULL,
    price INT NOT NULL,
    PRIMARY KEY(ID)
);

CREATE TABLE Class (
    ID INT,
    IID INT NOT NULL REFERENCES Instructor(ID),      -- Leads relation
    TID INT NOT NULL REFERENCES Type(ID),            -- Is of relation
    SID INT NOT NULL REFERENCES School(ID),          -- Is at relation
    date DATE NOT NULL,
    minutes INT NOT NULL,
	PRIMARY KEY(ID)
);

CREATE TABLE Attends (
    LID INT REFERENCES Learner(ID),
    CID INT REFERENCES Class(ID),
    rating INT NOT NULL,
    PRIMARY KEY(LID, CID)
);

CREATE TABLE Needs (
    TID INT REFERENCES Type(ID),
    EID INT REFERENCES Equipment(ID),
    quantity INT NOT NULL,
    PRIMARY KEY(TID, EID)
);

