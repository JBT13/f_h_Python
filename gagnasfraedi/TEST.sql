SELECT 'Hello world';

CREATE TABLE RankingList (
    ranking_id INTEGER PRIMARY KEY, -- 
    name VARCHAR(255) UNIQUE NOT NULL,    startyear INTEGER -- 
);

CREATE TABLE PlayerRanking (
    ranking_id INTEGER PRIMARY KEY REFERENCES RankingList(ranking_id),
    age_group VARCHAR(50) NOT NULL
);

CREATE TABLE ClubRanking (
    ranking_id INTEGER PRIMARY KEY REFERENCES RankingList(ranking_id)
);

CREATE TABLE GlobalRanking (
    ranking_id INTEGER PRIMARY KEY REFERENCES ClubRanking(ranking_id)
);

CREATE TABLE NationalRanking (
    ranking_id INTEGER PRIMARY KEY REFERENCES ClubRanking(ranking_id),
    nationality VARCHAR(100) NOT NULL
);





CREATE TABLE Game (
    game_id INTEGER PRIMARY KEY,
    tournament_id INTEGER NOT NULL,
    league_number INTEGER NOT NULL,
    date DATE,
    description TEXT,
    result VARCHAR(50),
    winner_club_id INTEGER REFERENCES Club(club_id),
    FOREIGN KEY (tournament_id, league_number) REFERENCES League(tournament_id, league_number)
);

CREATE TABLE Goal (
    game_id INTEGER REFERENCES Game(game_id),
    number INTEGER,
    player_id INTEGER NOT NULL REFERENCES Player(player_id), 
    speed NUMERIC(5, 2) NOT NULL,
    description TEXT,
    PRIMARY KEY (game_id, number)
);


CREATE TABLE SponsorSponsorsPlayer (
    sponsor_id INTEGER REFERENCES Sponsor(sponsor_id),
    player_id INTEGER REFERENCES Player(player_id),
    type VARCHAR(100) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE, --
    PRIMARY KEY (sponsor_id, player_id, type, start_date)
);

CREATE TABLE ClubParticipatesLeague (
    club_id INTEGER REFERENCES Club(club_id),
    tournament_id INTEGER NOT NULL,
    league_number INTEGER NOT NULL,
    rank INTEGER,
    PRIMARY KEY (club_id, tournament_id, league_number),
    FOREIGN KEY (tournament_id, league_number) REFERENCES League(tournament_id, league_number)
);

CREATE TABLE SponsorPaysForParticipation (
    sponsor_id INTEGER REFERENCES Sponsor(sponsor_id),
    club_id INTEGER NOT NULL,
    tournament_id INTEGER NOT NULL,
    league_number INTEGER NOT NULL,
    fee NUMERIC(15, 2),
    PRIMARY KEY (sponsor_id, club_id, tournament_id, league_number),
    FOREIGN KEY (club_id, tournament_id, league_number) REFERENCES ClubParticipatesLeague(club_id, tournament_id, league_number)
);

CREATE TABLE ClubPlaysGame (
    game_id INTEGER REFERENCES Game(game_id),
    club_id INTEGER NOT NULL,
    tournament_id INTEGER NOT NULL,
    league_number INTEGER NOT NULL,
    possession INTEGER CHECK (possession BETWEEN 0 AND 100),
    shirt_color VARCHAR(50),
    PRIMARY KEY (game_id, club_id),
    FOREIGN KEY (club_id, tournament_id, league_number) REFERENCES ClubParticipatesLeague(club_id, tournament_id, league_number)
);

CREATE TABLE GameRefereedBy (
    game_id INTEGER REFERENCES Game(game_id),
    employee_id INTEGER REFERENCES Employee(employee_id),
    PRIMARY KEY (game_id, employee_id)
);

CREATE TABLE PlayerRankedIn (
    player_id INTEGER REFERENCES Player(player_id),
    ranking_id INTEGER REFERENCES PlayerRanking(ranking_id),
    rank INTEGER,
    PRIMARY KEY (player_id, ranking_id)
);

CREATE TABLE ClubRankedInGlobal (
    club_id INTEGER REFERENCES Club(club_id),
    ranking_id INTEGER REFERENCES GlobalRanking(ranking_id),
    rank INTEGER,    PRIMARY KEY (club_id, ranking_id)
);

CREATE TABLE ClubRankedInNational (
    club_id INTEGER REFERENCES Club(club_id),
    ranking_id INTEGER REFERENCES NationalRanking(ranking_id),
    rank INTEGER,
    PRIMARY KEY (club_id, ranking_id)
);



SELECT -- My goat column1, column2
FROM -- Table_name
WHERE -- Condition

SELECT * -- Helps for debugs
FROM -- Aliases might be helpful
WHERE -- filter

SELECT * 
FROM Country; -- Everything of country

SELECT name,population
FROM Country
WHERE region = "Southearn Europer" -- Every name and pop where region = "blabla"

SELECT population
FROM Country
WHERE name = "Denmark" -- Easy

SELECT code, name, region -- Where country is not independece
FROM Country
WHERE indepyear IS NULL

-- OPerators + - * / 

SELECT code, name, population + 10000, -- each population + 10000
FROM Country

SELECT code ||"-"|| name as CountryLabel -- Column would be "Countrylabel" 
FROM country

-- DONT USE LIMIT MY GANG PLEASEEEEEEEEEEEEE
SELECT name, population
FROM Country
ORDER BY population DESC

-- Distinct dictries in USA IT COST MONEY SO USE IT WHEN NEEDED
SELECT Distinct dictries
FROM City 
WHERE CountryCode = "USA"

-- how many cities are in the databse
SELECT count(*)
FROM City

SELECT count(distinct name)
FROM City

SELECT sum(population)
FROM country

SELECT avg(life_expent)
FROM country

SELECT min(population)
FROM Country

SELECT max(population)
FROM Country

-- JOIN MY GOAAATTTT

-- What cities are in denmark??  W connection between tables 
SELECT CY.name
FROM City CY
JOIN Country CT ON CT.Code = CY.CountryCode
WHERE CT.name = "Denmark"

SELECT disctinct CT.name
FROM Country CT
JOIN City CY ON CT.code = CY.CountryCode
WHERE CY.population > 100000

-- AND Operator 
SELECT disctinct CT.name
FROM Country CT
JOIN City CY ON CT.code = CY.CountryCode
JOIN IsIN I ON I.CountryCode = CT.code
WHERE CY.population > 100000
AND I.contitent = "Oceania"

SELECT code as "Landakodi", name as "landanafn"
FROM Country

SELECT code, language
FROM language
WHERE isOficial IS TRUE

SELECT name
FROM City
WHERE name LIKE "San%" -- "San___" = Santos
-- "%ang%" somewhere in the middle of the word

SELECT name 
FROM City
WHERE Population BETWEEN 5000 AND 2000

SELECT name
FROM country
ORDER BY population DESC
-- Default is ASCENDING

-- GROUP BY cost a lot, so we put them in group and kópavogur knows how many kopavogur there are HAHAHHA 
-- HAVING er lwk like where

SELECT Code, count(*)
FROM City
GROUP BY Code 

SELECT name, count(*)
FROM City
GROUP BY name 
HAVING count(*) > 1 

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