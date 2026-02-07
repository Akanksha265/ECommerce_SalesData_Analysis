import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector


db = mysql.connector.connect(host = "localhost",
                            user = "root",
                            password = "mysql",
                            database = "ecommerce")

cur = db.cursor()
#List all unique cities where customers are located.
print("-------QUERY 1------")
query = """
SELECT DISTINCT customer_city
FROM customers
"""

cur.execute(query)
data = cur.fetchall()

df = pd.DataFrame(data, columns=["customer_city"])
print(df.head())
print("-------QUERY 2------")
#Count the number of orders placed in 2017.
query = """ select count(order_id) from orders where year(order_purchase_timestamp) = 2017 """

cur.execute(query)

data = cur.fetchall()

print("Total orders placed in 2017 are:", data[0][0])

print("-------QUERY 3------")
#Find the total sales per category.
query = """ select upper(products.product_category) category, 
round(sum(payments.payment_value),2) sales
from products join order_items 
on products.product_id = order_items.product_id
join payments 
on payments.order_id = order_items.order_id
group by category
"""

cur.execute(query)

data = cur.fetchall()

df = pd.DataFrame(data, columns = ["Category", "Sales"])
print(df)

print("-------QUERY 4------")
#Calculate the percentage of orders that were paid in installments.
query = """ select ((sum(case when payment_installments >= 1 then 1
else 0 end))/count(*))*100 from payments
"""

cur.execute(query)

data = cur.fetchall()

print("The percentage of orders that were paid in installments is", data[0][0])


print("-------QUERY 5------")
#Count the number of customers from each state.
query = """ select customer_state ,count(customer_id)
from customers group by customer_state
"""

cur.execute(query)

data = cur.fetchall()
df = pd.DataFrame(data, columns = ["state", "customer_count" ])
print(df)
df = df.sort_values(by = "customer_count", ascending= False)

plt.figure(figsize = (8,3))
plt.bar(df["state"], df["customer_count"])
plt.xticks(rotation = 90)
plt.xlabel("states")
plt.ylabel("customer_count")
plt.title("Count of Customers by States")
plt.show()

