'''
116. Full View Rate
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
+----------------+---------+
'''

import pandas as pd

def tiktok_full_view_rate(tiktok_fct_views: pd.DataFrame) -> pd.DataFrame:
  #calculate the full_views
  full_view= (tiktok_fct_views['viewed_to_completion']==1).sum()
  total_views = len(tiktok_fct_views)
  full_view_rate=round(full_view/total_views*100,2)if total_views>0 else 0.0
  return pd.DataFrame({'full_view_rate': [full_view_rate]}) 

