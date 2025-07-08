'''
118. Users With 3+ Companies
medium
data scientist
data analyst
data engineer
Question
Which users have worked at more than two distinct companies? (Some users may have returned to the same company multiple times.)
Return the email addresses of these users in ascending order.

DataFrame Schemas
Input: linkedin_emp_history

+-------------+------------+
| Column Name | Data Type  |
+-------------+------------+
| user_id     | int64      |
| employment  | object     |
| start_date  | object     |
| end_date    | object     |
+-------------+------------+
Input: linkedin_users

+-------------+------------+
| Column Name | Data Type  |
+-------------+------------+
| user_id     | int64      |
| first_name  | object     |
| last_name   | object     |
| email       | object     |
| country     | object     |
| joined_dt   | object     |
| account_type| object     |
+-------------+------------+
Expected Output:

+---------------------+--------+
| Column Name         | Type   |
+---------------------+--------+
| email               | object |
+---------------------+--------+'''

import pandas as pd

# Display DataFrame
user_count=linkedin_emp_history.groupby('user_id')['employment'].nunique().reset_index(name='count')

filtered_more_than_2 = user_count[user_count['count']>2]

merged = pd.merge(filtered_more_than_2,linkedin_users, on='user_id', how='left' )

merged[['email']].sort_values(by='email')