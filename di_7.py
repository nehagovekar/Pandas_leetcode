'''
66. Max Parking Spots
easy
data analyst
data scientist
Question
Find the highest number of parking spots across all properties.
Return a DataFrame with a single column: max_parking_spots.

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

+-------------------+--------+
| Column Name       | Type   |
+-------------------+--------+
| max_parking_spots | int64  |
+-------------------+--------+'''

import pandas as pd

# Display the DataFrame for inspection
max_parking_spots= airbnb_dim_property['parking_spots'].max()
result= pd.DataFrame({'max_parking_spots':[max_parking_spots]})
result