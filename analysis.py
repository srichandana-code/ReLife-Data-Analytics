import pandas as pd

# Load cleaned File 1
df1 = pd.read_csv("ReLife_Cleaned_File1.csv")

# Convert date
df1["Order_Date"] = pd.to_datetime(df1["Order_Date"])

print("Total Orders:", len(df1))

print("\nReturn Status:")
print(df1["Return_Status"].value_counts())

print("\nReturn Reasons:")
print(df1["Return_Reason"].value_counts())

print("\nProduct Categories:")
print(df1["Product_Category"].value_counts())
# ReLife KPI calculations

total_orders = len(df1)

returned_orders = (df1["Return_Status"] == "Returned").sum()

return_rate = (returned_orders / total_orders) * 100

total_return_cost = df1.loc[
    df1["Return_Status"] == "Returned", "Return_Cost"
].sum()

total_profit_loss = df1["Profit_Loss"].sum()

print("\n===== RELIFE KPIs =====")
print("Total Orders:", total_orders)
print("Returned Orders:", returned_orders)
print("Return Rate: {:.2f}%".format(return_rate))
print("Total Return Cost: {:.2f}".format(total_return_cost))
print("Total Profit/Loss: {:.2f}".format(total_profit_loss))
