-- Создание таблицы
CREATE TABLE Employees (
    Name TEXT NOT NULL,
    Position TEXT NOT NULL,
    Department TEXT NOT NULL,
    Salary REAL NOT NULL
);

-- Добавление данных
INSERT INTO Employees (Name, Position, Department, Salary)
VALUES
    ('Иван Иванов', 'Developer', 'IT', 4500),
    ('Петр Петров', 'Manager', 'Sales', 6500),
    ('Анна Сидорова', 'Accountant', 'Finance', 5200),
    ('Мария Смирнова', 'Sales Manager', 'Sales', 5800);

-- Изменение должности сотрудника
UPDATE Employees
SET Position = 'Senior Developer'
WHERE Name = 'Иван Иванов';

-- Добавление нового поля
ALTER TABLE Employees
ADD COLUMN HireDate DATE;

-- Заполнение даты приема на работу
UPDATE Employees
SET HireDate = '2022-01-15'
WHERE Name = 'Иван Иванов';

UPDATE Employees
SET HireDate = '2021-06-10'
WHERE Name = 'Петр Петров';

UPDATE Employees
SET HireDate = '2023-03-20'
WHERE Name = 'Анна Сидорова';

UPDATE Employees
SET HireDate = '2022-09-01'
WHERE Name = 'Мария Смирнова';

-- Найти всех менеджеров
SELECT *
FROM Employees
WHERE Position = 'Manager';

-- Найти сотрудников с зарплатой больше 5000
SELECT *
FROM Employees
WHERE Salary > 5000;

-- Найти сотрудников отдела Sales
SELECT *
FROM Employees
WHERE Department = 'Sales';

-- Найти среднюю зарплату
SELECT AVG(Salary) AS AverageSalary
FROM Employees;

-- Удалить таблицу
DROP TABLE Employees;