-- Problem 1 (EASY)

SELECT 기준년도, 학교명, 학교급명, 졸업남자수, 졸업여자수 from graduates
WHERE 학교급명 = '특수학교' AND (졸업남자수 + 졸업여자수) >= 25;