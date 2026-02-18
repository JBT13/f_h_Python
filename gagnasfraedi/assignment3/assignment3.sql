-- T-202-GAG1: Assignment 3
-- Student name(s): Jeremias Borjas, Einar Berg Viðarson, Emil Berg

-- A
-- Least expensive piece of equipment cost only return the price


SELECT min(price)
FROM Equipment;
-- Explanation:


-- B
-- how many(count) Classes have been held on February 29th 
SELECT count(*)
FROM Class C
WHERE EXTRACT(Month FROM C.date) = 02 AND EXTRACT(Day FROM C.date) = 29;
-- Explanation:


-- C
-- how many(count) classes of types that has piano somewhere in their name(ILIKE)
-- case insensitive
-- Explanation:

SELECT COUNT(c.ID)
FROM Class c
JOIN Type t on c.TID = t.ID
WHERE t.name ILIKE '%piano%'; 
-- þetta er rett 


-- D
-- How many differents Instructors have led
-- one class attended by a learner that they personally tutor
-- Select instructors from X group by instructor 
-- Explanation:

SELECT COUNT(DISTINCT I.ID) 
FROM Instructor I
JOIN Class C ON I.ID = C.IID          
JOIN Attends A ON C.ID = A.CID     
JOIN Learner L ON A.LID = L.ID       
WHERE L.IID = I.ID; -- THE SAME INSTRUCTOR



-- E
-- Each class type name with the average rating of all classes of that type
-- the result should be rounded to the nearest integer and ordered from highest to lowest 

SELECT T.name, ROUND(AVG(A.rating)) AS "Average Rating"
FROM Type T
JOIN Class C ON C.TID = T.ID 
JOIN Attends A ON A.CID = C.ID
GROUP BY T.name 
ORDER BY "Average Rating" DESC;
-- Explanation:


-- F
-- How many learners have not attended any classes and are not being tutored
-- by an instructor

SELECT COUNT(*) 
FROM Learner 
WHERE IID IS NULL -- InstructorID = Null (no instructor)
AND 
ID NOT IN (SELECT LID FROM Attends); -- Have not attended any classes 

-- Explanation:




-- G
-- How many Instructors have led 10 or more classes

SELECT COUNT(*)
FROM (
    SELECT I.ID
    FROM Instructor I
    JOIN Class C ON C.IID = I.ID
    GROUP BY I.ID -- Set apart the instructors
    HAVING count(C.ID) >= 10 -- Where they have equal or more than 10 classes
) X;

-- Explanation:


-- H
-- Explanation:
SELECT COUNT(*) FROM Learner l1
WHERE l1.iid IS NOT NULL AND EXISTS (
SELECT 1 FROM Learner l2 WHERE l2.id <> l1.id
AND l2.iid = l1.iid AND split_part(l2.name, ' ', 1) = split_part(l1.name, ' ', 1));


-- I
-- How many classes were held at schools in reykjavik with capacitiy 
-- between 30 <= x <= 40 but were not full
SELECT COUNT(*)
FROM Class C
JOIN School S ON C.SID = S.ID
JOIN Type T ON C.TID = T.ID
WHERE S.address LIKE '%Reykjavik%' -- held in reykjavik
  AND T.capacity BETWEEN 30 AND 40 -- between 30 and 40
  AND (
    SELECT COUNT(*)  
    FROM Attends A  
    WHERE A.CID = C.ID -- Full class 
  ) < T.capacity;
 
-- Explanation:


-- J
-- Which instructor has/have led the most total class time(minutes)

SELECT I.ID, I.name, SUM(C.minutes) 
FROM Instructor I
JOIN Class C ON C.IID = I.ID
GROUP BY I.ID, I.name 
HAVING SUM(C.minutes) = (
    SELECT MAX(TotalSum) -- Max guy 
    FROM (
        SELECT SUM(minutes) AS TotalSum
        FROM Class
        GROUP BY IID
    )
);
-- Explanation:




