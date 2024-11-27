create table Customer(
Customer_Key int,
ID int,
DateOfBirth date,
Gender char(1),
email varchar(255),
UserName varchar(255),
AccountPassword varchar(255),
FName varchar(255),
LName Varchar(255)
);

create table C_Transaction(
Transaction_Key int,
ID int,
Amount int,
Currency char(3),
TransactionType varchar(255),
PaymentType varchar(255),
PaymentStatus varchar(255),
TransactionDate date,
C_ID int
);

create table Interaction(
Interaction_Key int,
ID int,
Interaction_Type varchar(255),
Interaction_Outcome varchar(255),
Follow_Up_Required varchar(3),
Follow_UP_Date date,
C_ID int
);


create table C_Address(
Address_Key int,
Country varchar(255),
Government varchar(255),
city varchar(255),
C_ID int
);

create Table Agent(
Agent_Key int,
FName varchar(255),
LName varchar(255)
);

create table Phone(
Phone_Key int,
Phone int,
C_ID int
);


create table MasterManager (
Master_Key int,
Customer_Key int,
Transaction_Key int,
Interaction_Key int,
Address_Key int,
Agent_Key int,
Phone_key int
)


