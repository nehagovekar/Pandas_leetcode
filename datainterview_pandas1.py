'''
Question
Find the top 5 largest properties at AirBnB (with total_sqft of 3000+).
Return exactly 5 rows, ordered by property_id ascending. Ignore ties.

DataFrame Schema
Input: airbnb_dim_property

+---------------------+------------+
| Column Name         | Data Type  |
+---------------------+------------+
| property_id         | int64      |
| owner_id            | int64      |
| property_type       | object     |
| property_quality    | object     |
| no_bedrooms         | int64      |
| no_bathrooms        | float64    |
| total_sqft          | object     |
| nightly_price_range | object     |
| parking_spots       | int64      |
| location_town       | object     |
| location_country    | object     |
| first_listed_on     | object     |
+---------------------+------------+
Expected Output:

+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| property_id | int64  |
+-------------+--------+'''
import pandas as pd

# Display dataframe
filtered= airbnb_dim_property[airbnb_dim_property['total_sqft'] == '3000+']
filtered_sorted= filtered.sort_values(by='property_id')

res= filtered_sorted[['property_id']].head(5).reset_index(drop=True)
res
