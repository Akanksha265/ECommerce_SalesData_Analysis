
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

🛠️ Tech Stack
🗄️ Database

🐬 MySQL

💻 Languages & Libraries

🐍 Python

🗄️ SQL

🐼 Pandas

🔢 NumPy

📈 Matplotlib

🎨 Seaborn

🖥️ Development Environment

💻 VS Code

🔧 Version Control

🔄 Git

🌍 GitHub

📂 Dataset
📥 Source

📊 Kaggle E-Commerce Dataset

📦 Data Includes

👥 Customers

🛒 Orders

💳 Payments

⏳ Order Timestamps

💰 Transaction Values

The dataset simulates a real-world online marketplace system.

📈 Project Structure
📦 E-Commerce-Data-Analytics
 ┣ 📜 SQL Queries (15 total)
 ┣ 📜 Python Analysis Script
 ┣ 📊 Visualizations
 ┗ 📄 README.md
 
📊 SQL Analysis (15 Queries)

The project includes structured SQL queries categorized into three levels:

🔹 Basic Level Queries

📦 Total number of orders

💰 Total revenue

📅 Monthly sales analysis

👥 Customer count

🧮 Average order value

🔹 Intermediate Queries

📆 Revenue by year/month

🔁 Customer purchase frequency

🛍️ Product/category performance

🏆 Ranking customers by total spend

🔹 Advanced Queries (Window Functions & CTEs)
📌 1️⃣ Moving Average of Customer Order Value

Window Function Used:

AVG(payment) OVER(
  PARTITION BY customer_id 
  ORDER BY order_purchase_timestamp
  ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
)


📊 Insight:
Helps identify customer spending trends and smooth fluctuations in purchasing behavior over time.

📌 2️⃣ Cumulative Monthly Sales

Window Function Used:

SUM(payment) OVER(
  ORDER BY years, months
)


📊 Insight:
Tracks revenue growth progression and long-term sales performance.

📌 3️⃣ Year-over-Year (YoY) Growth Rate

Window Function Used:

LAG(payment, 1) OVER(ORDER BY years)


📊 Insight:
Measures annual business growth and compares financial performance year by year.

📌 4️⃣ Customer Retention Rate (Within 6 Months)

Techniques Used:

🧱 CTEs (Common Table Expressions)

📅 Date filtering logic

🧮 Aggregation functions

📊 Insight:
Evaluates customer loyalty and repeat purchase behavior within a defined time window.

📌 5️⃣ Top 3 Customers Per Year

Window Function Used:

DENSE_RANK() OVER(
  PARTITION BY year
  ORDER BY SUM(payment) DESC
)


📊 Insight:
Identifies high-value customers annually and helps in strategic customer targeting.

Here is your fully polished, professional, GitHub-ready formatted version with clean structure, strong wording, and consistent emojis — ready to paste into your README 👇

🐍 Python Data Analysis & Visualization

After executing SQL queries, the results were:

📥 Imported into Pandas DataFrames

🧹 Cleaned and transformed using NumPy & Pandas

📊 Visualized using Matplotlib & Seaborn

📈 Example Visualizations

📊 Bar plots of top customers by yearly spending

📈 Trend analysis of cumulative sales

📉 Year-over-Year growth charts

🔍 Key Business Insights

📈 Revenue shows steady Year-over-Year growth

💰 A small percentage of customers contribute a large portion of total revenue (Pareto effect)

🔁 Customer retention within 6 months significantly impacts long-term profitability

📊 Moving averages help identify consistent and high-value customers

💡 Skills Demonstrated

✔ Advanced SQL (CTEs, Window Functions, Ranking Functions)

✔ Business KPI Calculation

✔ Data Cleaning & Transformation

✔ Time-Series Analysis

✔ Analytical Thinking & Problem Solving

✔ Data Visualization & Storytelling

✔ Database Connectivity using mysql.connector

✔ End-to-End Data Analytics Workflow

🎯 Why This Project Matters

This project simulates real-world business analytics scenarios such as:

📈 Revenue tracking

👥 Customer segmentation

🔁 Retention analysis

📊 Performance reporting

📑 KPI dashboard preparation

It reflects practical skills required for roles like:

📊 Data Analyst

📈 Business Intelligence Analyst

🗄️ SQL Developer

🤖 Junior Data Scientist

▶ How to Run the Project


1️⃣ Clone the Repository
git clone https://github.com/Akanksha265/ECommerce_SalesData_Analysis.git


2️⃣ Install Required Libraries
pip install pandas numpy matplotlib seaborn mysql-connector-python

3️⃣ Setup Database


Import the dataset into MySQL

Update database credentials in the Python script

4️⃣ Run the Project
python your_script_name.py

📌 Future Improvements

📊 Build an interactive dashboard using Power BI / Tableau

🌐 Deploy as a Streamlit web application

📑 Add automated reporting features

🤖 Implement customer segmentation using clustering

📘 Expand into a complete Business Intelligence case study portfolio

👨‍💻 Author

Akanksha Kumari


Aspiring Data Analyst | SQL | Python | Data Visualization

🔗 GitHub: https://github.com/Akanksha265

LinkedIn:https://www.linkedin.com/in/akanksha-kumari-1a0222289
