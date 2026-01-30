CREATE DATABASE "MyDatabase";

CREATE TABLE Player (
    player_id INTEGER PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    nationality VARCHAR(100),
    no_goals INTEGER DEFAULT 0  
);

CREATE TABLE Award (
    year INTEGER PRIMARY KEY,
    player_id INTEGER NOT NULL,
    prize NUMERIC(15, 2),
    inst VARCHAR(255),
    FOREIGN KEY (player_id) REFERENCES Player(player_id)
);

CREATE TABLE Club (
    club_id INTEGER PRIMARY KEY,
    name VARCHAR(255),
    nationality VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE PlayerMemberOfClub (
    player_id INTEGER,
    club_id INTEGER,
    start_date DATE,
    end_date DATE,
    PRIMARY KEY (player_id, club_id, start_date),
    FOREIGN KEY (player_id)  REFERENCES Player(player_id),
    FOREIGN KEY (player_id)  REFERENCES Club(club_id),
);

CREATE TABLE Tournament (
    tournament_id INTEGER PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    venue VARCHAR(255), 
    date DATE,
    hosted_by_club_id INTEGER NOT NULL,
    monitored_by_employee_id INTEGER NOT NULL, 
    FOREIGN KEY (hosted_by_club_id) REFERENCES Club(club_id), 
    FOREIGN KEY (monitored_by_employee_id) REFERENCES Employee(employee_id) 
);

CREATE TABLE Employee (
    employee_id INTEGER PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE League (
    tournament_id INTEGER
    number INTEGER,
    name VARCHAR(255) NOT NULL,
    duration VARCHAR(100),
    PRIMARY KEY (tournament_id, number),
    UNIQUE (tournament_id, name)
);

CREATE TABLE Sponsor (
    sponsor_id INTEGER PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    nationality VARCHAR(100)
);




