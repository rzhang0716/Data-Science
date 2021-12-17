<h1>Leetcode Databse Problems (MySQL)

#### Question #175: Write an SQL query to report the first name, last name, city, and state of each person in the Person table. If the address of a personId is not present in the Address table, report null instead.
select firstName, lastName,  city,state from Person p left join Address a on p.personID = a.personID;
  
#### Question #181: Write an SQL query to find the employees who earn more than their managers.
select e1.name as Employee from Employee e1 join Employee e2 on e1.managerId = e2.id where e1.salary > e2.salary;

#### Question #182: Write an SQL query to report all the duplicate emails.
 select distinct p1.email Email from Person p1 join Person p2 where p1.email = p2.email and p1.id != p2.id;
  
#### Question #183: Write an SQL query to report all customers who never order anything.
select name Customers from Customers c left join Orders o on c.id = o.customerID where o.customerID is null;

#### Question #196: Write an SQL query to delete all the duplicate emails, keeping only one unique email with the smallest id.  
delete p1 from Person p1, Person p2 where p1.email = p2.email and p1.id > p2.id;

#### Question #197:Write an SQL query to find all dates' Id with higher temperatures compared to its previous dates (yesterday).
select w2.id from Weather w1 join Weather w2 where datediff(w1.recordDate, w2.recordDate) = -1 and w1.temperature < w2.temperature;
  
#### Question #511: Write an SQL query that reports the first login date for each player
SELECT player_id, min(event_date) as first_login FROM Activity GROUP BY player_id;
                                                                                                                                   
#### Question #512: Write an SQL query to report the device that is first logged in for each player.
select a1.player_id, a1.device_id from Activity a1 join (select player_id, min(event_date) m from Activity group by player_id) a2 on a1.player_id = a2.player_id and a1.event_date = a2.m;
                                                                                                                                   
#### Question #595: Write a SQL solution to output big countries' name, population and area.
SELECT name, population, area FROM World WHERE population > 25000000 OR area > 3000000;

#### Question #613: Write a query to find the shortest distance between two points in these points.
SELECT min(abs(a.x-b.x)) as shortest FROM point a JOIN point b WHERE a.x != b.x;

#### Question #1068: Write an SQL query that reports all product names of the products in the Sales table along with their selling year and price.
SELECT product_name, year, price FROM Sales s JOIN Product p ON s.product_id = p.product_id; 

#### Question #1069: Write an SQL query that reports the total quantity sold for every product id.
SELECT product_id, sum(quantity) AS total_quantity FROM Sales GROUP BY product_id;

#### Question #1173: Write an SQL query to find the percentage of immediate orders in the table, rounded to 2 decimal places.
SELECT round(sum(order_date = customer_pref_delivery_date)*100/count(*),2) as immediate_percentage FROM Delivery;

#### Question #1251: Write an SQL query to find the average selling price for each product.average_price should be rounded to 2 decimal places.
SELECT p.product_id as product_id, ROUND((sum(price*units))/(sum(units)),2) as average_price FROM Prices p JOIN UnitsSold u ON p.product_id = u.product_id AND (purchase_date BETWEEN start_date AND end_date) GROUP BY p.product_id;

#### Question #1303: Write an SQL query to find for each date, the number of distinct products sold and their names. The sold-products names for each date should be sorted lexicographically. 
SELECT sell_date, COUNT(DISTINCT product) AS num_sold, GROUP_CONCAT(DISTINCT product) AS products FROM Activities GROUP BY sell_date ORDER BY sell_date;
  
#### Question #1350: Write an SQL query to find the id and the name of all students who are enrolled in departments that no longer exists.
SELECT id, name FROM Students WHERE department_id NOT IN (SELECT id FROM Departments)ORDER BY id;
  
#### Question #1378: Write an SQL query to show the unique ID of each user, If a user doesn't have a unique ID replace just show null.
SELECT E2.unique_id, E1.name FROM Employees E1 LEFT JOIN EmployeeUNI E2 ON E1.id = E2.id ORDER BY E1.id;

#### Question #1407: Write an SQL query to report the distance travelled by each user. Return the result table ordered by travelled_distance in descending order, if two or more users travelled the same distance, order them by their name in ascending order.
SELECT name, Ifnull(sum(distance),0) AS travelled_distance FROM Users u LEFT JOIN Rides r ON u.id = r.user_id GROUP BY name ORDER BY travelled_distance DESC, name;

#### Question #1484: Write an SQL query to find the team size of each of the employees.
SELECT employee_id, COUNT(employee_id) OVER (PARTITION BY team_id) AS team_size FROM Employee;

















