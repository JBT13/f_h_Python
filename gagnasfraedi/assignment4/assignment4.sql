-- T-202-GAG1: Assignment 4
-- Student name(s): Jeremias Borjas

-- A
-- How many class types need more than 20 digital keyboards ?

SELECT COUNT(*)
FROM 

SELECT COUNT(*)
FROM Class C
JOIN Type T ON T.ID = C.TID
JOIN Needs N ON N.TID = T.ID
JOIN Equipment E ON E.ID = N.EID
WHERE E.name LIKE '%Digital Keyboard%' AND N.quantity > 20;
-- Explanation:



-- B
-- How many different class types have a higher attendance capacity
-- than the quantity needed of some equipment in the class type?

SELECT COUNT(DISTINCT T.ID)
FROM Type T
JOIN Needs N ON T.ID = N.TID
WHERE T.capacity > N.quantity;

-- Explanation:


-- C
-- Return the names of learners who have attended two classes in the
-- same day in different schools

SELECT DISTINCT L.name
FROM Learner L
JOIN Attends A1 ON L.ID = A1.LID -- First learner
JOIN Class C1 ON A1.CID = C1.ID 
JOIN Attends A2 ON L.ID = A2.LID -- Second learner
JOIN Class C2 ON A2.CID = C2.ID
WHERE C1.date = C2.date   -- Same day
  AND C1.SID <> C2.SID;   -- Different schools

-- Explanation:




-- D
-- How many learners have a tutoring instructor, but have never
-- attended a class that their instructor led?
-- Explanation:

SELECT COUNT(*)
FROM Learner L
JOIN Instructor I ON I.ID = L.IID 
JOIN Attends A ON A.LID = L.ID
WHERE A.CID <> I.ID 

-- E
-- For each class type, return its name and wheter the average rating of classes
-- of that type is higher or equal to 7, or lower than 7, in a column
-- named "Rating" with values "Good" or "Bad" respectively
-- Explanation:
SELECT T.name,
  CASE 
        WHEN AVG(A.rating) >= 7 THEN 'Good' 
        ELSE 'Bad' 
  END AS Rating
FROM Attends A
JOIN Class C ON C.ID = A.CID
JOIN Type T ON C.TID = T.ID
GROUP BY T.name


-- F
-- Return the ID of the instructors who have tutored most learners
-- Explanation:

SELECT IID, COUNT(*)
FROM Learner
--JOIN Learner L ON L.IID = I.ID
GROUP BY IID 
having count(*) = (
  select max(TotalPerInstructor)
  from (
    select count(*) as TotalPerInstructor
    from Learner
    where IID is not null
    group by IID
  ) as subtable
);



-- G
-- How many class types have at least one needed equipment item 
-- costing more than 100.000 and at least one other needed equipment item
-- costing less than 5000
-- Explanation:

SELECT count(*)
FROM Type T
WHERE EXISTS(
  SELECT 1
  FROM Needs N
  JOIN Equipment E ON N.EID = E.ID
  WHERE N.TID = T.ID AND E.price > 100000
)
AND EXISTS(
    SELECT 1
  FROM Needs N
  JOIN Equipment E ON N.EID = E.ID
  WHERE N.TID = T.ID AND E.price < 5000
)


-- H
-- How many instructors have led a class in all schools on the same day?
-- Explanation:
SELECT COUNT(DISTINCT IID)
FROM (
    SELECT IID, date
    FROM Class 
    GROUP BY IID, date
    HAVING COUNT(DISTINCT SID) = (SELECT COUNT(*) FROM School)
) AS InstructorsInAllSchools;


-- I
-- How many class types have a total equipment cost of less than
-- 1.000.000?
-- ○ Hint: You must take into account the equipment quantity as well
-- Explanation:

SELECT COUNT(*)
FROM (
  SELECT TID, SUM(E.price * N.quantity)
  FROM Type T
  JOIN Needs N ON N.TID = T.ID
  JOIN Equipment E ON E.ID = N.EID 
  GROUP BY TID
  HAVING SUM(E.price * N.quantity) < 1000000
)



-- J
-- Return the name of the class type with the highest equipment cost per
-- person, based on full capacity.
-- ○ Hint: You must take into account the equipment quantity as well

-- Explanation:




