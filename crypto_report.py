import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheets API Setup
SHEET_NAME = "Crypto Live Tracker"
SCOPES = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
CREDS_FILE = "tracker-api-452816-2010e309d03f.json"

# Load Google Sheets API Credentials
creds = ServiceAccountCredentials.from_json_keyfile_name(CREDS_FILE, SCOPES)
client = gspread.authorize(creds)

# Open the Google Sheet
sheet = client.open(SHEET_NAME).sheet1

# Load Crypto Data from Excel
df = pd.read_excel("crypto_data.xlsx")

# Debugging: Print column names
print("Column Names:", df.columns)

# Ensure correct column names
price_change_col = "24h Price Change (%)"  # Column verified from print output

# Generate Summary Report
summary = {
    "Top 5 Market Cap": ", ".join(  # Convert to comma-separated string
        [f"{row['Symbol']} (${row['Market Cap']:,.2f})" for row in df.nlargest(5, "Market Cap")[["Symbol", "Market Cap"]].to_dict(orient="records")]
    ),
    "Average Price": f"${df['Price (USD)'].mean():,.2f}",  # Format as string
    "Highest 24h % Change": f"{df.loc[df[price_change_col].idxmax(), 'Symbol']} ({df[price_change_col].max():.2f}%)",  
    "Lowest 24h % Change": f"{df.loc[df[price_change_col].idxmin(), 'Symbol']} ({df[price_change_col].min():.2f}%)",
}

# Convert Summary to DataFrame for Google Sheets
summary_df = pd.DataFrame(summary.items(), columns=["Metric", "Value"])

# Upload Data to Google Sheets
sheet.clear()
sheet.update([summary_df.columns.tolist()] + summary_df.values.tolist())

print("Google Sheets updated successfully!")
