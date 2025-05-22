# Appending to an Excel Sheet: Harsh's Data Adventure
# Using pandas to append a new row to an existing Excel sheet!

# Import pandas
import pandas as pd

name = "Harsh"
new_score = 95

# File path for the Excel file
excel_file = "append_excel.xlsx"

# New data to append 
new_data = {"Name": name, "Score": new_score}

try:
    # Try to read the existing Excel file
    df = pd.read_excel(excel_file)
    print(f"{name} found an existing Excel sheet:")
    print(df)
except FileNotFoundError:
    # If file doesn't exist, create a new DataFrame
    df = pd.DataFrame(columns=["Name", "Score"])
    print(f"{name} created a new Excel sheet!")

# Convert new data to a DataFrame
new_row = pd.DataFrame([new_data])

# Append new row to existing DataFrame
updated_df = pd.concat([df, new_row], ignore_index=True)

# Write the updated DataFrame back to the Excel file
updated_df.to_excel(excel_file, index=False)

# Read and display the updated Excel sheet
final_df = pd.read_excel(excel_file)
print(f"\n{name}'s updated Excel sheet after appending:")
print(final_df)
