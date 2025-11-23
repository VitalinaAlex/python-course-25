/*Task 1
Joins
Use the sample SQLite database hr.db (same database you used in the previous lesson for homework tasks)
As a solution to HW, create a file named: task1.sql with all SQL queries:
write a query in SQL to display the first name, last name, department number, and department name for each employee*/
SELECT 
    em.first_name AS "First Name",
    em.last_name AS "Last Name", 
    em.department_id as "department id",
    dep.department_name
FROM employees as em
JOIN department as dep 
	on em.department_id=dep.department_id;
--write a query in SQL to display the first and last name, department, city, and state province for each employee
SELECT 
    em.first_name AS "First Name",
    em.last_name AS "Last Name", 
    em.department_id as "department id",
    loc.city,
    loc.state_province
FROM employees as em
JOIN departments as dep 
	on em.department_id=dep.department_id
JOIN locations as loc 
	on dep.location_id=loc.location_id;
--write a query in SQL to display the first name, last name, department number, and department name, for all employees for departments 80 or 40
SELECT 
    em.first_name AS "First Name",
    em.last_name AS "Last Name", 
    em.department_id as "department id",
    dep.department_name
FROM employees as em
JOIN department as dep 
	on em.department_id=dep.department_id
WHERE em.department_id in (40,80);
--write a query in SQL to display all departments including those where does not have any employee
SELECT 
    d.department_id,
    d.depart_name,
    em.employee_id,
    em.first_name AS "First Name",
    em.last_name AS "Last Name"
FROM departments d
LEFT JOIN employees em
    ON d.department_id = em.department_id
--write a query in SQL to display the first name of all employees including the first name of their manager
SELECT 
    em.first_name AS "First Name",
    em.last_name AS "Last Name",
FROM employees em
JOIN jobs j
	ON j.job_id = em.job_id;
--write a query in SQL to display the job title, full name (first and last name ) of the employee, and the difference between the maximum salary for the job and the salary of the employee
SELECT 
	em.employee_id as "employee ID",
    em.first_name AS "First Name",
    em.manager_id AS "manager ID",
    em2.first_name as "Manager First Name"
FROM employees em
JOIN employees as em2    
	ON em.manager_id = em2.employee_id
order by em.first_name;
--write a query in SQL to display the job title and the average salary of employees
SELECT 
    em.first_name AS "First Name",
    em.last_name AS "Last Name",
    em.job_id as "Job ID",
    j.job_title as "Job title",
    (j.min_salary+j.max_salary)/2 as "Average salary for job title",
    em.salary as "employee salary"
FROM employees em
JOIN jobs j    
	ON j.job_id = em.job_id;
--write a query in SQL to display the full name (first and last name), and salary of those employees who work in any department located in London
SELECT 
    em.first_name || ' ' || em.last_name AS full_name,
    em.salary,
    em.department_id,
    dep.location_id,
    l.city
FROM employees as em
JOIN department as dep 
	on em.department_id = dep.department_id
JOIN locations as l 
	on dep.location_id = l.location_id
WHERE l.city ='London';
--write a query in SQL to display the department name and the number of employees in each department
SELECT department_name, 
	COUNT(em.department_id) as count
FROM department as d
JOIN employees as em on d.department_id=em.department_id
GROUP BY d.department_id, d.department_name;
