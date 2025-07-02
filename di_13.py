'''
42. Top 3 Avg Tenure
easy
data analyst
data scientist
Question
Your boss is preparing numbers for a leadership presentation.
Which 3 employers have the longest average tenure in months?
Return exactly 3 rows, rounded to 2 decimals, sorted by tenure descending.

DataFrame Schema
Input: linkedin_emp_history

+-------------+------------+
| Column Name | Data Type  |
+-------------+------------+
| user_id     | int64      |
| employment  | object     |
| start_date  | object     |
| end_date    | object     |
+-------------+------------+
Expected Output:

+-------------+------------+
| employment  | avg_tenure |
+-------------+------------+
| object      | float64    |
+-------------+------------+'''

import pandas as pd

# Display dataframe
linkedin_emp_history['start_date']=pd.to_datetime(linkedin_emp_history['start_date'])
linkedin_emp_history['end_date']=pd.to_datetime(linkedin_emp_history['end_date'])

linkedin_emp_history['months']= ((linkedin_emp_history['end_date'].dt.year - 
linkedin_emp_history['start_date'].dt.year)*12 +  
(linkedin_emp_history['end_date'].dt.month - linkedin_emp_history['start_date'].dt.month))


result= (
  linkedin_emp_history
  .groupby('employment')['months']
  .mean().round(2).reset_index(name='avg_tenure')
  
)
result= result.sort_values('avg_tenure', ascending=False).head(3)

result