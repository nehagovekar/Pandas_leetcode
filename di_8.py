'''
58. Single Post Count
easy
data analyst
data scientist
Question
Count how many job posts on LinkedIn have been posted only once. Return the total number of such unique posts.

DataFrame Schema
Input: linkedin_job_posts

+------------+------------+
| Column Name| Data Type  |
+------------+------------+
| event_id   | bigint     |
| post_id    | bigint     |
| post_date  | date       |
| company_id | bigint     |
| company    | varchar    |
+------------+------------+
Expected Output:

+------------------+--------+
| Column Name      | Type   |
+------------------+--------+
| num_unique_post  | int64  |
+------------------+--------+'''

import pandas as pd

# Display DataFrame
df= linkedin_job_posts.groupby('post_id')['event_id'].size().reset_index(name='num_unique_post')
ans=df[df['num_unique_post']==1].shape[0]
result=pd.DataFrame({'num_unique_post':[ans]})
result