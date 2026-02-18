CREATE DATABASE "helloworld";


CREATE TABLE sponsee (
    id INT PRIMARY KEY,
    grant_amount DECIMAL(10, 2) NOT NULL
);


CREATE TABLE member (
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    username VARCHAR(100) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL

);


CREATE TABLE trainee (
    member_id INT PRIMARY KEY,
    last_login_date DATE NOT NULL,
    fitness_level INT NOT NULL,
    sponsee_id INT NULL,
    FOREIGN KEY (member_id) REFERENCES member (id) ON DELETE CASCADE,
    FOREIGN KEY (sponsee_id) REFERENCES sponsee(id)
);


CREATE TABLE coach (
    member_id INT PRIMARY KEY,
    avail_hours VARCHAR(100) NOT NULL,
    phone VARCHAR(30) UNIQUE NOT NULL,
    bank VARCHAR(100) NOT NULL,
    ledger VARCHAR(100) NOT NULL,
    account_number VARCHAR(100) NOT NULL,
    FOREIGN KEY (member_id) REFERENCES member (id) ON DELETE CASCADE
);


CREATE TABLE discipline (
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    rank INT NOT NULL,
    CONSTRAINT chk_rank CHECK (rank BETWEEN 1 AND 10)
);


CREATE TABLE program (
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    start_date DATE NOT NULL,
    level INT NOT NULL,
    discipline_id INT NOT NULL,
    coach_id INT NOT NULL,
    FOREIGN KEY (discipline_id) REFERENCES discipline (id),
    FOREIGN KEY (coach_id) REFERENCES coach (member_id)
);


CREATE TABLE component (
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    program_id INT NOT NULL,
    FOREIGN KEY (program_id) REFERENCES program (id) ON DELETE CASCADE
);


CREATE TABLE workout (
    component_id INT PRIMARY KEY,
    intensity_lvl INT NOT NULL,
    duration TIME NOT NULL,
    FOREIGN KEY (component_id) REFERENCES component (id) ON DELETE CASCADE
);


CREATE TABLE fittest (
    component_id INT PRIMARY KEY,
    test_date DATE NOT NULL,
    duration TIME NOT NULL,
    FOREIGN KEY (component_id) REFERENCES component (id) ON DELETE CASCADE
);


CREATE TABLE task (
    fittest_id INT,
    task_number INT,
    intensity_lvl INT NOT NULL,
    description VARCHAR(100) NOT NULL,
    PRIMARY KEY (fittest_id, task_number),
    FOREIGN KEY (fittest_id) REFERENCES fittest (component_id) ON DELETE CASCADE
);


CREATE TABLE crew (
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(100),
    discipline_id INT NULL,
    sponsee_id INT NULL,
    FOREIGN KEY (discipline_id) REFERENCES discipline (id) ON DELETE SET NULL,
    FOREIGN KEY (sponsee_id) REFERENCES sponsee(id)

);



-- Relations


CREATE TABLE nominates (
    coach_id INT,
    sponsee_id INT,
    year INT NOT NULL,
    PRIMARY KEY (coach_id, sponsee_id, year),
    FOREIGN KEY (coach_id) REFERENCES coach (member_id) ON DELETE CASCADE,
    FOREIGN KEY (sponsee_id) REFERENCES sponsee (id) ON DELETE CASCADE
);


CREATE TABLE follows (
    follower_id INT,
    follows_id INT,
    PRIMARY KEY (follower_id, follows_id),
    FOREIGN KEY (follower_id) REFERENCES trainee (member_id) ON DELETE CASCADE,
    FOREIGN KEY (follows_id) REFERENCES trainee (member_id) ON DELETE CASCADE
);


CREATE TABLE crew_members (
    crew_id INT,
    trainee_id INT,
    PRIMARY KEY (crew_id, trainee_id),
    FOREIGN KEY (crew_id) REFERENCES crew (id) ON DELETE CASCADE,
    FOREIGN KEY (trainee_id) REFERENCES trainee (member_id) ON DELETE CASCADE
);


CREATE TABLE reviews (
    review_id INT PRIMARY KEY,
    trainee_id INT NOT NULL,
    coach_id INT NOT NULL,
    stars INT NOT NULL,
    FOREIGN KEY (trainee_id) REFERENCES trainee (member_id) ON DELETE CASCADE,
    FOREIGN KEY (coach_id) REFERENCES coach (member_id) ON DELETE CASCADE,
    CONSTRAINT check_no_self_review CHECK (trainee_id <> coach_id)
);


CREATE TABLE enrolled_in (
    trainee_id INT,
    program_id INT,
    PRIMARY KEY (trainee_id, program_id),
    FOREIGN KEY (trainee_id) REFERENCES trainee (member_id) ON DELETE CASCADE,
    FOREIGN KEY (program_id) REFERENCES program (id) ON DELETE CASCADE
);


CREATE TABLE completes (
    trainee_id INT,
    component_id INT,
    program_id INT,
    avg_heart_rate INT NOT NULL,
    max_heart_rate INT NOT NULL,
    PRIMARY KEY (trainee_id, component_id, program_id),
    FOREIGN KEY (trainee_id) REFERENCES trainee (member_id) ON DELETE CASCADE,
    FOREIGN KEY (component_id) REFERENCES component (id) ON DELETE CASCADE,
    FOREIGN KEY (program_id) REFERENCES program (id) ON DELETE CASCADE
);
