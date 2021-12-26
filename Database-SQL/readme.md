<h1>Leetcode Databse Problems (MySQL)

#### Question #175: Write an SQL query to report the first name, last name, city, and state of each person in the Person table. If the address of a personId is not present in the Address table, report null instead.
select firstName, lastName, city, state from Person p left join Address a on p.personID = a.personID;
  
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

#### Question #577: Write an SQL query to report the name and bonus amount of each employee with a bonus less than 1000.
select name, bonus from Employee e1 left join Bonus b on e1.empId = b.empId where bonus < 1000 or bonus is null;                                                 

#### Question #584: Write an SQL query to report the IDs of the customer that are not referred by the customer with id = 2.
select name from Customer where referee_id != 2 or referee_id is null;
  
#### Question #586: Write an SQL query to find the customer_number for the customer who has placed the largest number of orders.
select customer_number from Orders group by customer_number order by count(order_number) desc limit 1;

#### Question #595: Write a SQL solution to output big countries' name, population and area.
SELECT name, population, area FROM World WHERE population > 25000000 OR area > 3000000;

#### Question #596: Write an SQL query to report all the classes that have at least five students.
select class from Courses group by class having count(class) >=5;
  
#### Question #597: Write an SQL query to find the overall acceptance rate of requests, which is the number of acceptance divided by the number of requests. Return the answer rounded to 2 decimals places.
select ifnull(round((count(distinct requester_id,accepter_id)/count(distinct sender_id,send_to_id)),2),0.00) as accept_rate from FriendRequest, RequestAccepted;

#### Question #603: Write an SQL query to report all the consecutive available seats in the cinema.  
select distinct c1.seat_id from Cinema c1 join Cinema c2 where (abs(c1.seat_id - c2.seat_id) = 1) and (c1.free = 1) and (c2.free = 1) order by c1.seat_id;

#### Question #607: Write an SQL query to report the names of all the salespersons who did not have any orders related to the company with the name "RED".
select name from SalesPerson s left join (select o.sales_id, o.order_id from Orders o join Company c on o.com_id = c.com_id where c.name = 'RED') a on s.sales_id = a.sales_id where a.order_id is null;

#### Question #610: Write an SQL query to report for every three line segments whether they can form a triangle.
select x, y,z, case when (x + y- z >0) and (x+z-y>0) and (y+z-x>0) then 'Yes' else 'No' end as triangle from Triangle;
  
#### Question #613: Write a query to find the shortest distance between two points in these points.
SELECT min(abs(a.x-b.x)) as shortest FROM point a JOIN point b WHERE a.x != b.x;
  
#### Question #619: Write an SQL query to report the largest single number. If there is no single number, report null.
select (select num from MyNumbers group by num having count(num) = 1 order by num desc limit 1) as num;

#### Question #620: Write an SQL query to report the movies with an odd-numbered ID and a description that is not "boring".
select id, movie, description, rating from Cinema where mod(id,2) = 1 and description != 'boring' order by rating desc;
  
#### Question #627: Write an SQL query to swap all 'f' and 'm' values (i.e., change all 'f' values to 'm' and vice versa) with a single update statement and no intermediate temporary tables.
update salary set sex = CHAR(ASCII('f') ^ ASCII('m') ^ ASCII(sex));

#### Question #1050: Write a SQL query for a report that provides the pairs (actor_id, director_id) where the actor has cooperated with the director at least three times.
select actor_id, director_id from ActorDirector group by actor_id, director_id having count(*) >= 3;

#### Question #1068: Write an SQL query that reports all product names of the products in the Sales table along with their selling year and price.
SELECT product_name, year, price FROM Sales s JOIN Product p ON s.product_id = p.product_id; 

#### Question #1069: Write an SQL query that reports the total quantity sold for every product id.
SELECT product_id, sum(quantity) AS total_quantity FROM Sales GROUP BY product_id;

#### Question #1075: Write an SQL query that reports the average experience years of all the employees for each project, rounded to 2 digits.
select project_id, round(avg(experience_years),2) as average_years from Project p join Employee e on p.employee_id = e.employee_id group by project_id;

#### Question #1076: Write an SQL query that reports all the projects that have the most employees.
select project_id from Project group by project_id having count(*) = (select count(*) from Project group by project_id order by count(*) desc limit 1);

#### Question #1082: Write an SQL query that reports the best seller by total sales price, If there is a tie, report them all.
select seller_id from Sales group by seller_id having sum(price) = (select sum(price) from sales group by seller_id order by sum(price) desc limit 1);
  
#### Question #1083: Write an SQL query that reports the buyers who have bought S8 but not iPhone. Note that S8 and iPhone are products present in the Product table.
select buyer_id from sales s join product p on s.product_id = p.product_id group by buyer_id having sum(p.product_name = 'S8') > 0 and sum(p.product_name = 'iPhone') = 0;
  
#### Question #1084: Write an SQL query that reports the products that were only sold in the spring of 2019. That is, between 2019-01-01 and 2019-03-31 inclusive.
SELECT s.product_id, product_name FROM Sales s LEFT JOIN Product p ON s.product_id = p.product_id GROUP BY s.product_id HAVING MIN(sale_date) >= CAST('2019-01-01' AS DATE) AND MAX(sale_date) <= CAST('2019-03-31' AS DATE)

#### Question #1113: Write an SQL query that reports the number of posts reported yesterday for each report reason. Assume today is 2019-07-05.
select extra as report_reason, count(distinct post_id) as report_count from Actions where extra is not null and action_date = '2019-07-04' and action = 'report'
group by extra;

#### Question #1141: Write an SQL query to find the daily active user count for a period of 30 days ending 2019-07-27 inclusively. A user was active on someday if they made at least one activity on that day.
select activity_date as day, count(distinct user_id) as active_users from Activity where datediff('2019-07-27', activity_date) <30 group by activity_date;

#### Question #1142: Write an SQL query to find the average number of sessions per user for a period of 30 days ending 2019-07-27 inclusively, rounded to 2 decimal places. The sessions we want to count for a user are those with at least one activity in that time period.
SELECT ifnull(ROUND(COUNT(DISTINCT session_id)/COUNT(DISTINCT user_id), 2),0.00) AS average_sessions_per_user FROM Activity  WHERE activity_date >= '2019-06-28' and activity_date <= '2019-07-27';

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

















