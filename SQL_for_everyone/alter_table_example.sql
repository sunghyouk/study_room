-- add column
CREATE TABLE book_info (
    id INTEGER NOT NULL PRIMARY KEY,
    name VARCHAR(20) NOT NULL
);

INSERT INTO book_info VALUES(1, 'POSTGRESQL'), (2, 'MONGODB');

ALTER TABLE book_info
ADD COLUMN published_date DATE;

SELECT * FROM book_info;

UPDATE book_info
SET published_date = '2020.12.25'
WHERE id = 1;

UPDATE book_info
SET published_date = '2020.12.27'
WHERE id = 2;

ALTER TABLE book_info
ALTER COLUMN published_date SET NOT NULL;

-- drop column with reference
DROP TABLE IF EXISTS book_info;

CREATE TABLE book_info (
    book_id INTEGER NOT NULL PRIMARY KEY,
    book_name VARCHAR(20) NOT NULL UNIQUE
);

INSERT INTO book_info VALUES(1, 'POSTGRESQL'), (2, 'MONGODB');

CREATE TABLE library(
    id INTEGER NOT NULL PRIMARY KEY,
    name VARCHAR(40) NOT NULL,
    book_name VARCHAR(20) NOT NULL REFERENCES book_info(book_name)
);

INSERT INTO library VALUES(1, '국립도서관', 'POSTGRESQL');

SELECT * FROM book_info;

ALTER TABLE book_info DROP COLUMN book_name CASCADE;

SELECT * FROM book_info;

-- rename column
-- 한번에 하나씩만 바꿀 수 있다.
DROP TABLE book_info;
DROP TABLE library;

CREATE TABLE book_info (
    book_id INTEGER NOT NULL PRIMARY KEY,
    book_name VARCHAR(20) NOT NULL UNIQUE
);

INSERT INTO book_info VALUES(1, 'POSTGRESQL'), (2, 'MONGODB');

CREATE TABLE library(
    id INTEGER NOT NULL PRIMARY KEY,
    name VARCHAR(40) NOT NULL,
    book_name VARCHAR(20) NOT NULL REFERENCES book_info(book_name)
);

INSERT INTO library VALUES (1, '국립도서관', 'POSTGRESQL');

ALTER TABLE book_info RENAME book_name TO name;