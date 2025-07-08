'''
117. Monetized to Non-monetized
medium
data analyst
data scientist
Question
Which creators published a monetized video 5 minutes or longer followed by a non-monetized video that was also 5 minutes or longer?

Round intermediary calculations to 2 decimals.
Output the email of creators, sorted in alphabetical order.
DataFrame Schemas
Input: youtube_videos

+--------------+--------------+
| Column Name  | Data Type    |
+--------------+--------------+
| video_id     | int64        |
| is_monetized | bool         |
| video_title  | object       |
| channel      | object       |
| user_id      | int64        |
| category     | object       |
| published_at | object       |
| duration_sec | int64        |
+--------------+--------------+
Input: youtube_users

+-----------+--------------+
| Column    | Data Type    |
+-----------+--------------+
| user_id   | int64        |
| username  | object       |
| first_name| object       |
| last_name | object       |
| email     | object       |
| country   | object       |
| signup_dt | object       |
+-----------+--------------+
Expected Output:

+----------------------+
| email                |
+----------------------+
| BLee3@hotmail.com    |
| MKim7@hotmail.com    |
| WGuzman3@yahoo.com   |
+----------------------+'''

import pandas as pd
# Display dataframes
youtube_videos= youtube_videos[youtube_videos['duration_sec']>=300]
monetized =youtube_videos[youtube_videos['is_monetized']==1][['user_id','published_at']]
non_monetized= youtube_videos[youtube_videos['is_monetized']==0][['user_id','published_at']]

merged= pd.merge(monetized,non_monetized, on ='user_id', suffixes=
                ['_mon','_nonmon'] )
user_ids= merged[merged['published_at_mon'] < merged['published_at_nonmon']][['user_id']]

result = youtube_users[youtube_users['user_id'].isin(user_ids['user_id'])][['email']].drop_duplicates().sort_values('email').reset_index(drop=True)

result