'''
'1757. Recyclable and Low Fat Products
Solved
Easy
Topics
Companies
SQL Schema
Pandas Schema
Table: Products

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| low_fats    | enum    |
| recyclable  | enum    |
+-------------+---------+
product_id is the primary key (column with unique values) for this table.
low_fats is an ENUM (category) of type ('Y', 'N') where 'Y' means this product is low fat and 'N' means it is not.
recyclable is an ENUM (category) of types ('Y', 'N') where 'Y' means this product is recyclable and 'N' means it is not.
 

Write a solution to find the ids of products that are both low fat and recyclable.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Products table:
+-------------+----------+------------+
| product_id  | low_fats | recyclable |
+-------------+----------+------------+
| 0           | Y        | N          |
| 1           | Y        | Y          |
| 2           | N        | Y          |
| 3           | Y        | Y          |
| 4           | N        | N          |
+-------------+----------+------------+
Output: 
+-------------+
| product_id  |
+-------------+
| 1           |
| 3           |
+-------------+
Explanation: Only products 1 and 3 are both low fat and recyclable.'
'''
import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:

    df_filtered = products[(products['low_fats']=='Y') & (products['recyclable']=='Y')]
    return df_filtered[['product_id']]

    #mistake 1 corrected: products['low_fats'] == 'Y' → Returns a boolean Series (True/False for each row)
    #basically if there is an if condition --> use ==
    #mistake 2: when to use and/&
    #and is a Python logical operator that works with single boolean values (not Pandas Series).

   # df_filtered= products[products['low_fats']=='Y' & products['recyclable']=='Y']

   #mistake 3:There's still a small mistake in your code due to operator precedence. The bitwise & operator has lower precedence than the comparison ==, so the condition should be properly parenthesized.

