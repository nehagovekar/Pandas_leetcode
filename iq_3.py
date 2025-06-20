'''
83. Luxury Property Count
easy
data analyst
data scientist
Question
Find the total number of luxury properties listed on Airbnb.

DataFrame Schema
Input: airbnb_dim_property

+---------------------+-------------+
| Column Name         | Data Type   |
+---------------------+-------------+
| property_id         | int64       |
| owner_id            | int64       |
| property_type       | object      |
| property_quality    | object      |
| no_bedrooms         | int64       |
| no_bathrooms        | float64     |
| total_sqft          | object      |
| nightly_price_range | object      |
| parking_spots       | int64       |
| location_town       | object      |
| location_country    | object      |
| first_listed_on     | object      |
+---------------------+-------------+
Expected Output:

+------------------------+--------+
| Column Name            | Type   |
+------------------------+--------+
| total_luxury_properties| int64  |
+------------------------+--------+'''

import pandas as pd

# Display the DataFrame for inspection
total_luxury_properties=airbnb_dim_property[airbnb_dim_property['property_type']=='Luxury'].shape[0]

result= pd.DataFrame({'total_luxury_properties':[total_luxury_properties]})

result