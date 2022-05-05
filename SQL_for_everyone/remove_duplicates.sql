-- Column에 board_pk, board_user, register_date, title, description, likes, image_name이 있을 때,
-- title, description, register_date의 세 가지 항목으로 중복된 행을 찾아서 row_num이라는 칼럼에 중복된 횟수를 저장하고,
-- row_num이 1보다 큰 경우를 제거하여 1만 남김

SELECT *
FROM (SELECT board_pk, board_user, register_date, title, description, likes, image_name,
	 ROW_NUMBER() OVER (PARTITION BY title, description, register_date) as row_num
	 FROM board) a
WHERE row_num > 1
ORDER BY board_pk;
