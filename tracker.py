import requests
import pandas as pd
import time
import schedule
import gspread
from google.oauth2.service_account import Credentials

# Google Sheets Setup
SERVICE_ACCOUNT_FILE = "tracker-api-452816-2010e309d03f.json"  # Update with your JSON file name
SPREADSHEET_NAME = "Crypto Live Tracker"

# Authenticate with Google Sheets
SCOPES = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
client = gspread.authorize(creds)
sheet = client.open(SPREADSHEET_NAME).sheet1  # Access first sheet

# CoinGecko API URL
API_URL = "https://api.coingecko.com/api/v3/coins/markets"
PARAMS = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 50,
    "page": 1,
    "sparkline": False
}

def fetch_crypto_data():
    """Fetch live crypto data from CoinGecko API."""
    response = requests.get(API_URL, params=PARAMS)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data:", response.status_code)
        return []

def process_data(data):
    """Process API data into a Pandas DataFrame and list format for Google Sheets."""
    df = pd.DataFrame(data)[
        ['name', 'symbol', 'current_price', 'market_cap', 'total_volume', 'price_change_percentage_24h']]

    # Rename columns
    df.columns = ['Name', 'Symbol', 'Price (USD)', 'Market Cap', '24h Trading Volume', '24h Price Change (%)']

    # Convert DataFrame to list format for Google Sheets
    data_list = [df.columns.tolist()] + df.values.tolist()

    return df, data_list

def update_sheets():
    """Fetch crypto data and update Google Sheets & Excel file."""
    print("\nFetching live data...")
    data = fetch_crypto_data()
    if data:
        df, data_list = process_data(data)

        # Update Google Sheet
        sheet.clear()
        sheet.update("A1", data_list)  # ✅ Correct syntax

        # Save locally as well
        df.to_excel("crypto_data.xlsx", index=False, engine='openpyxl')

        print("\nGoogle Sheet & Excel file updated!")

# Schedule the script to run every 5 minutes
schedule.every(5).minutes.do(update_sheets)

print("Tracker is running... Updating Google Sheets & Excel every 5 minutes.")
update_sheets()  # Run once before scheduling

while True:
    schedule.run_pending()
    time.sleep(1)
