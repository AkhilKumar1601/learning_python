import pandas as pd

data = {
    "Stock": ["HDFC", "TCS", "Infosys", "ICICI", "Reliance", "ITC"],
    "SIP_Amount": [5000, 4000, 4500, 3000, 6000, 3500],
    "Months": [24, 24, 24, 24, 24, 24],
    "Current_Value": [160000, 135000, 142000, 102000, 120000, 98000]
}

df = pd.DataFrame(data)

df["Total_Invested"] = df["SIP_Amount"] * df["Months"]
df["Profit"] = df["Current_Value"] - df["Total_Invested"]
df["Return_%"] = (df["Profit"] / df["Total_Invested"]) * 100

print(df)

total_current_value = df["Current_Value"].sum();
print(total_current_value);
total_profit = df["Profit"].sum();
print(total_profit);

stock_with_highest_return = df.loc[df["Return_%"].idxmax()];
print(stock_with_highest_return);

stock_with_lowest_return = df.loc[df["Return_%"].idxmin()];
print(stock_with_lowest_return);

profitable = df[df["Return_%"] > 0];
print(profitable);

sorted_by_return = df.sort_values(by="Return_%", ascending=False);
print(sorted_by_return);

top_Two = sorted_by_return.head(3);
print(top_Two);