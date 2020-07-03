## Leetcode Databse Problems (MySQL)

#### Question #1350: Write an SQL query to find the id and the name of all students who are enrolled in departments that no longer exists.

SELECT id, name FROM Students WHERE department_id NOT IN (SELECT id FROM Departments)ORDER BY id;

#### Question #1378: Write an SQL query to show the unique ID of each user, If a user doesn't have a unique ID replace just show null.

SELECT E2.unique_id, E1.name FROM Employees E1 LEFT JOIN EmployeeUNI E2 ON E1.id = E2.id ORDER BY E1.id;

#### Question #1303: Write an SQL query to find for each date, the number of distinct products sold and their names. The sold-products names for each date should be sorted lexicographically. 

SELECT sell_date, COUNT(DISTINCT product) AS num_sold, GROUP_CONCAT(DISTINCT product) AS products FROM Activities GROUP BY sell_date ORDER BY sell_date;

#### Question #1484: Write an SQL query to find the team size of each of the employees.

SELECT employee_id, COUNT(employee_id) OVER (PARTITION BY team_id) AS team_size FROM Employee;

#### Question #1068: Write an SQL query that reports all product names of the products in the Sales table along with their selling year and price.

SELECT product_name, year, price FROM Sales s JOIN Product p ON s.product_id = p.product_id; 

#### Question #1069: Write an SQL query that reports the total quantity sold for every product id.

SELECT product_id, sum(quantity) AS total_quantity FROM Sales GROUP BY product_id;

#### Question #1407: Write an SQL query to report the distance travelled by each user. Return the result table ordered by travelled_distance in descending order, if two or more users travelled the same distance, order them by their name in ascending order.

SELECT name, Ifnull(sum(distance),0) AS travelled_distance FROM Users u LEFT JOIN Rides r ON u.id = r.user_id GROUP BY name ORDER BY travelled_distance DESC, name;

#### Question #1251: Write an SQL query to find the average selling price for each product.average_price should be rounded to 2 decimal places.

SELECT p.product_id as product_id, ROUND((sum(price*units))/(sum(units)),2) as average_price FROM Prices p JOIN UnitsSold u ON p.product_id = u.product_id AND (purchase_date BETWEEN start_date AND end_date) GROUP BY p.product_id;

#### Question #511: Write an SQL query that reports the first login date for each player
SELECT player_id, min(event_date) as first_login FROM Activity GROUP BY player_id;

