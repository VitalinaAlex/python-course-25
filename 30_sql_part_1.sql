
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
