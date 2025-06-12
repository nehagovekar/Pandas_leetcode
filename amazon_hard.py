'''
Question
For each country, what percentage of users enrolled in Prime within 5 days (inclusive) after joining Amazon?
Round to 2 decimal places. Order the output by country in ascending order.

DataFrame Schema
Input: amazon_users

+------------------+----------------+
| Column Name      | Data Type      |
+------------------+----------------+
| user_id          | int64          |
| first_name       | object         |
| last_name        | object         |
| email            | object         |
| country          | object         |
| joined_dt        | datetime64[ns] |
| prime_member     | int64          |
| prime_joined_dt  | datetime64[ns] |
+------------------+----------------+
Expected Output:

+----------+------------+
| country  | percentage |
+----------+------------+
| object   | float64    |
+----------+------------+
'''import pandas as pd
import numpy as np

def joined_prime_within_5_days(amazon_users: pd.DataFrame) -> pd.DataFrame:
    # Ensure datetime columns are in datetime format
    amazon_users['joined_dt'] = pd.to_datetime(amazon_users['joined_dt'])
    amazon_users['prime_joined_dt'] = pd.to_datetime(amazon_users['prime_joined_dt'])

    # Calculate days between joined_dt and prime_joined_dt
    days_diff = (amazon_users['prime_joined_dt'] - amazon_users['joined_dt']).dt.days

    # Create the flag: 1 if joined within 5 days, else 0
    amazon_users['joined_prime_within_5_days'] = np.where(days_diff <= 5, 1, 0)
    # If prime_joined_dt is NaT, days_diff is NaN, so the condition is False and gets 0

    # Group by country and calculate percentage
    result = (
        amazon_users
        .groupby('country', as_index=False)
        .agg(percentage=('joined_prime_within_5_days', lambda x: round(x.mean() * 100, 2)))
        .sort_values('country')
        .reset_index(drop=True)
    )

    # Reorder columns as per expected output
    result = result[['country', 'percentage']]
    return result