'''
39. Full View Rate
easy
data analyst
data scientist
Question
Find the percentage of views that were watched to completion.
Return the result rounded to 2 decimals.

DataFrame Schema
Input: tiktok_fct_views

+-----------------------+------------+
| Column Name           | Data Type  |
+-----------------------+------------+
| viewer_id             | int64      |
| creator_id            | int64      |
| view_ts               | object     |
| device_type           | object     |
| viewed_to_completion  | int64      |
| sound_id              | int64      |
| has_promotion         | int64      |
+-----------------------+------------+
Expected Output:

+----------------+---------+
| full_view_rate | float64 |
+----------------+---------+'''

import pandas as pd

# Display DataFrame
tiktok_fct_views.head()

complete_view = tiktok_fct_views[tiktok_fct_views['viewed_to_completion']==1].shape[0]

total_view = tiktok_fct_views.shape[0]

full_view_rate=((complete_view/total_view)*100)

res=pd.DataFrame({('full_view_rate'):[full_view_rate]})
res

