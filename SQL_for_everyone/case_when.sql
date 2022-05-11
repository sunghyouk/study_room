
SELECT * FROM student_score;

-- CASE phrase example
SELECT id, name, score,
CASE 
WHEN score <= 100 AND score >= 90 THEN 'A'
WHEN score <= 89 AND score >=80 THEN 'B'
WHEN score <= 79 AND score >=70 THEN 'C'
WHEN score < 70 THEN 'F'
END grade
FROM student_score;

-- COALESE() function example
-- insert null
INSERT INTO student_score(name, score)
VALUES ('Youjun', NULL), ('MINJOO', NULL);

-- COALESE and re-classification
SELECT id, name, COALESCE(score, 0),
CASE
WHEN score <= 100 AND score >= 90 THEN 'A'
WHEN score <= 89 AND score >=80 THEN 'B'
WHEN score <= 79 AND score >=70 THEN 'C'
WHEN COALESCE(score, 0) < 70 THEN 'F'
END grade
FROM student_score;