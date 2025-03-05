import pandas as pd

# Load the Excel file
file_path = "crypto_data.xlsx"
df = pd.read_excel(file_path)

# Ensure correct column names
print("Column Names:", df.columns)

# Top 5 Cryptos by Market Cap
top_5_market_cap = df.nlargest(5, "Market Cap")[["Symbol", "Market Cap"]]

# Average Price Calculation
average_price = df["Price (USD)"].mean()

# Highest & Lowest 24h Price Change
highest_24h_change = df.loc[df["24h Price Change (%)"].idxmax(), ["Symbol", "24h Price Change (%)"]]
lowest_24h_change = df.loc[df["24h Price Change (%)"].idxmin(), ["Symbol", "24h Price Change (%)"]]

# Save analysis results to a new sheet in the same Excel file
with pd.ExcelWriter(file_path, mode="a", if_sheet_exists="replace") as writer:
    top_5_market_cap.to_excel(writer, sheet_name="Top 5 Market Cap", index=False)
    pd.DataFrame({"Metric": ["Average Price"], "Value": [average_price]}).to_excel(writer, sheet_name="Average Price", index=False)
    highest_24h_change.to_frame().T.to_excel(writer, sheet_name="Highest 24h Change", index=False)
    lowest_24h_change.to_frame().T.to_excel(writer, sheet_name="Lowest 24h Change", index=False)

print("Crypto analysis completed successfully! Data saved to 'crypto_data.xlsx'.")
