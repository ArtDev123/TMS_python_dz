-- INNER JOIN: общее количество проданных книг каждого автора
SELECT
    authors.first_name,
    authors.last_name,
    SUM(sales.quantity) AS total_sales
FROM authors
INNER JOIN books
    ON authors.id = books.author_id
INNER JOIN sales
    ON books.id = sales.book_id
GROUP BY
    authors.id,
    authors.first_name,
    authors.last_name;


-- LEFT JOIN: общее количество проданных книг каждого автора,
-- включая авторов без продаж
SELECT
    authors.first_name,
    authors.last_name,
    COALESCE(SUM(sales.quantity), 0) AS total_sales
FROM authors
LEFT JOIN books
    ON authors.id = books.author_id
LEFT JOIN sales
    ON books.id = sales.book_id
GROUP BY
    authors.id,
    authors.first_name,
    authors.last_name;