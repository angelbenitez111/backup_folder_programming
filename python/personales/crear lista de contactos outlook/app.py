# import pandas as pandas
"""
import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)
"""

"""
# Create your own labels:
import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)
"""
"""
import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)
"""

"""
# Create a Series using only data from "day1" and "day2":
import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories, index = ["day1", "day2"])

print(myvar)

"""

"""
Check the number of maximum returned rows:

import pandas as pd

print(pd.options.display.max_rows)

"""

"""
Get a quick overview by printing the first 10 rows of the DataFrame:

import pandas as pd

df = pd.read_csv('data.csv')

print(df.head(10))
"""

"""
# Print the last 5 rows of the DataFrame:
print(df.tail()) 
"""

"""
# Print information about the data:

print(df.info()) 
"""

"""
Return a new Data Frame with no empty cells:

import pandas as pd

df = pd.read_csv('data.csv')

new_df = df.dropna()

print(new_df.to_string())

"""
# Load a comma separated file (CSV file) into a DataFrame:

import pandas as pd

df = pd.read_csv('temp.CSV')

print(df)