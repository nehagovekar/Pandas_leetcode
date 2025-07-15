'''
115. Average Days Between Videos
medium
data analyst
data scientist
Question
For each creator, calculate the average number of days between their video uploads.

Output the creator's username and their average days between videos.
If a creator has no videos or only one video, impute the average as 0.
Round the average to 2 decimal places.
Order the results alphabetically by username.
Limit the output to first 10 rows.
DataFrame Schemas
Input: youtube_users

+-------------+------------+
| Column Name | Data Type  |
+-------------+------------+
| user_id     | int64      |
| username    | object     |
| first_name  | object     |
| last_name   | object     |
| email       | object     |
| country     | object     |
| signup_dt   | object     |
+-------------+------------+
Input: youtube_videos

+--------------+------------+
| Column Name  | Data Type  |
+--------------+------------+
| video_id     | int64      |
| is_monetized | int64      |
| video_title  | object     |
| channel      | object     |
| user_id      | int64      |
| category     | object     |
| published_at | object     |
| duration_sec | int64      |
+--------------+------------+
Expected Output:

+----------------+-----------------------------+
| Column Name    | Type                        |
+----------------+-----------------------------+
| username       | object                      |
| avg_days_between_two_videos | float64        |
+----------------+-----------------------------+
'''

import pandas as pd

#merge two tables
df = pd.merge(youtube_users,youtube_videos, how='left', on='user_id' )
#convert date to datetime
df['signup_dt'] = pd.to_datetime(df['signup_dt'])
df['published_at'] = pd.to_datetime(df['published_at'])

#sort the dates according to each user
df = df.sort_values(['email', 'published_at'])

#NEW THING LEARNT: SHIFT IS LIKE LAG USE GROUP BY FOR PARTITION BY AND ORDER BY IN PREV STEP TO SORT
df['prev_signup_dt'] = df.groupby('email')['published_at'].shift(1)
df['datediff']= ( df['published_at'] - df['prev_signup_dt']).dt.days

#group by average
df= (
  df.groupby('username')['datediff']
  .mean()
  .round(2)
  .reset_index(name='avg_days_between_two_videos')
  .sort_values(by='username', ascending=True)
  .rename(columns={'datediff':'avg_days_between_two_videos'})
)
df['avg_days_between_two_videos']= df['avg_days_between_two_videos'].fillna(0)
df.head(10)

