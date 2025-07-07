'''
3. Monetized Videos
easy
data scientist
data analyst
Question
Return the email address of creators who posted monetized videos with at least 5-minute duration (≥ 300 seconds) more than once. Order the result in ascending order of email.

DataFrame Schemas
Input: youtube_users

+-------------+------------+
| Column Name | Data Type |
+-------------+------------+
| email       | object     |
| country     | object     |
| user_id     | int64      |
| username    | object     |
| last_name   | object     |
| signup_dt   | object     |
| first_name  | object     |
+-------------+------------+
Input: youtube_videos

+----------------+------------+
| Column Name    | Data Type |
+----------------+------------+
| channel        | object     |
| user_id        | int64      |
| category       | object     |
| video_id       | int64      |
| video_title    | object     |
| duration_sec   | int64      |
| is_monetized   | int64      |
| published_at   | object     |
+----------------+------------+
Expected Output:

+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| email       | object |
+-------------+--------+'''

import pandas as pd

# Display the DataFrame for inspection
#youtube_users.head()

df = youtube_videos[(youtube_videos['is_monetized'] == 1) & (youtube_videos['duration_sec'] >= 300)]

#find count more than once of these people

ans = df.groupby('user_id')['video_id'].count().reset_index(name="cnt")

ans=ans[ans['cnt']>1]
res= pd.merge(ans,youtube_users, on='user_id', how='inner')[['email']].sort_values(by='email', ascending=True)

res = res.drop_duplicates()

res

