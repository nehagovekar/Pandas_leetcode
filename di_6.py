'''
68. Ad Impressions Count
easy
data analyst
data scientist
Question
Count the total number of impressions each ad received.
Sort the result by ad_impressions (descending) and ad_name (ascending).

DataFrame Schema
Input: ads_actions

+-------------+------------+
| Column Name | Data Type  |
+-------------+------------+
| ad_exp_id   | int64      |
| ad_name     | object     |
| cpc_rate    | object     |
| clicked_ad  | int64      |
+-------------+------------+
Expected Output:

+------------------------+-----------------+
| ad_name                | ad_impressions  |
+------------------------+-----------------+
| Nike Shoe Release      | 13              |
| Spotify Prem           | 11              |
| Charty Inc Trial       | 10              |
| Disney+ Bundle         | 10              |
| Cosmetics Holiday Sale | 6               |
+------------------------+-----------------+'''
import pandas as pd


result=(
  ads_actions
  .groupby('ad_name')
  .size()
  .reset_index(name='ad_impressions')
  .sort_values(by=['ad_impressions','ad_name'], ascending=[False, True])
)
result