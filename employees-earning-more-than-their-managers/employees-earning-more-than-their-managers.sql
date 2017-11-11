# Write your MySQL query statement below
SELECT a.Name as Employee
FROM Employee as a
INNER JOIN Employee as b
ON a.ManagerId = b.Id
WHERE a.Salary > b.Salary;
