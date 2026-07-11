-- INNER JOIN: список всех книг и их авторов
SELECT
    books.title,
    authors.first_name,
    authors.last_name
FROM books
INNER JOIN authors
ON books.author_id = authors.id;


-- LEFT JOIN: список всех авторов и их книг
SELECT
    authors.first_name,
    authors.last_name,
    books.title
FROM authors
LEFT JOIN books
ON authors.id = books.author_id;


-- RIGHT JOIN: список всех книг и их авторов
SELECT
    books.title,
    authors.first_name,
    authors.last_name
FROM authors
RIGHT JOIN books
ON authors.id = books.author_id;