import pandas as pd
from faker import Faker

# Initialize Faker
fake = Faker()

# Number of records
num_records = 11000

# Generating agents data
agent_data = {
    'Agent_ID': [fake.random_int(min=1001, max=9999) for _ in range(num_records)],
    'First_Name': [fake.first_name() for _ in range(num_records)],
    'Last_Name': [fake.last_name() for _ in range(num_records)]
}
agent_df = pd.DataFrame(agent_data)

# Generating interactions data
interaction_data = {
    'Interaction_ID': [fake.random_int(min=2001, max=9999) for _ in range(num_records)],
    'Interaction_Type': [fake.random_element(elements=('Phone', 'Email', 'Chat', 'In-Person')) for _ in range(num_records)],
    'Interaction_Outcome': [fake.random_element(elements=('Resolved', 'Pending', 'Escalated', 'In-Progress')) for _ in range(num_records)],
    'Follow_Up_Required': [fake.random_element(elements=('Yes', 'No')) for _ in range(num_records)],
    'Interaction_Channel': [fake.random_element(elements=('Call', 'Email', 'Web Chat', 'In-Person')) for _ in range(num_records)],
    'Follow_Up_Date': [fake.date_between(start_date='today', end_date='+30d') if fake.random_element(elements=('Yes', 'No')) == 'Yes' else 'N/A' for _ in range(num_records)],
    'Customer_ID': [fake.random_int(min=3001, max=9999) for _ in range(num_records)],
    'Agent_ID': [fake.random_int(min=1001, max=9999) for _ in range(num_records)]
}
interaction_df = pd.DataFrame(interaction_data)

# Generating manager notes data
summary_data = {
    'Agent_ID': [fake.random_int(min=1001, max=9999) for _ in range(num_records)],
    'Agent_Name': [f"{fake.first_name()} {fake.last_name()}" for _ in range(num_records)],
    'Manager_Notes': [fake.sentence(nb_words=6) for _ in range(num_records)]
}
summary_df = pd.DataFrame(summary_data)

# Writing to Excel with multiple sheets
excel_path = 'expanded_agent_manager_interaction_tracking.xlsx'
with pd.ExcelWriter(excel_path) as writer:
    agent_df.to_excel(writer, sheet_name='Agents', index=False)
    interaction_df.to_excel(writer, sheet_name='Interactions', index=False)
    summary_df.to_excel(writer, sheet_name='Manager_Notes', index=False)

# Writing to a CSV file
csv_path = 'expanded_agent_manager_interaction_tracking.csv'
interaction_df.to_csv(csv_path, index=False)

print(f"Excel file saved to {excel_path}")
print(f"CSV file saved to {csv_path}")
