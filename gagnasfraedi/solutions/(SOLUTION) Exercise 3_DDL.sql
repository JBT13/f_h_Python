-- Exercise 3 (Solution by Hildur Davíðsdóttir)
--create database "Exercise3";

drop table if exists sponsors cascade;
drop table if exists ranked_in_national cascade;
drop table if exists ranked_in_global cascade;
drop table if exists ranked_in cascade;
drop table if exists national_ranking cascade;
drop table if exists global_ranking cascade;
drop table if exists club_ranking cascade;
drop table if exists player_ranking cascade;
drop table if exists ranking_list cascade;
drop table if exists plays cascade;
drop table if exists goal cascade;
drop table if exists referees cascade;
drop table if exists pays_for;
drop table if exists participates_in cascade;
drop table if exists sponsor cascade;
drop table if exists game cascade;
drop table if exists league cascade;
drop table if exists tournament cascade;
drop table if exists is_member_of cascade;
drop table if exists award cascade;
drop table if exists employee cascade;
drop table if exists club cascade;
drop table if exists player cascade;


-- 1
create table player (
  ID integer primary key,
  name varchar not null,
  nationality varchar not null,
  no_goals integer not null
);

-- 2
create table award (
  playerID integer,
  year integer not null,
  institution varchar not null,
  prize integer null,
  primary key (playerID, year),
  foreign key (playerID) references player(ID)
    on delete cascade
);

--3
create table club (
  ID integer primary key,
  name varchar not null,
  nationality varchar not null,
  unique (name, nationality)
);

--4
create table is_member_of (
  playerID integer,
  clubID integer,
  startdate date,
  enddate date null,
  primary key (playerID, clubID, startdate),
  foreign key (playerID) references player(ID),
  foreign key (clubID) references club(ID),
  check (enddate is null or enddate >= startdate) -- (not required check from the speicifcation, but wise!)
  -- Unfulfilled constraint: prevent overlapping membership intervals for the same (player, club)
);

--7
create table employee (
  ID integer primary key,
  name varchar not null
);

-- 5
create table tournament (
  ID integer primary key,
  name varchar not null,
  venue varchar not null,
  date date not null,
  hostClubID integer not null, --6
  monitorEmployeeID integer not null, --7
  foreign key (hostClubID) references club(ID),
  foreign key (monitorEmployeeID) references employee(ID)
);

-- 8
create table league (
  tournamentID integer,
  number integer not null,
  name varchar not null,
  duration integer not null, -- could also be varchar
  primary key (tournamentID, number),
  foreign key (tournamentID) references tournament(ID)
    on delete cascade,
  unique (tournamentID, name)
);

-- 9
create table game (
  ID integer primary key,
  tournamentID integer not null,
  leagueNumber integer not null,
  date date not null,
  result varchar not null,
  description varchar not null, --13
  foreign key (tournamentID, leagueNumber) references league(tournamentID, number),
  unique (ID, tournamentID, leagueNumber) --15
);


--11
create table participates_in (
  tournamentID integer not null,
  leagueNumber integer not null,
  clubID integer not null,
  final_rank integer not null,
  primary key (tournamentID, leagueNumber, clubID),
  foreign key (tournamentID, leagueNumber) references league(tournamentID, number),
  foreign key (clubID) references club(ID)
);

--12
create table sponsor (
  ID integer primary key,
  name varchar not null,
  nationality varchar not null
);

create table pays_for (
  tournamentID integer,
  leagueNumber integer,
  clubID integer,
  sponsorID integer not null,
  fee_amount integer not null,
  primary key (tournamentID, leagueNumber, clubID),
  foreign key (tournamentID, leagueNumber, clubID) references participates_in(tournamentID, leagueNumber, clubID),
  foreign key (sponsorID) references sponsor(ID)
);

--13
create table referees (
  gameID integer,
  employeeID integer,
  primary key (gameID, employeeID),
  foreign key (gameID) references game(ID),
  foreign key (employeeID) references employee(ID)
  -- Unfulfilled 1..* constraint: each game must have at least one referee
);

--14
create table goal (
  gameID integer,
  number integer not null,
  description varchar null,
  ball_speed integer not null,
  scorerPlayerID integer not null,
  primary key (gameID, number),
  foreign key (gameID) references game(ID)
    on delete cascade,
  foreign key (scorerPlayerID) references player(ID)
);

--15
create table plays (
  gameID integer not null,
  tournamentID integer not null,
  leagueNumber integer not null,
  clubID integer not null references club(ID),
  ball_possession integer not null,
  shirt_color varchar not null,
  primary key (gameID, clubID),
  foreign key (gameID, tournamentID, leagueNumber) references game(ID, tournamentID, leagueNumber),
  foreign key (tournamentID, leagueNumber, clubID) references participates_in(tournamentID, leagueNumber, clubID)
);

--16
create table ranking_list (
  ID integer primary key,
  name varchar not null unique,
  startyear integer not null
);

--17
create table player_ranking (
  rankingID integer primary key,
  age_group varchar not null,
  foreign key (rankingID) references ranking_list(ID)
);

create table club_ranking (
  rankingID integer primary key,
  --is_global boolean not null,
  --nationality varchar null,
  foreign key (rankingID) references ranking_list(ID)
--   (this can be solved this way but it is better to create separate tables for global and national)
--   check ( 
--     (is_global = true  and nationality is null) or
--     (is_global = false and nationality is not null)
--   )
);

create table global_ranking (
  rankingID integer primary key,
  foreign key (rankingID) references club_ranking(rankingID)
);

create table national_ranking (
  rankingID integer primary key,
  nationality varchar null,
  foreign key (rankingID) references club_ranking(rankingID)
);

--18
create table ranked_in (
  playerID integer primary key,
  rankingID integer not null,
  current_rank integer not null,
  foreign key (rankingID)references player_ranking(rankingID),
  foreign key (playerID) references player(ID)
);

--19
create table ranked_in_global (
  clubID integer primary key,
  rankingID integer not null,
  current_rank integer not null,
  foreign key (rankingID) references global_ranking(rankingID),
  foreign key (clubID) references club(ID)
);

create table ranked_in_national (
  clubID integer primary key,
  rankingID integer not null,
  current_rank integer not null,
  foreign key (rankingID) references national_ranking(rankingID),
  foreign key (clubID) references club(ID)
);

--20
create table sponsors (
  sponsorID integer,
  playerID integer,
  type varchar not null, 
  startdate date not null,
  enddate date null,
  primary key (playerID, sponsorID),
  foreign key (sponsorID) references sponsor(ID),
  foreign key (playerID) references player(ID),
  --Unfulfilled constraint: Players can only have one sponsor of each type at a time.
);
