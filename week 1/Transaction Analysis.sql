--____________________________________________________Transaction Analysis_________________________________________________________________--
-- proc to see who have more than one account 
create procedure Multiacount 
AS
select c.FName+' '+c.LName fullname,c.customer_id,count(amount) As MUltiacount 
from TheTransaction T inner join customer c on c.customer_id=t.customer_id
group by c.FName+' '+c.LName,c.customer_id
having count(amount)>1
order by count(amount) desc

Exec Multiacount
-------- proc to see how much people use certine account 
create procedure PaymentMethod_Analysis
As
select payment_method ,count(*) as Customers
from TheTransaction
group by payment_method
order by count(*) desc

exec PaymentMethod_Analysis
 -------- proc to see payment status for the customers 
 create procedure PaymentStatus_Analysis
 As
 select payment_status ,count(*) as Customers
 from TheTransaction
 group by payment_status
 order by count(*) desc

 exec PaymentStatus_Analysis

 ---------what currency the customers use the most
 create procedure MostUsedCurr
 As
select currency ,count(*) as Customers
 from TheTransaction
 group by currency
 order by count(*) desc


 exec MostUsedCurr

