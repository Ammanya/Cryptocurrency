🚀 Crypto Live Tracker - Tracker
This project tracks live cryptocurrency data, updates an Excel sheet, performs data analysis, and syncs with Google Sheets.

📂 Project Structure
bash
Copy
Edit
📦 Tracker  
├── 📜 crypto_analysis.py      # Analyzes cryptocurrency data  
├── 📜 crypto_data.xlsx        # Excel file storing fetched data  
├── 📜 crypto_dox.py           # (File purpose not specified)  
├── 📄 Crypto_Report.docx      # Final report with analysis  
├── 📜 crypto_report.py        # Generates report and updates Google Sheets  
├── 📜 tracker.py              # Main script for fetching data  

🛠️ Setup & Installation
Clone the repository:


git clone <https://github.com/Ammanya/Cryptocurrency.git>


cd tracker

🛠️Install dependencies:

pip install -r requirements.txt

🛠️Run the tracker script to fetch crypto data:


python tracker.py

🛠️Analyze the fetched data:


python crypto_analysis.py

🛠️Generate reports and update Google Sheets:


python crypto_report.py

📊 Features
✔️ Fetches live cryptocurrency data from CoinGecko
✔️ Updates data in an Excel file (crypto_data.xlsx) every 5 minutes
✔️ Analyzes top 5 cryptocurrencies based on market cap
✔️ Generates a report (Crypto_Report.docx)
✔️ Syncs data with Google Sheets
