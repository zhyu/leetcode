select A.Name as Customers from Customers as A where A.Id not in (select distinct(B.CustomerId) from Orders as B);
