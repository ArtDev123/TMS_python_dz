-- 1 Задание

CREATE TABLE Employees(
id INT PRIMARY KEY,
Name VARCHAR(50),
Position VARCHAR(50),
Department VARCHAR(50),
Salary DECIMAL(10, 2)
);

-- 2 Задание

INSERT INTO Employees (id, Name, Position, Department, Salary) VALUES
(1, 'Maksi', 'Manager', 'IT', 50000.00),
(2, 'Anna', 'Developer', 'IT', 60000.00),
(3, 'Bob', 'Designer', 'Design', 45000.00),
(4, 'Charlie', 'Analyst', 'Finance', 48000.00),
(5, 'Diana', 'HR', 'HR', 42000.00),
(6, 'Eve', 'Developer', 'IT', 58000.00),
(7, 'Frank', 'Manager', 'Sales', 52000.00),
(8, 'Grace', 'Tester', 'QA', 38000.00),
(9, 'Henry', 'Analyst', 'Finance', 47000.00),
(10, 'Ivy', 'Designer', 'Design', 44000.00);

-- 3 Задание
-- Измените данные в таблице для каких-то сотрудников.

UPDATE Employees
SET Salary = Salary / 2
WHERE Salary > 55000;
SELECT * FROM Employees

-- 4 Задание
-- Добавьте новое поле "HireDate" (дата приема на работу) в
-- таблицу "Employees".

ALTER TABLE Employees
ADD HireDate DATE DEFAULT NULL;
SELECT * FROM Employees;

-- 5 Задание
-- Добавьте новое поле "HireDate" (дата приема на работу) в
-- таблицу "Employees".

UPDATE Employees SET HireDate = CASE id
    WHEN 1 THEN '2023-01-15'
    WHEN 2 THEN '2023-02-20'
    WHEN 3 THEN '2023-03-10'
    WHEN 4 THEN '2023-04-05'
    WHEN 5 THEN '2023-05-12'
    WHEN 6 THEN '2023-06-18'
    WHEN 7 THEN '2023-07-22'
    WHEN 8 THEN '2023-08-30'
    WHEN 9 THEN '2023-09-14'
    WHEN 10 THEN '2023-10-01'
END::date;
SELECT * FROM Employees

-- 6 Задание
-- Найдите всех сотрудников, чья должность "Manager".

CREATE FUNCTION find_position_manager()
RETURNS TEXT
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN (SELECT STRING_AGG(Name, ', ') FROM Employees WHERE Position = 'Manager');
END;
$$;

SELECT find_position_manager();

-- 7 Задание
-- Найдите всех сотрудников, у которых зарплата больше 5000 долларов.

CREATE FUNCTION bigger_salary()
RETURNS TEXT
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN (SELECT STRING_AGG(Name, ', ') FROM Employees WHERE Salary >= 45000);
END;
$$;

SELECT bigger_salary();

-- 8 Задание
-- Найдите всех сотрудников, которые работают в отделе "Sales".

CREATE FUNCTION department_sales()
RETURNS TEXT
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN (SELECT STRING_AGG(Name, ', ') FROM Employees WHERE Department = 'Sales');
END;
$$;

SELECT department_sales();

-- 9 Задание
-- Найдите среднюю зарплату по всем сотрудникам.

CREATE FUNCTION middle_salary()
RETURNS NUMERIC
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN (SELECT AVG(Salary) FROM Employees);
END;
$$;

SELECT middle_salary();

-- 10 Задание
-- Удалите таблицу "Employees"

DROP TABLE Employees;