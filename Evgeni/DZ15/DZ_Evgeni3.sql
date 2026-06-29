-- INNER JOIN: список книг, их авторов и продаж
SELECT
    books.title,
    authors.first_name,
    authors.last_name,
    sales.quantity
FROM books
INNER JOIN authors
    ON books.author_id = authors.id
INNER JOIN sales
    ON books.id = sales.book_id;


-- LEFT JOIN: список всех авторов, их книг и продаж
SELECT
    authors.first_name,
    authors.last_name,
    books.title,
    sales.quantity
FROM authors
LEFT JOIN books
    ON authors.id = books.author_id
LEFT JOIN sales
    ON books.id = sales.book_id;