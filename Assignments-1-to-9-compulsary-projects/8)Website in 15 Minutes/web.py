import streamlit as st
import pandas as pd
import random

# Streamlit page config
st.set_page_config(page_title="Employee Data Generator", layout="wide")
st.title("💼 Employee CSV File Generator")

# Sample data
names = ["Ahmed", "Sara", "Usman", "Ayesha", "Bilal", "Nimra", "Farhan", "Mehwish", "Kashif", "Hina"]
departments = ["HR", "Finance", "Engineering", "Marketing", "Sales", "IT"]

# User input: number of employees
num_employees = st.slider("Select number of employees to generate", 5, 100, 20)

# Generate employee data
employees = []
for i in range(1, num_employees + 1):
    employee = {
        "ID": i,
        "Name": random.choice(names),
        "Age": random.randint(22, 60),
        "Department": random.choice(departments),
        "Salary (USD)": random.randint(30000, 120000),
        "Experience (Years)": random.randint(1, 35)
    }
    employees.append(employee)

# Convert to DataFrame
df = pd.DataFrame(employees)

# Filter by Department
selected_departments = st.multiselect("Filter by Department", options=departments, default=departments)
filtered_df = df[df["Department"].isin(selected_departments)]

# Display data
st.subheader("📋 Generated Employee Data")
st.dataframe(filtered_df)

# Download CSV
csv_file = filtered_df.to_csv(index=False).encode('utf-8')
st.download_button("⬇️ Download CSV", csv_file, "employee_data.csv", "text/csv")

# Success message
st.success("✅ Employee records generated successfully!")
