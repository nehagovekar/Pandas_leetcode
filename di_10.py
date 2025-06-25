'''
55. Avg Tenure Company
easy
data analyst
data scientist
Question
Calculate the average tenure (in months) for each company based on employee history.
Return the company name and average tenure, rounded to 1 decimal place, sorted by company name in ascending order.

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
| company     | avg_tenure |
+-------------+------------+
| object      | float64    |
+-------------+------------+'''

import pandas as pd

# Display the DataFrame for inspection
linkedin_emp_history['start_date']= pd.to_datetime(linkedin_emp_history['start_date'])

linkedin_emp_history['end_date']= pd.to_datetime(linkedin_emp_history['end_date'])

linkedin_emp_history['months'] = (
    (linkedin_emp_history['end_date'].dt.year - linkedin_emp_history['start_date'].dt.year) * 12 +
    (linkedin_emp_history['end_date'].dt.month - linkedin_emp_history['start_date'].dt.month)
)

ans=linkedin_emp_history.groupby('employment')['months'].mean().reset_index(name='avg_tenure').round(1).sort_values(by='employment')

ans.rename(columns={'employment': 'company'}, inplace=True)


ans