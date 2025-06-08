import sqlite3
import pandas as pd

conn = sqlite3.connect("company.db")

# 1. Material usage per site
materials_report = pd.read_sql_query('''
    SELECT site_id, material_name, SUM(quantity_needed) AS total_quantity
    FROM Materials
    GROUP BY site_id, material_name
''', conn)
materials_report.to_csv("report_materials.csv", index=False)

# 2. Total salary per site
salary_report = pd.read_sql_query('''
    SELECT site_id, SUM(salary) AS total_salary
    FROM Workers
    GROUP BY site_id
''', conn)
salary_report.to_csv("report_salary.csv", index=False)

# 3. Ownership report
ownership_report = pd.read_sql_query('''
    SELECT s.site_id, s.location, c.customer_name, o.transfer_date, o.price_paid
    FROM Sites s
    JOIN OwnershipTransfers o ON s.site_id = o.site_id
    JOIN Customers c ON o.customer_id = c.customer_id
''', conn)
ownership_report.to_csv("report_ownership.csv", index=False)

conn.close()

print("✅ All reports saved as CSVs.")
