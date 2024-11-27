from faker import Faker
import datetime

fake = Faker()

# Number of unique Customer_id
num_customers = 11000

# SQL update statement template with Customer_id
update_template = "UPDATE TheTransaction SET Transaction_Date = '{}' WHERE Customer_id = {};"

# Define the date range using datetime.date
start_date = datetime.date(2020, 1, 1)
end_date = datetime.date.today()

# Open a file to store the SQL update statements as a .txt file
with open("fake_transaction_updates_customer_id.txt", "w") as file:
    for customer_id in range(1, num_customers + 1):
        # Generate a fake date between the defined start and end dates
        fake_date = fake.date_between(start_date=start_date, end_date=end_date)
        
        # Write the update statement for the current Customer_id
        update_statement = update_template.format(fake_date, customer_id)
        file.write(update_statement + "\n")

print(f"Generated update statements for {num_customers} customers in 'fake_transaction_updates_customer_id.txt'.")
