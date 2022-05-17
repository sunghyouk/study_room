-- 5-4 Excercise
-- View entire table
SELECT * FROM population_by_year;

-- 1) 전국의 인구수 총합을 년도 별로 표시
SELECT 년도, sum(총인구수) AS 총인구수
FROM population_by_year
GROUP BY 1
ORDER BY 1;

-- 2) 2014년 이후 전국의 한 세대당 평균 인구수 보기
SELECT 년도, avg(총인구수::numeric/세대수) AS "세대당 인구수"
FROM population_by_year
WHERE 년도 > 2014
GROUP BY 1
ORDER BY 1;

-- 3) 2014년 이후 남자/여자 인구수 성비의 평균을 행정구역별로 출력하고 가장 높은 지역 표시
SELECT 행정구역, avg(남자_인구수::numeric/여자_인구수) AS 성비
FROM population_by_year
WHERE 년도 > 2014
GROUP BY 행정구역
ORDER BY 성비 DESC;