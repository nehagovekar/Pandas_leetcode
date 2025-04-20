'''
Given the schema shown below, write a solution to fetch the 3 lowest-earning employees, including their IDs, names and salaries.

employees                  
+---------------+---------+
| id            | int     |
| first_name    | varchar |
| last_name     | varchar |
| salary        | int     |
| department_id | int     |
+---------------+---------+
Your query should output a result in the following format:

id | first_name | last_name | salary 
----+------------+-----------+--------
int | varchar    | varchar   | int
'''
import pandas as pd

def lowest_earning_employees(employees: pd.DataFrame) -> pd.DataFrame:
    employees= employees[['id','first_name','last_name','salary']].sort_values('salary').head(3)
    return employees
    # your code goes here

# debug your code below
employees = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'first_name': ['John', 'Ava', 'Cailin', 'Mike', 'Ian', 'John'],
    'last_name': ['Smith', 'Muffinson', 'Ninson', 'Peterson', 'Peterson', 'Mills'],
    'salary': [20000, 10000, 30000, 20000, 80000, 50000],
    'department_id': [1, 5, 2, 2, 2, 3]
})

result = lowest_earning_employees(employees)
print(result.to_string(index=False))