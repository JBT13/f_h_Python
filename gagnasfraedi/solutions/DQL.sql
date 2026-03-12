-- Sample (generated/fictional) flowerbed database for a park
-- Copyright (C), Björn Þór Jónsson

drop table if exists PlantedIn; -- Use alias I
drop table if exists Beds;
drop table if exists Gardens;
drop table if exists Plants;
drop table if exists Families;
drop table if exists Types;
drop table if exists Staff;

-- Tables

create table Staff (
	ID int primary key,
	name varchar not null,
	position varchar not null
);

create table Types (
	ID int primary key,
	name varchar not null
);

create table Families (
	ID int primary key,
	typeID int not null references Types(ID),
	name varchar not null
);

create table Plants (
	ID int primary key,
	familyID int references Families(ID),
	name varchar not null
);

create table Gardens (
       ID int primary key,
       name varchar not null unique
);

create table Beds (
	ID int primary key,
	gardenID int not null references Gardens(ID),
	size float not null,
	description varchar not null
);

create table PlantedIn (
	bedID int not null references Beds(ID),
	plantID int not null references Plants(ID),
	percentage int not null,
	staffID int not null references Staff(ID),
	primary key (bedID, plantID)
);