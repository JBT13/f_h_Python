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

SELECT name
FROM    

-- Explanation:




-- D
-- Explanation:




-- E
-- Explanation:




-- F
-- Explanation:




-- G
-- Explanation:




-- H
-- Explanation:




-- I
-- Explanation:




-- J
-- Explanation:




