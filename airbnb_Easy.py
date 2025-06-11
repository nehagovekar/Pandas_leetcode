'''
120. Bon Air Properties
easy
data analyst
data scientist
Question
Count the total number of Airbnb properties located in Bon Air.

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

+-------------------+--------+
| Column Name       | Type   |
+-------------------+--------+
| total_properties  | int64  |
+-------------------+--------+
'''
import pandas as pd

def count_properties_in_bon_air(airbnb_dim_property: pd.DataFrame) -> pd.DataFrame:
  ans=airbnb_dim_property[airbnb_dim_property['location_town']=='Bon Air'].shape[0]
  return pd.DataFrame([{'total_properties': ans}])
    