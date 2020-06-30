## Leetcode Databse Problems (Based on MySQL)

* Question 1: Write an SQL query to find the id and the name of all students who are enrolled in departments that no longer exists.

SELECT id, name FROM Students 
WHERE department_id NOT IN (SELECT id FROM Departments)
ORDER BY id;

* Question 2: Write an SQL query to show the unique ID of each user, If a user doesn't have a unique ID replace just show null.

SELECT E2.unique_id, E1.name 
FROM Employees E1 
LEFT JOIN EmployeeUNI E2 
ON E1.id = E2.id 
ORDER BY E1.id;
