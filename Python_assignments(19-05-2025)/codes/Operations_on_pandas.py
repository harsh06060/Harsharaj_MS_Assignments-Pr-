# pandas is a Python library for working with data in a table-like structure called a DataFrame (like an Excel sheet).

# Basic Pandas Operations: Harsh's Study Adventure
# Simple pandas operations to create, view, select, add, filter, calculate, and save!

# Import pandas
import pandas as pd

name = "Harsh"

# 1. Create a DataFrame
data = {"Subject": ["Math", "Science", "English"], "Score": [90, 85, 88]}
df = pd.DataFrame(data)

# 2. View the DataFrame
print(f"\n{name}'s study scores:")
print(df)

# 3. Select a column
scores = df["Score"]
print(f"\n{name}'s scores only:")
print(scores)

# 4. Add a new row
new_row = pd.DataFrame({"Subject": ["History"], "Score": [92]})
df = pd.concat([df, new_row])
print(f"\n{name} added a new subject:")
print(df)

# 5. Filter rows (scores >= 90)
high_scores = df[df["Score"] >= 90]
print(f"\n{name}'s high scores (>=90):")
print(high_scores)

# 6. Calculate average score
average_score = df["Score"].mean()
print(f"\n{name}'s average score: {average_score}")

# 7. Save to Excel
excel_file = "harsh_study.xlsx"
df.to_excel(excel_file, index=False)
print(f"\n{name} saved the scores to {excel_file}!")