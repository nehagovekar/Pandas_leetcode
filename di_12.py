'''
44. Top Rented Properties
easy
data analyst
data scientist
Question
Find the property_id(s) with the highest total number of nights rented from the table below.
If there are ties, return all such property_ids, sorted in ascending order.

DataFrame Schema
Input: airbnb_fct_rentals

+-------------------+------------+
| Column Name       | Data Type  |
+-------------------+------------+
| user_id           | int64      |
| property_id       | int64      |
| num_of_nights     | int64      |
| price_per_night   | float64    |
| purchased_date    | object     |
+-------------------+------------+
Expected Output:

+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| property_id | int64  |
+-------------+--------+
'''

import pandas as pd

# Display dataframe
res= airbnb_fct_rentals.groupby('property_id')['num_of_nights'].sum().reset_index()

max_nights= res['num_of_nights'].max()

top_rented = res[res['num_of_nights']==max_nights]

top_rented[['property_id']].sort_values('property_id').reset_index(drop=True)


