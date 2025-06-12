'''
114. Top Facebook Posters
easy
data analyst
data scientist
Question
Find the user(s) with the most posts on Facebook and count how many of each post type they made.
If there is a tie, return all top users.
Order the result by creator (ascending) and post_type (ascending).

DataFrame Schema
Input: fb_posts

+-----------+-----------+---------------------+-----------+
| post_id   | user_id   | creation_date       | post_type |
+-----------+-----------+---------------------+-----------+
| bigint    | bigint    | timestamp           | varchar   |
+-----------+-----------+---------------------+-----------+
Expected Output:

+---------+-----------+-------------+
| creator | post_type | total_posts |
+---------+-----------+-------------+
| int64   | object    | int64       |
+---------+-----------+-------------+'''

import pandas as pd

def top_posters(fb_posts: pd.DataFrame) -> pd.DataFrame:
  
  #let us filter total posts per user
    user_post_cnt =         fb_posts.groupby('user_id')['post_id'].count().reset_index(name='total_posts')
    max_posts= user_post_cnt['total_posts'].max()
  #filter fb_posts for the max posts
  #in max posts we get the total_posts that have max count need the users
    top_users= user_post_cnt[user_post_cnt['total_posts']==max_posts]['user_id']
    result = (
      
      fb_posts[fb_posts['user_id'].isin(top_users)]
      .groupby(['user_id','post_type'])
      .size()
      .reset_index(name='total_posts')
      .rename(columns={'user_id': 'creator'})
      .sort_values(['creator','post_type'])
      .reset_index(drop=True)
    
  )
    return result
    # Write your solution here.
    