Construction Project Dashboard

This is a comprehensive data-driven dashboard built for real-world construction project tracking and management. The system is designed using Python, SQLite, and Streamlit to monitor costs, clients, material inventory, and worker details efficiently. It reflects how a mid-size construction firm can use data engineering to make operations transparent and scalable.

Project Objective

To develop a full-fledged project monitoring tool for construction businesses that consolidates all financial, material, and workforce data into a clean, visual, and interactive dashboard. The goal is to make operational insights accessible and actionable, even without technical expertise.

Technologies Used

Technology	Description
Python (Pandas)	Data processing, cleaning, and transformation
SQLite	Lightweight, file-based database for structured storage
Streamlit	Web-based interface for dashboard and data display
CSV	Used as the initial data input for ETL
Core Features

1. Project Management
Site tracking by location, area (sqft), and construction status
Captures detailed cost breakdowns (land, material, labor)
Calculates total spend, sale price, and net profit
2. Material Inventory
Tracks all materials used per site (e.g., cement, sand, tiles)
Calculates quantity used vs. available
Supports finishing materials (e.g., lights, fans, taps)
3. Worker Management
Stores worker name, role, assigned site, and salary
Role categories include mason, carpenter, plumber, painter, etc.
Tracks attendance and supports salary reporting
4. Client and Ownership
Manages client info and their respective construction projects
Logs ownership transfers over time
Enables filtering and analysis by client
5. Interactive Dashboard (Streamlit)
Displays real-time summaries: total spend, total sales, and profit
Enables filtering by area, status, site, client
Presents tabular and aggregated views using Streamlit widgets
Project Directory Structure

ConstructionProject/
│
├── data/
│   ├── sites.csv
│   ├── clients.csv
│   ├── materials.csv
│   ├── workers.csv
│   └── attendance.csv
│
├── db/
│   └── construction.db          # SQLite database
│
├── scripts/
│   └── etl_loader.py            # Loads CSV data into database
│
├── app/
│   └── dashboard.py             # Streamlit application
│
└── README.md
How It Works

Extract: Data is initially sourced from structured CSV files for each category (projects, clients, materials, workers, etc.)
Transform: Python (via Pandas) processes this data, cleaning inconsistencies, filling nulls, and converting types as needed.
Load: The data is inserted into a normalized SQLite database using a script (etl_loader.py).
Display: The dashboard reads from the SQLite DB and uses Streamlit to show:
Detailed site info
Summary metrics
Filtered search results
Business Applications

Track real-time progress across 3000+ construction projects
Monitor profit margins per site and area
Prevent overspending on materials
Understand client history and ownership flow
Identify areas with the most construction activity
Data Integrity & Security

All ETL operations are handled programmatically (not through manual entry)
Data is validated before loading to prevent schema mismatch
Streamlit app is read-only for display; DB write access is restricted to scripts
Scalability

SQLite is sufficient for thousands of records; supports future migration to PostgreSQL
Modular design makes it easy to upgrade dashboard components
Can be containerized or moved to cloud-hosted environments for enterprise use
Future Enhancements

Add role-based access for clients, workers, and admins
Include image support per site (site photos)
Enable monthly PDF report export for each project
Live integration with vendor material APIs
