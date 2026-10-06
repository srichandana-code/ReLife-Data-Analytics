import pandas as pd

# Load File 1
df1 = pd.read_csv("returns_sustainability_dataset.csv")

print("Shape:", df1.shape)
print("\nFirst 5 rows:")
print(df1.head())

print("\nColumns:")
print(df1.columns.tolist())
print("\nMissing values:")
print(df1.isnull().sum())

print("\nDuplicate rows:")
print(df1.duplicated().sum())
print("\nData types:")
print(df1.dtypes)
df1["Order_Date"] = pd.to_datetime(df1["Order_Date"], errors="coerce")

print("\nOrder_Date type:", df1["Order_Date"].dtype)
print("Invalid dates:", df1["Order_Date"].isnull().sum())
print("\nFinal validation:")
print("Rows:", df1.shape[0])
print("Columns:", df1.shape[1])
print("Missing values:", df1.isnull().sum().sum())
print("Duplicate rows:", df1.duplicated().sum())
print("Invalid dates:", df1["Order_Date"].isnull().sum())

# Save cleaned File 1
df1.to_csv("ReLife_Cleaned_File1.csv", index=False)

print("\nFile 1 cleaned and saved successfully!")