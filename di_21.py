'''
2. Days Since First Session
medium
data scientist
Question
Calculate the number of days since a users first session. Assume today is 2022-05-26. Return answers sorted by days desc and user_id asc.

DataFrame Schemas
Input: ig_user_sessions

+-------------+-----------------+
| Column Name | Data Type       |
+-------------+-----------------+
| user_id     | int64           |
| session_ts  | datetime64[ns]  |
+-------------+-----------------+
Expected Output:

+---------------------------+------------------+
| Column Name               | Data Type        |
+---------------------------+------------------+
| user_id                   | int64            |
| first_session             | datetime64[ns]   |
| days_since_first_session  | int64            |
+---------------------------+------------------+'''

import pandas as pd

# Display the DataFrame for inspection
first_session_filtered=  ig_user_sessions.groupby('user_id')['session_ts'].min().reset_index(name='first_session')

first_session_filtered['first_session']=pd.to_datetime(first_session_filtered['first_session'])

first_session_filtered['days_since_first_session']= (pd.to_datetime('2022-05-26')-first_session_filtered['first_session']).dt.days


first_session_filtered.sort_values(by=['days_since_first_session','user_id'], ascending=[False, True])