'''
Table: Person

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| personId    | int     |
| lastName    | varchar |
| firstName   | varchar |
+-------------+---------+
personId is the primary key (column with unique values) for this table.
This table contains information about the ID of some persons and their first and last names.
 

Table: Address

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| addressId   | int     |
| personId    | int     |
| city        | varchar |
| state       | varchar |
+-------------+---------+
addressId is the primary key (column with unique values) for this table.
Each row of this table contains information about the city and state of one person with ID = PersonId.
 

Write a solution to report the first name, last name, city, and state of each person in the Person table. If the address of a personId is not present in the Address table, report null instead.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Person table:
+----------+----------+-----------+
| personId | lastName | firstName |
+----------+----------+-----------+
| 1        | Wang     | Allen     |
| 2        | Alice    | Bob       |
+----------+----------+-----------+
Address table:
+-----------+----------+---------------+------------+
| addressId | personId | city          | state      |
+-----------+----------+---------------+------------+
| 1         | 2        | New York City | New York   |
| 2         | 3        | Leetcode      | California |
+-----------+----------+---------------+------------+
Output: 
+-----------+----------+---------------+----------+
| firstName | lastName | city          | state    |
+-----------+----------+---------------+----------+
| Allen     | Wang     | Null          | Null     |
| Bob       | Alice    | New York City | New York |
+-----------+----------+---------------+----------+
Explanation: 
There is no address in the address table for the personId = 1 so we return null in their city and state.
addressId = 1 contains information about the address of personId = 2.'
'''
import pandas as pd # type: ignore

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    ans=pd.merge(person, address, how='left', on='personId')
    return ans[['firstName','lastName', 'city', 'state']]
'''  pd.merge(
    left,                 # First DataFrame
    right,                # Second DataFrame
    how='inner',          # Type of join: 'left', 'right', 'inner', 'outer'
    on=None,              # Column name to join on (if same in both DFs)
    left_on=None,         # Column from left DF to join on
    right_on=None,        # Column from right DF to join on
    left_index=False,     # Use index from left DF instead of column
    right_index=False,    # Use index from right DF instead of column
    sort=False,           # Sort the join keys lexicographically
    suffixes=('_x', '_y'),# Suffixes for overlapping column names
    copy=True,            # Copy data from inputs
    indicator=False,      # Add a column showing merge source
    validate=None         # Check if merge is of specified type
)'''
