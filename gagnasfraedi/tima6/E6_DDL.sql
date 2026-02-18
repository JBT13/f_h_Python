-- Sample bills database 
-- Copyright (C) 2016-2026, Bjorn Thor Jonsson


-- Clean database
CREATE DATABASE "E6";

DROP TABLE IF EXISTS Bills;
DROP TABLE IF EXISTS Records;
DROP TABLE IF EXISTS Accounts;
DROP TABLE IF EXISTS People;


CREATE TABLE People (
    PID INT GENERATED ALWAYS AS IDENTITY, 
    pName VARCHAR(50) NOT NULL,
    pGender CHAR(1) NOT NULL,
    pHeight FLOAT NOT NULL,
    PRIMARY KEY (PID)
);

CREATE TABLE Accounts (
    AID INT GENERATED ALWAYS AS IDENTITY, 
    PID INT NOT NULL,
    aDate DATE NOT NULL,
    aBalance INT NOT NULL,
    aOver INT NOT NULL,
    PRIMARY KEY (AID),
    FOREIGN KEY (PID) REFERENCES People(PID)
);

CREATE TABLE Records (
    RID INT GENERATED ALWAYS AS IDENTITY,
    AID INT NOT NULL,
    rDate DATE NOT NULL,
    rType CHAR(1) NOT NULL,
    rAmount INT NOT NULL,
    rBalance INT NOT NULL,
    PRIMARY KEY (RID),
    FOREIGN KEY (AID) REFERENCES Accounts(AID)
);

CREATE TABLE Bills (
    BID INT GENERATED ALWAYS AS IDENTITY,
    PID INT NOT NULL,
    bDueDate DATE NOT NULL,
    bAmount INT NOT NULL,
    bIsPaid BOOLEAN NOT NULL,
    PRIMARY KEY (BID),
    FOREIGN KEY (PID) REFERENCES People(PID)
);


--1
DROP VIEW IF EXISTS AllRecords;

CREATE VIEW AllRecords(
    PID,
    AID,
    aDate,
    aBalance,
    OVER,
    RID,
    RDATE,
    RTYPE,
    rAmount,
    RBALANCE
) AS
SELECT 
    A.PID,
    A.AID,
    A.aDate,
    A.aBalance,
    A.aOver,
    R.RID,
    R.rDate,
    R.rType,
    R.rAmount,
    R.rBalance
FROM Accounts A 
LEFT OUTER JOIN Records R ON R.AID = A.AID


--2
DROP TRIGGER IF EXISTS CheckBills ON Bills;
DROP FUNCTION IF EXISTS CheckBills1();

CREATE FUNCTION CheckBills1() 
RETURNS TRIGGER
AS $$ 
BEGIN 

    IF (TG_OP = 'DELETE') THEN
        RAISE EXCEPTION 'You cannot delete my brother';
    END IF;

    IF (NEW.bAmount < 0) THEN
        RAISE EXCEPTION 'Cannot be negative my brother (ID=%)', NEW.ID;
    END IF;

    IF (NEW.bDueDate <= CURRENT_DATE) THEN
        RAISE EXCEPTION 'You are in the past';
    END IF;



    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER CheckBills
BEFORE INSERT OR DELETE OR UPDATE OF BID, PID, bDueDate, bAmount ON Bills
FOR EACH ROW 
EXECUTE FUNCTION CheckBills1();


--3

CREATE FUNCTION Account_Withdrawn()
RETURNS TRIGGER
AS $$
DECLARE
    current_balance INT;
    withdrawn_limit INT;
    new_balance INT;
BEGIN 
    IF (TG_OP = 'DELETE') THEN
        RAISE EXCEPTION 'You cannot delete my brother';
    END IF;

    IF (TG_OP = 'UPDATE') THEN
        RAISE EXCEPTION 'You cannot update my brother';
    END IF;

    SELECT aBalance, aOver 
    INTO current_balance, withdrawn_limit
    FROM Accounts
    WHERE AID = NEW.AID
    FOR UPDATE;

    IF (current_balance + withdrawn_limit) < NEW.rAmount THEN
        RAISE EXCEPTION 'You dont got enough money gang';
    END IF;

    new_balance := current_balance - NEW.rAmount;

    UPDATE Accounts
    SET aBalance = new_balance
    WHERE AID = NEW.AID;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER Account_Withdrawn
BEFORE INSERT OR UPDATE OR DELETE ON Records
FOR EACH ROW 
EXECUTE FUNCTION Account_Withdrawn();
