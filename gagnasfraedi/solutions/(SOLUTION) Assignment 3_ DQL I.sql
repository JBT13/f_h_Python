-- T-202-GAG1: Assignment 3
-- Student names: Solution

-- A
SELECT min(E.price)
FROM Equipment E;


-- B
SELECT count(*)
FROM Class C
WHERE extract(day FROM C.date) = 29 
AND extract(month FROM C.date) = 2;


-- C
SELECT count(*)
FROM Class C 
JOIN Type T ON T.ID = C.TID 
WHERE lower(T.name) LIKE '%piano%';


-- D
SELECT COUNT(DISTINCT C.IID)
FROM Class C
JOIN Attends A ON A.CID = C.ID
JOIN Learner L ON L.ID = A.LID
WHERE L.IID = C.IID;


-- E
SELECT T.name, ROUND(AVG(A.rating)) AS "Average Rating"
FROM Type T
JOIN Class C ON C.TID = T.ID
JOIN Attends A ON A.CID = C.ID
GROUP BY T.ID
ORDER BY "Average Rating" DESC;


-- F
SELECT COUNT(*)
FROM Learner L
WHERE L.ID NOT IN (
    SELECT A.LID 
    FROM Attends A
)
  AND L.IID IS NULL;


-- G
SELECT COUNT(*)
FROM (
    SELECT C.IID
    FROM Class C
    GROUP BY C.IID
    HAVING COUNT(*) >= 10
) X;


-- H
SELECT COUNT(DISTINCT L1.ID)
FROM Learner L1
JOIN Learner L2
  ON SPLIT_PART(L1.name, ' ', 1) = SPLIT_PART(L2.name, ' ', 1)  -- same first name
 AND L1.IID = L2.IID                                            -- same instructor
WHERE L1.ID <> L2.ID;


--I
SELECT COUNT(*)
FROM (
    SELECT C.ID
    FROM Class C
    JOIN School S ON S.ID = C.SID
    JOIN Type T ON T.ID = C.TID
    LEFT JOIN Attends A ON A.CID = C.ID
    WHERE S.address ILIKE '%Reykjavik%'
      AND T.capacity BETWEEN 30 AND 40
    GROUP BY C.ID, T.capacity
    HAVING COUNT(A.LID) < T.capacity
) X;


-- J
SELECT I.ID, I.name, SUM(C.minutes) AS total_minutes
FROM Instructor I
JOIN Class C ON C.IID = I.ID
GROUP BY I.ID, I.name
HAVING SUM(C.minutes) = (
    SELECT MAX(total_minutes)
    FROM (
        SELECT SUM(minutes) AS total_minutes
        FROM Class
        GROUP BY IID
    ) X
);