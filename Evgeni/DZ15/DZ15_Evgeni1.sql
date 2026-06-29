-- Создание таблицы авторов
CREATE TABLE authors (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
);

-- Создание таблицы книг
CREATE TABLE books (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author_id INTEGER NOT NULL,
    publication_year INTEGER NOT NULL,
    FOREIGN KEY (author_id) REFERENCES authors(id)
);

-- Создание таблицы продаж
CREATE TABLE sales (
    id INTEGER PRIMARY KEY,
    book_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    FOREIGN KEY (book_id) REFERENCES books(id)
);

-- Добавление авторов
INSERT INTO authors (id, first_name, last_name)
VALUES
    (1, 'Александр', 'Пушкин'),
    (2, 'Лев', 'Толстой'),
    (3, 'Федор', 'Достоевский');

-- Добавление книг
INSERT INTO books (id, title, author_id, publication_year)
VALUES
    (1, 'Евгений Онегин', 1, 1833),
    (2, 'Война и мир', 2, 1869),
    (3, 'Анна Каренина', 2, 1877),
    (4, 'Преступление и наказание', 3, 1866);

-- Добавление информации о продажах
INSERT INTO sales (id, book_id, quantity)
VALUES
    (1, 1, 120),
    (2, 2, 85),
    (3, 3, 60),
    (4, 4, 95);