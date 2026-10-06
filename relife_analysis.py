import pandas as pd

# Load the cleaned dataset
df = pd.read_csv("ReLife_Cleaned_File1.csv")

# Display first 5 rows
print(df.head())

# Display number of rows and columns
print("Shape:", df.shape)

# Display column names
print("\nColumns:")
print(df.columns)

# Display data types
print("\nData Types:")
print(df.dtypes)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Statistical summary
print("\nStatistical Summary:")
print(df.describe())
# Order and Sales Analysis

print("\n--- Orders by Product Category ---")
print(df["Product_Category"].value_counts())

print("\n--- Sales by Product Category ---")
sales_by_category = df.groupby("Product_Category")["Order_Value"].sum()
print(sales_by_category.sort_values(ascending=False))

print("\n--- Average Order Value by Category ---")
avg_order_category = df.groupby("Product_Category")["Order_Value"].mean()
print(avg_order_category.sort_values(ascending=False))