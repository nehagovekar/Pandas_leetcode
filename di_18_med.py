'''
119. Monthly Reported Posts
medium
data analyst
data scientist
Question
For each reported_reason, find the number of posts reported each month in 2022.

Return the result sorted by reported_reason (ascending) and by month (chronological order).
The mon_yr column should be formatted as YYYY-Mon (e.g., 2022-Mar).
Duplicates are allowed (count all reports).
DataFrame Schema
Input: fb_reported_posts

+------------------+-------------+
| Column Name      | Data Type   |
+------------------+-------------+
| reported_by      | int64       |
| post_id          | int64       |
| posted_by        | int64       |
| reported_reason  | object      |
| risk_rating      | object      |
| reported_at      | object      |  # date or datetime string
| is_reviewed      | int64       |
| is_removed       | int64       |
+------------------+-------------+
Expected Output:

+-----------+------------------+----------------+
| mon_yr    | reported_reason  | posts_reported |
+-----------+------------------+----------------+
| object    | object           | int64          |
+-----------+------------------+----------------+'''

import pandas as pd

# Display DataFrame
import pandas as pd

fb_reported_posts['reported_at']= pd.to_datetime(fb_reported_posts['reported_at'])
# Filter for 2022
df_2022 = fb_reported_posts[fb_reported_posts['reported_at'].dt.year == 2022].copy()

df_2022['reported_month'] = df_2022['reported_at'].dt.month

df_2022['mon_yr']= pd.to_datetime(df_2022['reported_at']).dt.strftime('%Y-%b')

df_2022 = df_2022.groupby(['mon_yr', 'reported_reason','reported_month'])['post_id'].size().reset_index(name='posts_reported')

df_2022= df_2022.sort_values(by=['reported_reason', 'reported_month'], ascending=[True, True])
df_2022[['mon_yr','reported_reason','posts_reported']]


                             
