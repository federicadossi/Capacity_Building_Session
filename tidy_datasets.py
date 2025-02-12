# %%
# Tidy data follows a structured format that makes it easier to manipulate, analyze, and visualize.
# The concept of tidy data was introduced by Hadley Wickham, a statistician and data scientist.
#
# Key Principles of Tidy Data:
# 1. Each variable is in its own column → Every column represents a single variable.
# 2. Each observation is in its own row → Every row represents a single observation or data point.
# 3. Each value is in its own cell → Each cell contains a single value.
# 4. Each type of observational unit forms a table → Data should be organized so that related observations belong in the same table.

import pandas as pd
import matplotlib.pyplot as plt

# Creating the untidy DataFrame
data_untidy = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 22],
    "Gender": ["Female", "Male", "Male"],
    "Test1": [85, 80, 88],
    "Test2": [90, 75, 85]
}

df_untidy = pd.DataFrame(data_untidy)

# Why is this untidy?
# • The test scores (Test1 and Test2) should be in one column under a "Score" variable.
# • Another column should specify which test the score belongs to.

'''Why is it important to work on tidy datasets?
Python operations, such as visualization, filtering, and statistical analysis libraries, work better with data in a
tidy format. - 
Tidy data makes filtering, transforming, summarizing, and visualizing information easier'''

# Convert to a Tidy Format using melt()
df_tidy = df_untidy.melt(
    id_vars=["Name", "Age", "Gender"],  # These columns remain unchanged
    var_name="Test",   # Column names (Test1, Test2) are converted into a single 'Test' column
    value_name="Score"  # The values from Test1 and Test2 are stored in a new 'Score' column
)

