# Write your MySQL query statement below
SELECT MAX(salary) as SecondHighestSalary FROM (
    SELECT salary, 
           DENSE_RANK() OVER (ORDER BY salary DESC) as rnk
    FROM employee 
) AS t WHERE rnk = 2;