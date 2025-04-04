import pandas as pd
import mysql.connector

# Establish connection to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    port=3306,
    password="",  # Your MySQL password
    database="optimising_power_bi"
)

cursor = conn.cursor()

# Create the table (if not exists)
cursor.execute("""
CREATE TABLE IF NOT EXISTS pizza (
    pizza_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    pizza_name_id VARCHAR(50),
    quantity INT,
    order_date DATE,
    order_time TIME,
    unit_price DECIMAL(10,2),
    total_price DECIMAL(10,2),
    pizza_size VARCHAR(10),
    pizza_category VARCHAR(100),
    pizza_ingredients VARCHAR(255),
    pizza_name VARCHAR(200)
)
""")
conn.commit()

# Load CSV file into a DataFrame
csv_file = "pizza.csv"
df = pd.read_csv(csv_file)

# Ensure correct datetime format
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce').dt.date
df['order_time'] = pd.to_datetime(df['order_time'], errors='coerce').dt.time

# Define the SQL query for inserting data (without pizza_id)
query = """
INSERT INTO pizza (order_id, pizza_name_id, quantity, order_date, order_time, unit_price, total_price, pizza_size, pizza_category, pizza_ingredients, pizza_name)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# Convert DataFrame to list of tuples
data = [tuple(row) for row in df.itertuples(index=False, name=None)]

# Execute batch insert
cursor.executemany(query, data)

# Commit changes
conn.commit()

print(cursor.rowcount, "records inserted successfully.")

# Close the connection
cursor.close()
conn.close()
