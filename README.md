# 📈 Tesla Stock Alert System

This Python project tracks **Tesla (TSLA)** stock prices using real-time data and sends an **email alert** when there's a significant change in the stock's closing price. It also includes the **top 3 news headlines** about Tesla using NewsAPI.

---

## 🔔 Features

- 📉 Fetches daily closing prices of TSLA using Alpha Vantage API  
- 📰 Retrieves top 3 Tesla-related news articles using NewsAPI  
- 📬 Sends a well-formatted stock update and news digest via email  
- 🔐 Secure API key and email password handling via environment variables  

---

## 🛠️ Tech Stack

- **Python 3**
- **Alpha Vantage API** – Stock data
- **NewsAPI** – News headlines
- **SMTP (Gmail)** – Email delivery
- `requests`, `smtplib`, `email.message`, `os`
---

## 📦 Project Structure
```bash
tesla-stock-alert/
├── main.py # Main Python script
├── requirements.txt # List of dependencies
├── .gitignore # Files to ignore in Git
├── README.md # Project documentation
└── .env (not included) # Environment variables (not to be shared)
```
---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/tesla-stock-alert.git
cd tesla-stock-alert
```

### 2. Install required packages
```bash
pip install -r requirements.txt
```

### 3. Create environment variables
Create a .env file or set these in your system:
```bash
STOCK_API_KEY=your_alpha_vantage_api_key
NEWS_API_KEY=your_newsapi_key
PASSWORD=your_gmail_app_password
```
### 4. Run the script
```bash
python main.py
```
✅ Make sure to set up an App Password for Gmail if two-factor authentication is enabled.

---
## 📖 Sample Output (Email Body)
```bash
TSLA: 🔺3.5%

Headline: Tesla announces new AI partnership.
Brief: Tesla has partnered with a major tech company to develop autonomous driving chips.

Headline: Tesla Q2 earnings beat expectations.
Brief: Tesla’s earnings for the second quarter exceeded Wall Street forecasts...

Headline: Musk tweets about next Gigafactory.
Brief: Elon Musk hints at plans for a new Gigafactory in India...
```
---

Built with ❤️ by Anushka Chaudhari
