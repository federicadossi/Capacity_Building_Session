# %% This script can be used to explain and demonstrate fundamental data handling in Python using pandas and matplotlib.

print ("Let's start!")

# %%  IMPORT PACKAGES: In Python, packages (also called libraries) are collections of pre-written code that allow us to
# perform specific tasks without writing everything from scratch. Without importing these packages,
# Python wouldn’t know how to read a CSV file or create a plot because these are not built-in functions of Python.

import pandas as pd # for modifying, analyzing, and visualizing data
import matplotlib.pyplot as plt # to create visualizations, such as scatter plots or bar charts

# Coding is step-by-step – each action builds on the previous one.

# %% Step 1: Import the CSV
raw_data = pd.read_csv("sample_data.csv")
df = raw_data # When we import data from a CSV file, it is automatically stored as a DataFrame (basically a two
              # dimensional table with index as rows and features as column)
# OBSERVE: By default, when you load a CSV file into a pandas DataFrame, Python automatically assigns numbers (0, 1, 2, …)
# as row indices (uncomment section below to explain this better).

# %% SECTION TO UNDERSTAND THE INDEX
#
# # Load CSV without specifying an index (Default behavior: numerical index is assigned)
# df_default = pd.read_csv("sample_data.csv")
#
# # Load CSV with "Name" as the index
# df_with_index = pd.read_csv("sample_data.csv", index_col="Name")
#
# # Demonstrating the difference between .loc[] and .iloc[]
#
# # Selecting a row using .iloc[] (numerical index) in df_default
# row_by_position_default = df_default.iloc[1]  # Selects the second row (Bob)
# print("Row Selected by .iloc[] (Default Index):")
# print(row_by_position_default.to_string(), "\n")
#
# # Selecting a row using .loc[] (label-based) in df_with_index
# row_by_label_indexed = df_with_index.loc["Bob"]  # Selects the row where Name = "Bob"
# print('Row Selected by .loc["Bob"] (Named Index):')
# print(row_by_label_indexed.to_string(), "\n")
#
# # Selecting a column using .iloc[] (numerical index)
# column_by_position_default = df_default.iloc[:, 1]  # Selects the "Age" column by position
# print("Column Selected by .iloc[:, 1] (Default Index):")
# print(column_by_position_default.to_string(), "\n")
#
# # Selecting a column using .loc[] (label-based)
# column_by_label_indexed = df_with_index.loc[:, "Age"]  # Selects the "Age" column by label
# print('Column Selected by .loc[:, "Age"] (Named Index):')
# print(column_by_label_indexed.to_string(), "\n")

# %% Step 2: Modify the data
df_transposed = df.T  # Transpose (switch columns with rows)

# %%
df_transposed.drop(df_transposed.columns[1], axis=1, inplace=True)  # Delete second column (because Python indexing starts at 0)
                                                                    # inplace=True means apply the change directly to df_transposed
# df_transposed.drop("Department", axis=0, inplace=True)  # todo: uncomment if you want to delete row instead of column

# If we change it to inplace=False, we must store the result in a new variable:
# df_transposed_modified = df_transposed.drop(df_transposed.columns[1], axis=1, inplace=False)

# Define the variable to control inplace behavior
use_inplace = True  # Change to False to use inplace=False

if use_inplace:
    df_transposed.drop(df_transposed.columns[1], axis=1, inplace=True)  # Delete second column in-place
    # df_transposed.drop("Department", axis=0, inplace=True)  # Uncomment to delete row instead of column
else:
    df_transposed = df_transposed.drop(df_transposed.columns[1], axis=1, inplace=False)  # Store result in a new variable
    # df_transposed = df_transposed.drop("Department", axis=0, inplace=False)  # Uncomment to delete row instead of column

# REMINDER: Indentation in Python is crucial because it defines the structure of the code, particularly within control
# structures like if statements, loops, and functions. Indented code belongs to the preceding control structure
# (e.g., if, else, for, while, def).

# %% Understanding how to access subsets

# Access using .loc[]: Use .loc[] when you know the row/column name.
bonus_row = df_transposed.loc["Department"]
print("Accessing using .loc[]:\n", bonus_row, "\n")

# Access using .iloc[]: Use .iloc[] when you want to access by position.
third_row = df_transposed.iloc[2]  # This accesses the third row (index starts at 0)
print("Accessing using .iloc[]:\n", third_row, "\n")

# %% Step 3: Perform a calculation
if "Salary" in df_transposed.index:
    df_transposed.loc["Bonus"] = df_transposed.loc["Salary"].astype(float) * 0.1  # Creates a new row called "Bonus", which contains 10% of the Salary values
    """
    Understanding Data Types !!! MOST COMMON SOURCE OF ERRORS !!!
    - float (Floating-Point Number) – A number with decimals, e.g., 50000.0
    - int (Integer) – A whole number, e.g., 50000
    - str (String) – Text or categorical data, e.g., "HR", "Alice"
    - bool (Boolean) – True/False values
    Why do we convert Salary to float?
      If Salary was stored as a string ("50000"), any mathematical operation will fail.
      By converting it to float, we ensure we can calculate the bonus correctly.
    How do you check what type the data is?
    print(df.dtypes) -> to inspect whole dataset
    0 → object → means it's text (string), non-numeric data
    int64 → means it's an integer number
    float64 → means it's a decimal number (float)
    """
    df_transposed.loc["Bonus"] = df_transposed.loc["Bonus"].apply(lambda x: f"{x:.0f}")  # Format as float with zero
                                                                                         # decimals, applies this formatting
                                                                                         # to every value in the Bonus row

# %% Step 4: Save the modified CSV

# Define the path to save the modified CSV
results_path = r"C:\Users\feder\PyCharmMiscProject\results\final_table.csv"
# Save the modified DataFrame to a CSV file
df_transposed.to_csv(results_path, index=True)

# %% Step 5: Plot the new data (e.g., Salary vs. Age)
# Dropping 'Name' and 'Department' since they are non-numeric
df_numeric = df.drop(columns=["Name", "Department"])

# %% Step 5: Plot the new data

# Plot Salary vs. Age
plt.figure(figsize=(8, 5))
plt.plot(df_numeric["Age"], df_numeric["Salary"], marker='o', linestyle='-', label="Salary vs Age")

# Labels and title
plt.xlabel("Age")  # Age on x-axis
plt.ylabel("Salary")  # Salary on y-axis
plt.title("Salary vs. Age Plot")
plt.legend()
plt.grid()
plt.savefig("salary_by_age_plot.png")

# Define save path
save_path = r"C:\Users\feder\PyCharmMiscProject\results\salary_by_age_plot.png"
# Save before showing the plot
plt.savefig(save_path)
# Show plot
plt.show()

