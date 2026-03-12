-- T-202-GAG1: Assignment 3
-- Student name(s): Einar Berg Viðarsson

-- A
-- What does the least expensive piece of equipment cost? Return only the price.
-- Explanation: 
SELECT MIN(price) FROM Equipment -- The lowest price

-- SELECT price FROM Equipment ODRER BY price -- All the prices


-- B
-- How many classes have been held on February 29th (of any year)?
-- Explanation:
SELECT COUNT(date) AS classes_on_february_29
FROM Class 
WHERE TO_CHAR(date, 'MM-DD') = '02-29';



-- C
-- How many classes of types that have 'piano' somewhere in their name
-- have been held? (Note that your query should be case-insensitive, i.e. classes
-- with ‘piAnO’ and ‘Piano’ in their type name should also be counted).
-- Explanation:
SELECT COUNT(c.ID)
FROM Class c
JOIN Type t on c.TID = t.ID
WHERE t.name ILIKE '%piano%'; 
-- þetta er rett 


-- D
-- How many different instructors have led at least one class attended by
-- a learner that they personally tutor?
-- Explanation:
SELECT COUNT(DISTINCT i.ID) AS diffrenet_instructors
FROM Instructor i
JOIN Class c ON i.ID = c.IID
JOIN Attends a ON c.ID = a.CID
JOIN Learner l ON a.LID = l.ID
WHERE l.IID = i.ID;



-- E
-- Return each class type name with the average rating of all classes of
-- that type. The result should be rounded to the nearest integer and ordered
-- from highest to lowest. Name the column with the average rating “Average
-- Rating”
-- Explanation:
SELECT 
    t.name AS "CLass Type",
    ROUND(AVG(a.rating)) AS "Average Rating"
FROM Type t
JOIN Class c ON t.ID = c.TID
JOIN Attends a ON c.ID = a.CID
GROUP BY t.ID ORDER BY "Average Rating" DESC;


-- F
-- How many learners have not attended any classes and are not being
-- tutored by an instructor?
-- Explanation:
SELECT COUNT(l.ID) AS learners_not_attended_and_tutored
FROM Learner l
JOIN Attends a ON l.ID = a.LID
WHERE l.IID IS NULL AND a.LID IS NULL;


-- G
-- How many instructors have led 10 or more classes?
-- Explanation:
SELECT COUNT(*) AS instructors_led_more_then_10
FROM(
    SELECT COUNT(i.ID)
    FROM Instructor i
    JOIN Class c ON i.ID = c.IID
    GROUP BY i.ID
    HAVING COUNT(c.IID) >= 10 
);


-- H
-- For how many learners is it true that there exists at least one other
-- learner with the same first name as them, and they also share a tutoring
-- instructor? (Note that if that is true for Mary Smith and Mary Johnson, they
-- should be counted as two results. Note also that two learners that have no
-- instructor cannot be considered as having the same instructor.).
-- Explanation:
SELECT COUNT(DISTINCT l1.ID)
FROM Learner l1
JOIN Learner l2 ON l1.name = l2.name AND l1.ID <> l2.ID
JOIN Instructor i ON l1.IID = i.ID AND l2.IID = i.ID
WHERE l1.IID IS NOT NULL AND l2.IID IS NOT NULL;



-- I
-- How many classes were held at schools in Reykjavik with capacity
-- between 30 and 40 (inclusive), but were not full?
-- Explanation:
SELECT COUNT(*) AS classes_not_full
FROM (
    SELECT COUNT(c.ID)
    FROM Class c
    JOIN Type t ON t.ID = c.TID
    JOIN School s ON s.ID = SID
    LEFT JOIN Attends a ON a.CID = c.ID
    WHERE s.address LIKE '%Reykjavik%' 
        AND t.capacity BETWEEN 30 AND 40
    GROUP BY c.ID, t.capacity
    HAVING COUNT(a.LID) < t.capacity
);


-- J
-- Which instructor(s) has/have led the most total class time (minutes)?
-- Return the ID, name and total minutes.
-- Explanation:
SELECT
    i.ID,
    i.name,
    SUM(c.minutes) AS total_minutes
FROM Instructor i
JOIN Class c ON i.ID = c.IID
GROUP BY i.ID, i.name
HAVING SUM(c.minutes) = (SELECT MAX(total_minutes)
    FROM (
        SELECT MAX(minutes) AS total_minutes
        FROM CLass
        GROUP BY IID ) AS total_class_times
    );