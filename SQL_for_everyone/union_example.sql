-- 방법 1) table을 일단 합치고 20개 밑의 상품 개수 배열을 출력
SELECT item_type, array_agg(name)
FROM (
(
SELECT name, quantity, 'drink' AS item_type
FROM drink
)
UNION ALL
(
SELECT name, quantity, 'ramen' AS item_type
FROM ramen
)
UNION ALL
(
SELECT name, quantity, 'canned_food' AS item_type
FROM canned_food
)
) item_list
WHERE  quantity <= 20
GROUP BY 1;

-- 방법 2) 20개 밑인 상품 개수 배열을 먼저 만들고 합침
SELECT item_type, array_agg
FROM (
(
SELECT 'drink' AS item_type, array_agg(name)
    FROM drink
    WHERE quantity <= 20
    GROUP BY 1
)
UNION ALL
(
SELECT 'ramen' AS item_type, array_agg(name)
FROM ramen
WHERE quantity <= 20
GROUP BY 1
)
UNION ALL
(
SELECT 'canned_food' AS item_type, array_agg(name)
FROM canned_food
WHERE quantity <= 20
GROUP BY 1
)
) item_list;