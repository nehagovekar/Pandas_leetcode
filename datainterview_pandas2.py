'''
106. Permanently Banned Users
easy
data scientist
data analyst
data engineer
Question
Find the usernames of all users who are permanently banned. Return the usernames in ascending order.

DataFrame Schemas
Input: fb_users_all

+-------------+------------+
| Column Name | Data Type  |
+-------------+------------+
| user_id     | int64      |
| username    | object     |
| first_name  | object     |
| last_name   | object     |
| email       | object     |
| country     | object     |
| signup_date | object     |
| is_verified | bool       |
+-------------+------------+
Input: banned_users

+---------------+------------+
| Column Name   | Data Type  |
+---------------+------------+
| user_id       | int64      |
| banned_reason | object     |
| banned_on     | object     |
| is_temporary  | int64      |
+---------------+------------+
Expected Output:

+----------+--------+
| username | object |
+----------+--------+'''
import pandas as pd

# Display DataFrame
#fb_users_all.head()
permanently_banned= banned_users[banned_users['is_temporary']==0]
permanently_banned
merged=pd.merge(fb_users_all,permanently_banned, on='user_id', how='right')

merged['username']