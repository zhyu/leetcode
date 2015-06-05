select employee.name as Employee from Employee as employee inner join Employee as manager on employee.ManagerId=manager.Id where employee.Salary>manager.Salary;
