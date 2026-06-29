-- Автор с наибольшим количеством проданных книг
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
    authors.last_name
HAVING total_sales = (
    SELECT MAX(author_sales)
    FROM (
        SELECT
            SUM(sales.quantity) AS author_sales
        FROM books
        INNER JOIN sales
            ON books.id = sales.book_id
        GROUP BY books.author_id
    )
);


-- Книги, проданные в количестве выше среднего
SELECT
    books.title,
    SUM(sales.quantity) AS total_sales
FROM books
INNER JOIN sales
    ON books.id = sales.book_id
GROUP BY
    books.id,
    books.title
HAVING total_sales > (
    SELECT AVG(book_sales)
    FROM (
        SELECT
            SUM(quantity) AS book_sales
        FROM sales
        GROUP BY book_id
    )
);