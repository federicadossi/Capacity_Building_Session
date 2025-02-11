# This script contains the first example to present at the capacity building session, it models ghjsmhfshfshfshfshfshfshfsmnjhfmfh


# %%  import packages

import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Import the CSV
df = pd.read_csv("sample_data.csv")

# Step 2: Modify the data
df = df.T  # Transpose (switch columns with rows)
df.drop(df.columns[1], axis=1, inplace=True)  # Delete second column (previously a row)

# Step 3: Perform a calculation (e.g., sum numeric values if applicable)
if "Salary" in df.index:
    df.loc["Bonus"] = df.loc["Salary"].astype(float) * 0.1  # Example: 10% salary bonus

# Step 4: Save the modified CSV
modified_csv_filename = "modified_sample_data.csv"
df.to_csv(modified_csv_filename)

# Step 5: Plot the new data (e.g., Salary vs. Age)
df_numeric = df.T  # Transpose back for plotting
if "Age" in df_numeric.columns and "Salary" in df_numeric.columns:
    plt.figure(figsize=(6, 4))
    plt.scatter(df_numeric["Age"], df_numeric["Salary"], color="blue", label="Salary")
    plt.xlabel("Age")
    plt.ylabel("Salary")
    plt.title("Salary by Age")
    plt.legend()
    plt.grid(True)
    plt.show()

# Save the plot
plt.savefig("salary_by_age_plot.png")
