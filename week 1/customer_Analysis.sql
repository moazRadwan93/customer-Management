--__________________________________________________________Customer Analysis_____________________________________________________________--

--proc to see how maney customers in each country
create procedure CustomersInCountries
AS
select country , count(customer_id) as customers_in_countris
from The_address
Group by country
order by country


exec CustomersInCountries
--proc to see who of the customers have multiaddress and by how much
create procedure CustomersHaveMultiAddress
As
select c.customer_id ,c.FName +' '+ c.LName as fullName , count(TA.city) as NUMofPLACESinCity 
from customer as c join The_address as TA ON c.customer_id = TA.customer_id
group by c.customer_id,c.FName,c.LName
order by NUMofPLACESinCity  desc

exec CustomersHaveMultiAddress


-- proc to see who maney customers have multiphones and by how maney
create procedure CustomersHaveMultiPhone
AS
select c.customer_id ,c.FName +' '+ c.LName as fullName , count(p.phone) as NUMofPhones
from customer as c join Customer_phone as p ON c.customer_id = p.customer_id
group by c.customer_id,c.FName,c.LName 
order by NUMofPhones desc

exec CustomersHaveMultiPhone


--number of customers in each year 
create procedure CUSTOMERSBIRTHDAY
AS 
select Year(c.date_of_birth) as year_of_birth ,count(c.customer_id) as CustomersInYear
from customer as c
group by year(c.date_of_birth)
order by CustomersInYear desc

exec CUSTOMERSBIRTHDAY

--how maney male and female
create procedure GENDERcounter
AS
select c.gender , count(c.customer_id) as NUMof_each_Gender
from customer as c 
group by c.gender
order by NUMof_each_Gender desc

exec GENDERcounter




