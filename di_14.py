'''
41. Top Product by Category
easy
data analyst
data scientist
Question
For each product category, find the most expensive product.

Return the following columns, sorted alphabetically by category:

category
product_name
price
Only return one product per category.

DataFrame Schema
Input: amazon_products

+--------------+------------+
| Column Name  | Data Type  |
+--------------+------------+
| product_id   | int64      |
| product_name | object     |
| category     | object     |
| price        | float64    |
| rating       | int64      |
| published_at | object     |
+--------------+------------+
Expected Output:

+--------------+--------------+--------+
| category     | product_name | price  |
+--------------+--------------+--------+
| ...          | ...          | ...    |
+--------------+--------------+--------+'''

index= amazon_products.groupby('category')['price'].idxmax()

result = amazon_products.loc[index, ['category','product_name','price' ]]

result.sort_values(by='category', ascending=False)