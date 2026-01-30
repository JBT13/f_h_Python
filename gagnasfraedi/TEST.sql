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

