'''
69. Prime Join Delay
easy
data analyst
data scientist
Question
What is the average number of days it takes for a user to enroll in prime after creating an account?
Ignore users who never joined prime.
Round your answer to 2 decimal places.

DataFrame Schema
Input: amazon_users

+-------------------+------------+
| Column Name       | Data Type  |
+-------------------+------------+
| user_id           | int64      |
| first_name        | object     |
| last_name         | object     |
| email             | object     |
| country           | object     |
| joined_dt         | object     |  # timestamp
| prime_member      | int64      |  # 1 if prime, 0 if not
| prime_joined_dt   | object     |  # timestamp, null if not prime
+-------------------+------------+
Expected Output:

+-------------------+---------+
| Column Name       | Type    |
+-------------------+---------+
| avg_days_to_join  | float64 |
+-------------------+---------+'''

import pandas as pd

# Display dataframe
prime_members_df= amazon_users[amazon_users['prime_member']==1].reset_index(drop=True)
prime_members_df['joined_dt']=pd.to_datetime(prime_members_df['joined_dt'])
prime_members_df['prime_joined_dt']=pd.to_datetime(prime_members_df['prime_joined_dt'])
prime_members_df['avg_days_to_join']=(prime_members_df['prime_joined_dt']-prime_members_df['joined_dt']).dt.days

avg_days_to_join=round(prime_members_df['avg_days_to_join'].mean(),2)


result= pd.DataFrame({'avg_days_to_join':[avg_days_to_join]})

result

