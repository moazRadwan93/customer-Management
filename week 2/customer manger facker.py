import random
from faker import Faker
import pandas as pd

# Create a Faker instance
fake = Faker()

# Data storage
customer_data = []
transaction_data = []
interaction_data = []
customer_phone_data = []
agent_data = []
address_data = []
interaction_agent_data = []

# We will generate 11,000 rows of data for most of the tables
num_customers = 5000
num_transactions = 5000
num_interactions = 5000
num_phones = 5000
num_agents = 50  # Assuming fewer agents
num_addresses = 5000
num_interaction_agent = 5000

# Generate data for the `customer` table (5000 customers)
for _ in range(num_customers):
    customer_data.append({
        "customer_id": random.randint(1, 1000000),
        "date_of_birth": fake.date_of_birth(minimum_age=18, maximum_age=90),
        "gender": random.choice(['M', 'F']),
        "email": fake.email(),
        "username": fake.user_name(),
        "Account_password": fake.password(length=10),
        "FName": fake.first_name(),
        "LName": fake.last_name()
    })

# Generate data for the `TheTransaction` table (5000 transactions)
for _ in range(num_transactions):
    transaction_data.append({
        "Transaction_id": random.randint(1, 1000000),
        "amount": random.randint(10, 10000),
        "currency": random.choice(['USD', 'EUR', 'EGP']),
        "Transaction_type": random.choice(['Purchase', 'Refund', 'Transfer']),
        "payment_method": random.choice(['Credit Card', 'Debit Card', 'PayPal']),
        "payment_status": random.choice(['Completed', 'Pending', 'Failed']),
        "customer_id": random.randint(1, 1000000)
    })

# Generate data for the `Interaction` table (5000 interactions)
for _ in range(num_interactions):
    interaction_data.append({
        "Interaction_id": random.randint(1, 1000000),
        "interaction_type": random.choice(['Call', 'Email', 'Chat']),
        "interaction_outcome": random.choice(['Positive', 'Negative', 'Neutral']),
        "follow_up_required": random.choice(['Yes', 'No']),
        "interaction_channel": random.choice(['Phone', 'Email', 'In-Person']),
        "follow_up_date": fake.date_this_year(),
        "customer_id": random.randint(1, 1000000)
    })

# Generate data for the `Customer_phone` table (5000 phone numbers)
for _ in range(num_phones):
    customer_phone_data.append({
        "phone": fake.phone_number(),
        "customer_id": random.randint(1, 1000000)
    })

# Generate data for the `Agent` table (50 agents)
for _ in range(num_agents):
    agent_data.append({
        "Agent_id": random.randint(1, 1000000),
        "FName": fake.first_name(),
        "LName": fake.last_name()
    })

# Generate data for the `The_address` table (5000 addresses)
for _ in range(num_addresses):
    address_data.append({
        "country": fake.country(),
        "government": fake.state(),
        "city": fake.city(),
        "customer_id": random.randint(1, 1000000)
    })

# Generate data for the `interaction_Agent_manger` table (5000 interaction-agent assignments)
for _ in range(num_interaction_agent):
    interaction_agent_data.append({
        "interaction_id": random.randint(1, 1000000),
        "Agent_id": random.randint(1, 1000000)
    })

# Convert data into DataFrames
customer_df = pd.DataFrame(customer_data)
transaction_df = pd.DataFrame(transaction_data)
interaction_df = pd.DataFrame(interaction_data)
customer_phone_df = pd.DataFrame(customer_phone_data)
agent_df = pd.DataFrame(agent_data)
address_df = pd.DataFrame(address_data)
interaction_agent_df = pd.DataFrame(interaction_agent_data)

# Save each DataFrame as a separate Excel file
customer_df.to_excel("customer_data_11000.xlsx", index=False)
transaction_df.to_excel("transaction_data_11000.xlsx", index=False)
interaction_df.to_excel("interaction_data_11000.xlsx", index=False)
customer_phone_df.to_excel("customer_phone_data_11000.xlsx", index=False)
agent_df.to_excel("agent_data_11000.xlsx", index=False)
address_df.to_excel("address_data_11000.xlsx", index=False)
interaction_agent_df.to_excel("interaction_agent_data_11000.xlsx", index=False)

print("Data with 11,000 rows has been exported to separate Excel files.")
