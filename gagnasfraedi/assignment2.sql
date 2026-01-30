CREATE DATABASE "assignement2Database";

CREATE TABLE Discipline (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    popularity INTEGER NOT NULL,
    CONSTRAINT discipline_pop CHECK (popularity IN (1,2,3,4,5,6,7,8,9,10))
);

CREATE TABLE Coach(
    id INTEGER PRIMARY KEY,
    phone VARCHAR(100) UNIQUE,
    availabity_hour VARCHAR(100),
    bank VARCHAR(100),
    ledger VARCHAR(100),
    account_number VARCHAR(100)
);

CREATE TABLE Program(
    id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    start_date DATE NOT NULL,
    level INTEGER,
    Dis_id INTEGER,
    Coh_id INTEGER,
    FOREIGN KEY (Dis_id) REFERENCES Discipline(id),
    FOREIGN KEY (Coh_id) REFERENCES Coach(id)
);

CREATE TABLE Component(
    id INTEGER PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE PRM_HAS_CMP(
    Prm_id INTEGER,
    Cmp_id INTEGER,
    PRIMARY KEY (Prm_id, Cmp_id),
    FOREIGN KEY (Prm_id) REFERENCES Program(id),
    FOREIGN KEY (Cmp_id) REFERENCES Component(id)
);

CREATE TABLE Member(
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    username VARCHAR(100) UNIQUE,
    email VARCHAR(100) UNIQUE
);

CREATE TABLE Sponsee(
    id INT PRIMARY KEY,
    grant_ammount INTEGER
);

CREATE TABLE Trainee(
    id INTEGER PRIMARY KEY,
    last_login DATE,
    level INTEGER,
    Spo_id INT NULL,
    FOREIGN KEY (Spo_id) REFERENCES Sponsee(id)
);

CREATE TABLE Workout(
    id INTEGER PRIMARY KEY,
    intensity_lvl VARCHAR(100),
    duration TIME,
    FOREIGN KEY (id) REFERENCES Component(id)
);

CREATE TABLE FitTest(
    id INTEGER PRIMARY KEY,
    "date" DATE,
    duration TIME,
    FOREIGN KEY (id) REFERENCES Component(id)
);

CREATE TABLE Task(
    number INTEGER,
    intensity_lvl VARCHAR(100),
    duration TIME,
    fit_test_id INTEGER NOT NULL,
    PRIMARY KEY(number, fit_test_id),

    FOREIGN KEY (fit_test_id) REFERENCES FitTest(id)
        ON DELETE CASCADE
);

CREATE TABLE Crew(
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    address VARCHAR(100),
    Dis_id INT NOT NULL,
    Spo_id INT NULL,
    FOREIGN KEY (Dis_id) REFERENCES Discipline(id),
    FOREIGN KEY (Spo_id) REFERENCES Sponsee(id)
);

CREATE TABLE Reviews(
    Coh_id INTEGER,
    Tra_id INTEGER,
    stars INTEGER,
    PRIMARY KEY(Coh_id, Tra_id),
    FOREIGN KEY (Coh_id) REFERENCES Coach(id),
    FOREIGN KEY (Tra_id) REFERENCES Trainee(id),
    CONSTRAINT stars_selec CHECK (stars IN (1,2,3,4,5))
);

CREATE TABLE Follows(
    flw_id INTEGER,
    flwer_id INTEGER,
    PRIMARY KEY (flw_id, flwer_id),
    FOREIGN KEY (flw_id) REFERENCES Trainee(id),
    FOREIGN KEY (flwer_id) REFERENCES Trainee(id)
);

CREATE TABLE Enrolled_in(
    Tra_id INTEGER,
    Prm_id INTEGER,
    PRIMARY KEY (Tra_id, Prm_id),
    FOREIGN KEY (Tra_id) REFERENCES Trainee(id),
    FOREIGN KEY (Prm_id) REFERENCES Program(id)
);

CREATE TABLE Completes(
    Tra_id INTEGER,
    Prm_id INTEGER,
    Cmp_id INTEGER,
    avg_HR INTEGER,
    max_HR INTEGER,
    PRIMARY KEY (Tra_id, Prm_id, Cmp_id),
    FOREIGN KEY (Tra_id, Prm_id) REFERENCES Enrolled_in(Tra_id, Prm_id),
    FOREIGN KEY (Cmp_id) REFERENCES Component(id)
);

CREATE TABLE IsPartOf(
    Tra_id INTEGER,
    Crew_id INTEGER,
    PRIMARY KEY (Tra_id, Crew_id),
    FOREIGN KEY (Tra_id) REFERENCES Trainee(id),
    FOREIGN KEY (Crew_id) REFERENCES Crew(id)
);

CREATE TABLE Nominates(
    year INT NOT NULL,
    Spo_id INT,
    Coh_id INT,
    PRIMARY KEY (year,Spo_id,Coh_id),
    FOREIGN KEY (Spo_id) REFERENCES Sponsee(id),
    FOREIGN KEY (Coh_id) REFERENCES Coach(id)
);



