'''
121. Growth Type Counts
easy
data scientist
data analyst
data engineer
Question
Clean the growth_type column so that only Low, Med, and High are present (fixing any typos or variants).
Return the total count for each growth type, sorted by total in descending order.

DataFrame Schema
Input: messy_data

+----------------+------------+
| Column Name    | Data Type  |
+----------------+------------+
| post_id        | int64      |
| growth_type    | object     |
| is_live        | float64    |
| creation_region| object     |
| etl_date       | object     |
+----------------+------------+
Expected Output:

+---------------------+--------+
| growth_typecleaned  | total  |
+---------------------+--------+
| Low                 | 31     |
| High                | 13     |
| Med                 | 6      |
+---------------------+--------+
'''
import pandas as pd

def cleaned_growth_report(messy_data: pd.DataFrame) -> pd.DataFrame:
    # Clean up the growth_type column
    def clean_growth_type(gt):
        if gt == 'low' or gt == 'Loww':
            return 'Low'
        elif gt == 'Hgh':
            return 'High'
        else:
            return gt

    messy_data['growth_typecleaned'] = messy_data['growth_type'].apply(clean_growth_type)

    # Filter to only Low, Med, High
    valid_types = ['Low', 'Med', 'High']
    filtered = messy_data[messy_data['growth_typecleaned'].isin(valid_types)]

    # Group and count
    result = (
        filtered
        .groupby('growth_typecleaned')
        .size()
        .reset_index(name='total')
        .sort_values('total', ascending=False)
        .reset_index(drop=True)
    )

    # Reorder columns as per expected output
    result = result[['growth_typecleaned', 'total']]
    return result