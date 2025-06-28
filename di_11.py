'''
52. Poll Response Rates
easy
data scientist
data analyst
Question
You are on the community polls DS team at Twitter. For each poll, calculate the percent of 'Yes' responses and the percent of 'No' responses.

Round the final answer to 2 decimals.
Sort the output by poll name in ascending order.
DataFrame Schema
Input: twitter_polls

+------------------------+------------+
| Column Name            | Data Type  |
+------------------------+------------+
| poll_id                | int64      |
| poll_name              | object     |
| user_id                | int64      |
| poll_submisison_date   | object     |
| poll_answer            | object     |
+------------------------+------------+
Expected Output:

+------------------------+----------+----------+
| poll_name              | yes_prcnt| no_prcnt |
+------------------------+----------+----------+
| object                 | float64  | float64  |
+------------------------+----------+----------+'''
import pandas as pd

# Display dataframe
poll_count= (
    twitter_polls
    .groupby('poll_name')
    .agg(
        yes_count = ('poll_answer', lambda x: (x=='Yes').sum()),
        no_count = ('poll_answer', lambda x : (x=='No').sum()),
        total_count = ('poll_answer','count')  
  )
    .reset_index()
)
poll_count['yes_prcnt']= round(100*poll_count['yes_count']/poll_count['total_count'],2)

poll_count['no_prcnt']= round(100*poll_count['no_count']/poll_count['total_count'],2)

poll_count[['poll_name','yes_prcnt','no_prcnt']].sort_values('poll_name').reset_index(drop=True)
