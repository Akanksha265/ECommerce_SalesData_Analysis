
📊 E-Commerce Data Analytics Project
🚀 Project Overview

This project is an end-to-end Data Analytics case study built using a Kaggle E-Commerce dataset.

It demonstrates strong proficiency in:

✅ SQL (Basic, Intermediate & Advanced Queries)

✅ Window Functions & Analytical Queries

✅ Data Analysis using Python

✅ Data Visualization

✅ Database Connectivity with MySQL

✅ Version Control using Git & GitHub

The project analyzes customer behavior, sales performance, retention, and revenue growth using real-world structured data.

🛠 Tech Stack

Database:

MySQL

Languages & Libraries:

Python

SQL

Pandas

NumPy

Matplotlib

Seaborn

Development Environment:

VS Code

Version Control:

Git & GitHub

📂 Dataset

Source: Kaggle E-Commerce Dataset

Data includes:

Customers

Orders

Payments

Order timestamps

Transaction values

The dataset simulates a real-world online marketplace system.

📈 Project Structure
📦 E-Commerce-Data-Analytics
 ┣ 📜 SQL Queries (15 total)
 ┣ 📜 Python Analysis Script
 ┣ 📊 Visualizations
 ┗ 📄 README.md

🧠 SQL Analysis (15 Queries)

The project includes:

🔹 Basic Level Queries

Total number of orders

Total revenue

Monthly sales

Customer count

Average order value

🔹 Intermediate Queries

Revenue by year/month

Customer purchase frequency

Product/category performance

Ranking customers by spend

🔹 Advanced Queries (Window Functions Used)

Some of the key advanced analyses include:

📌 1️⃣ Moving Average of Customer Order Value

Used SQL Window Function:

AVG(payment) OVER(
  PARTITION BY customer_id 
  ORDER BY order_purchase_timestamp
  ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
)


📊 Insight: Helps identify spending patterns and customer purchasing trends over time.

📌 2️⃣ Cumulative Monthly Sales
SUM(payment) OVER(
  ORDER BY years, months
)


📊 Insight: Tracks revenue growth progression over time.

📌 3️⃣ Year-over-Year (YoY) Growth Rate
LAG(payment, 1) OVER(ORDER BY years)


📊 Insight: Measures annual business growth percentage.

📌 4️⃣ Customer Retention Rate (Within 6 Months)

Used:

CTEs

Date filtering

Aggregation logic

📊 Insight: Measures customer loyalty and repeat behavior.

📌 5️⃣ Top 3 Customers Per Year

Used:

DENSE_RANK() OVER(
  PARTITION BY year
  ORDER BY SUM(payment) DESC
)


📊 Insight: Identifies high-value customers annually.

🐍 Python Data Analysis & Visualization

After executing SQL queries, results were:

Imported into Pandas DataFrames

Cleaned and processed using NumPy & Pandas

Visualized using Matplotlib & Seaborn

Example Visualization:

📊 Bar plots of top customers by yearly spending

📈 Trend analysis of cumulative sales

📉 Growth analysis charts

🔍 Key Business Insights

📈 Revenue shows steady year-over-year growth

💰 A small percentage of customers contribute a large portion of revenue

🔁 Customer retention within 6 months impacts long-term profitability

📊 Moving averages help detect spending consistency

💡 Skills Demonstrated

✔ Advanced SQL (CTEs, Window Functions, Ranking Functions)
✔ Business KPI Calculation
✔ Data Cleaning & Transformation
✔ Time-Series Analysis
✔ Analytical Thinking
✔ Data Visualization & Storytelling
✔ Database Connectivity using mysql.connector
✔ End-to-End Project Deployment

🎯 Why This Project Matters

This project simulates real-world business analytics tasks such as:

Revenue tracking

Customer segmentation

Retention analysis

Performance reporting

KPI dashboard preparation

It reflects practical skills required for:

Data Analyst

Business Intelligence Analyst

SQL Developer

Junior Data Scientist

▶ How to Run the Project

Clone the repository

git clone https://github.com/your-username/your-repo-name.git


Install required libraries

pip install pandas numpy matplotlib seaborn mysql-connector-python


Import dataset into MySQL

Update database credentials in the script

Run the Python file

📌 Future Improvements

Build an interactive dashboard using Power BI / Tableau

Deploy as a Streamlit web app

Add automated reporting

Add customer segmentation using clustering

Convert into a full BI case study portfolio

👨‍💻 Author

Akanksha Kumari
Aspiring Data Analyst | SQL | Python | Data Visualization

GitHub: https://github.com/Akanksha265

LinkedIn:https://www.linkedin.com/in/akanksha-kumari-1a0222289
