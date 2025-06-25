'''
64. Ride Refund Rate
easy
data analyst
data scientist
Question
Find the ride refund rate of all Uber trips: out of all rides, how many are refunded?

Be careful how you count: there could be more than one reason a rider cancels.
Round your answer to 2 decimals.
DataFrame Schemas
Input: uber_fct_trips

+-------------------+-----------+
| Column Name       | Data Type |
+-------------------+-----------+
| ride_id           | int64     |
| rider_id          | int64     |
| driver_id         | int64     |
| pickup_loc        | object    |
| dropoff_loc       | object    |
| city              | object    |
| ride_type         | object    |
| vehicle_type      | object    |
| destination_type  | object    |
| num_of_passengers | int64     |
| surcharge         | float64   |
| base_fare         | float64   |
| trip_miles        | float64   |
| trip_request_at   | object    |
| service_match_time| object    |
+-------------------+-----------+
Input: uber_refunds

+--------------+--------------+
| Column Name  | Data Type    |
+--------------+--------------+
| trip_id      | int64        |
| refund_reason| object       |
+--------------+--------------+
Expected Output:

+-------------------+---------+
| Column Name       | Type    |
+-------------------+---------+
| ride_refund_rate  | float64 |
+-------------------+---------+'''

import pandas as pd

# Display DataFrame
res= uber_refunds.groupby('trip_id').size().reset_index(name='refund reasons')
refund_cnt= res.shape[0]

total_rides = uber_fct_trips['ride_id'].nunique()

ride_refund_rate=round((refund_cnt/total_rides)*100,2)

result=pd.DataFrame({'ride_refund_rate':[ride_refund_rate]})

result