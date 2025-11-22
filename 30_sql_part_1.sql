
#Task 1
#Create a table
#Create a table of your choice inside the sample SQLite database, rename it, and add a new column. Insert a couple rows inside your table. 
#Also, perform UPDATE and DELETE statements on inserted rows.
#As a solution to this task, create a file named: task1.sql, with all the SQL statements you have used to accomplish this task

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

ALTER TABLE users RENAME TO customers;

ALTER TABLE customers ADD COLUMN email text

INSERT INTO customers (name, email) VALUES
    ('Lina', 'lina@example.com'),
    ('Linka', 'linka@example.com'),
    ('Tim', 'tim@example.com');

UPDATE customers
SET email = 'tim_al@example.com'
WHERE name = 'Tim';

DELETE FROM customers
WHERE name = 'Linka';

SELECT * FROM customers;

/*Task 2
Select queries
Use the sample SQLite database hr.db
As a solution to HW, create a file named: task2.sql with all SQL queries:*/
--write a query to display the names (first_name, last_name) using alias name "First Name", "Last Name" from the table of employees;
SELECT 
    first_name AS "First Name",
    last_name AS "Last Name"
FROM employees;
--write a query to get the unique department ID from the employee table
SELECT DISTINCT department_id as dep_id
FROM employees
order by department_id;
--write a query to get all employee details from the employee table ordered by first name, descending
SELECT *
FROM employees
order by first_name desc;
--write a query to get the names (first_name, last_name), salary, PF of all the employees (PF is calculated as 12% of salary)
SELECT first_name, last_name, salary, salary*0.12 as PF
FROM employees
order by employee_id;
--write a query to get the maximum and minimum salary from the employees table
SELECT MAX(salary) as MAX_SALARY, MIN(salary) as MIN_SALARY
FROM employees;
--write a query to get a monthly salary (round 2 decimal places) of each and every employee
SELECT 
    first_name,
    last_name,
    ROUND(salary / 12.0, 2) AS "Monthly Salary"
FROM employees;
