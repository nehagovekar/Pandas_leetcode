'''
99. CTR by Ad Type
easy
data analyst
data scientist
Question
Calculate the click-through rate (CTR) for advertisement and non-advertisement link types.

CTR = (# of Clicked) / (# of Viewed)
Round the result to 2 decimal places.
Order the output by the advertisement column in ascending order.
DataFrame Schema
Input: google_search_activity

+----------------+------------+
| Column Name    | Data Type  |
+----------------+------------+
| event_id       | int64      |
| session_id     | int64      |
| user_id        | int64      |
| website_id     | int64      |
| creation_dt    | object     |
| advertisement  | int64      |
| event_type     | object     |  # 'clicked' or 'viewed'
+----------------+------------+
Expected Output:

+----------------+-----------------+
| advertisement  | conversion_rate |
+----------------+-----------------+
| int64          | float64         |
+----------------+-----------------+'''

import pandas as pd
# Display dataframe

agg = google_search_activity.groupby('advertisement')['event_type'].value_counts().unstack(fill_value=0)
agg['conversion_rate']=(agg.get('clicked',0)/agg.get('viewed',0)).round(2)

result = agg.reset_index()[['advertisement','conversion_rate']].sort_values('advertisement')
result