# Write your MySQL query statement below
With ranked AS (SELECT 
    d.name AS Department, 
    e.name AS Employee, 
    e.salary AS Salary,
    DENSE_RANK() OVER (PARTITION BY d.name ORDER BY e.Salary DESC) as rnk
FROM Employee e
LEFT JOIN Department d
ON e.departmentId = d.id) 
SELECT Department, Employee, Salary FROM ranked where rnk = 1;
