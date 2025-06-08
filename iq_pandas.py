'''
Over 100 Dollars
0:00:00

21
Question
Solution
My submissions
User submissions
You’re given two dataframes: transactions and products.

The transactions dataframe contains transaction ids, product ids, and the total amount of each product sold.

The products dataframe contains product ids and prices.

Write a function to return a dataframe containing every transaction with a total value of over $100. Include the total value of the transaction as a new column in the dataframe.

Example:

Input:

import pandas as pd

transactions = {"transaction_id" : [1, 2, 3, 4, 5], "product_id" : [101, 102, 103, 104, 105], "amount" : [3, 5, 8, 3, 2]}

products = {"product_id" : [101, 102, 103, 104, 105], "price" : [20.00, 21.00, 15.00, 16.00, 52.00]}

df_transactions = pd.DataFrame(transactions)

df_products = pd.DataFrame(products)
Output:

transaction_id	product_id	amount	total_value
2	102	5	105.00
3	103	8	120.00
5	105	2	104.00
'''

import pandas as pd

def transactions_over_100(df_transactions: pd.DataFrame, df_products: pd.DataFrame):
    merged_df = pd.merge(df_transactions,df_products, on='product_id', how='inner' )
    merged_df['total_value']=merged_df['amount']*merged_df['price']
    result = merged_df[merged_df['total_value']>100]
    return result[['transaction_id','product_id','amount','total_value']]

    