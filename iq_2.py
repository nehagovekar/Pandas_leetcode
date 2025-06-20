'''
87. CTR by Website Type
easy
data analyst
data scientist
Question
You are on the Digital Marketing team at Google. Find the click-through-rate (CTR) for each website type.

CTR = # of Clicked / # of Viewed.
Use the event_type column (not conversion).
Round to 2 decimal places.
Output should be sorted by type ascending.
DataFrame Schemas
Input: google_search_activity

+---------------+------------+
| Column Name   | Data Type  |
+---------------+------------+
| event_id      | int64      |
| session_id    | int64      |
| user_id       | int64      |
| website_id    | int64      |
| creation_dt   | object     |
| advertisement | int64      |
| event_type    | object     |  # 'clicked' or 'viewed'
+---------------+------------+
Input: google_search_websites

+-------------+------------+
| Column Name | Data Type  |
+-------------+------------+
| website_id  | int64      |
| url         | object     |
| type        | object     |
+-------------+------------+
Expected Output:

+-------------+-----------------+
| Column Name | Type            |
+-------------+-----------------+
| type        | object          |
| conversion_rate | float64     |
+-------------+-----------------+'''

import pandas as pd
# Display dataframes
google_search_activity.head()
google_search_websites.head()

df_merge = pd.merge(google_search_activity[['website_id','event_type']],
                   google_search_websites[['website_id','type']], on='website_id',how='inner')

grouped = df_merge.groupby('type').event_type.value_counts().unstack(fill_value=0)

grouped['conversion_rate']= ((grouped['clicked'])/(grouped['viewed'])).round(2)

res=grouped.reset_index()[['type','conversion_rate']].sort_values('type').reset_index(drop=True)
res