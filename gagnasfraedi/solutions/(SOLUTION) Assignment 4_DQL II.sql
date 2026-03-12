-- T-202-GAG1: Assignment 4
-- Student names: SOLUTION

-- A. How many class types require more than 20 Digital Keyboards ?

SELECT count(N.TID)
FROM Needs N
JOIN Equipment E ON N.EID = E.ID
WHERE E.name = 'Digital Keyboard' and N.quantity > 20;


-- B. How many different class types have a higher attendance capacity 
-- than the quantity needed of some equipment in the class type?

SELECT count(DISTINCT T.ID)
FROM Type T
JOIN Needs N on N.TID = T.ID
WHERE T.capacity > N.quantity;


-- C. Return the names of learners who have attended two classes in the same day in different schools.

SELECT L.name
FROM Learner L
JOIN Attends A ON A.LID = L.ID
JOIN Class C ON C.ID = A.CID
GROUP BY L.ID, C.date
HAVING count(DISTINCT C.SID) > 1; -- Doing = 2 would also have been correct


-- D. How many learners have a tutoring instructor, but have never attended a class that their instructor led?

SELECT count(*)
FROM Learner L
WHERE L.IID IS NOT NULL
AND L.ID NOT IN (
    SELECT A.LID
    FROM Attends A
    JOIN Class C ON C.ID = A.CID
    WHERE C.IID = L.IID
);


-- E. For each class type, return its name and whether the average rating of classes 
-- of that type is >= 7 ("Good") or < 7 ("Bad"), in a column named "Rating".

SELECT T.name,
    CASE
        WHEN AVG(A.rating) >= 7 THEN 'Good'
        ELSE 'Bad'
    END AS "Rating"
FROM Attends A
JOIN Class C ON C.ID = A.CID
JOIN Type T ON T.ID = C.TID
GROUP BY T.ID;



-- F. Return the ID(s) of the instructor(s) who have tutored most learners

SELECT L.IID
FROM Learner L 
GROUP BY L.IID 
HAVING count(*) = (
    SELECT max(tutoring_count)
    FROM (
        SELECT L.IID, count(*) as tutoring_count
        FROM Learner L 
        WHERE L.IID IS NOT NULL --ok hérna að hafa Instructor töfluna með
        GROUP BY L.IID 
    )x
);


-- G. How many class types have at least one needed equipment item costing > 100000
-- and at least one other needed equipment item costing < 5000?

SELECT count(DISTINCT T.ID)
FROM Type T
JOIN Needs N  ON T.ID = N.TID
JOIN Needs N1 ON T.ID = N1.TID
JOIN Equipment E  ON E.ID = N.EID
JOIN Equipment E1 ON E1.ID = N1.EID
WHERE E.price > 100000 AND E1.price < 5000;


-- H. How many instructors have led a class in all schools on the same day?

SELECT count(*)
FROM (
    SELECT C.IID, C.date
    FROM Class C
    GROUP BY C.IID, C.date
    HAVING count(DISTINCT C.SID) = (
        SELECT count(*)
        FROM School S
    )
) X;


-- I. How many class types have a total equipment cost of < 1000000

SELECT count(*)
FROM Type T
WHERE T.ID NOT IN (
    SELECT N.TID
    FROM Needs N
    JOIN Equipment e ON e.ID = n.EID
    GROUP BY N.TID
    HAVING SUM(n.quantity * e.price) > 1000000
);


-- J. Return the name of the class type with the highest equipment cost per person (based on full capacity).

DROP VIEW IF EXISTS CostPerStudent;

CREATE VIEW CostPerStudent AS
SELECT T.ID, T.name, SUM(1.0 * N.quantity * E.price / T.capacity) AS avgcost
FROM Type T
JOIN Needs N ON T.ID = N.TID
JOIN Equipment E ON E.ID = N.EID
GROUP BY T.ID, T.name;

SELECT CPS.name, CPS.avgcost
FROM CostPerStudent CPS
WHERE CPS.avgcost = (
    SELECT MAX(avgcost)
    FROM CostPerStudent
);

DROP VIEW IF EXISTS CostPerStudent;