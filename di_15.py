'''
38. Avg Video Duration
easy
data analyst
data scientist
Question
What is the average video duration (in minutes) of monetized and non-monetized videos among users in UK, Australia, and US?
Output the monetization type and average duration in minutes.
Round duration to 2 decimal points.

DataFrame Schemas
Input: youtube_videos

+--------------+-------------+
| Column Name  | Data Type   |
+--------------+-------------+
| video_id     | int64       |
| is_monetized | int64       |
| video_title  | object      |
| channel      | object      |
| user_id      | int64       |
| category     | object      |
| published_at | object      |
| duration_sec | int64       |
+--------------+-------------+
Input: youtube_users

+-------------+-------------+
| Column Name | Data Type   |
+-------------+-------------+
| user_id     | int64       |
| username    | object      |
| first_name  | object      |
| last_name   | object      |
| email       | object      |
| country     | object      |
| signup_dt   | object      |
+-------------+-------------+
Expected Output:

+--------------+--------------------+
| is_monetized | avg_video_duration |
+--------------+--------------------+
| int64        | float64            |
+--------------+--------------------+'''

import pandas as pd
# Display dataframes
filtered_data= youtube_users[youtube_users['country'].isin(['UK','Australia','US'])][['user_id','country']]

data_needed= pd.merge(filtered_data,youtube_videos, on='user_id', how='inner')
data_needed=data_needed[['is_monetized','duration_sec']]

result = (
    data_needed
    .groupby('is_monetized')['duration_sec']
    .mean()
    .div(60)                    
    .round(2)
    .reset_index(name='avg_video_duration')
)

result