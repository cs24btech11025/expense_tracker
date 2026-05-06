# 💸 Personal Expense Tracker

A Python project that automatically tracks my UPI payments and analyzes my spending habits.

---

## What it does

- Automatically detects PhonePe transactions from SMS messages
- Uses **Google Gemini AI** to guess the expense category (Food, Transport, Shopping, etc.)
- Saves every transaction to a CSV file
- Analyzes spending with charts and summaries using a Jupyter Notebook

---

## How it works

1. I make a payment on PhonePe
2. My bank sends an SMS
3. MacroDroid (Android app) catches the SMS and sends it to my laptop
4. A Python server reads the SMS, extracts the amount and merchant name
5. Gemini AI figures out the category automatically
6. The transaction is saved to `expenses.csv`
7. The Jupyter Notebook reads the CSV and shows charts

---

## Project files

| File | What it does |
|---|---|
| `sms_server.py` | Receives SMS, calls Gemini AI, saves to CSV |
| `expense_analysis.ipynb` | Loads CSV and shows charts and insights |
| `expenses.csv` | Stores all transactions |
| `.env` | Stores API key (not uploaded for security) |

---

## Charts included

- Bar chart — spending by category
- Pie chart — expense breakdown
- Monthly spending summary

---

## Tools used

- Python
- Pandas — data cleaning and analysis
- Matplotlib — charts
- Flask — local server to receive SMS
- Google Gemini API — AI category guessing
- MacroDroid — Android automation
- Jupyter Notebook

---

## How to run it

**1. Clone the repo**
```
git clone https://github.com/yourusername/expense-tracker
cd expense-tracker
```

**2. Install dependencies**
```
pip install flask pandas matplotlib requests python-dotenv
```

**3. Add your Gemini API key**

Create a `.env` file:
```
GEMINI_API_KEY=your_key_here
```

**4. Start the server**
```
python sms_server.py
```

**5. Set up MacroDroid** on your Android phone to forward PhonePe SMS to `http://your-laptop-ip:5000/sms`

**6. Open the notebook**
```
jupyter notebook expense_analysis.ipynb
```

---

## What I learned

- Reading and cleaning data with Pandas
- Building charts with Matplotlib
- Creating a REST API with Flask
- Using an AI API (Gemini) for smart categorization
- Automating data collection from SMS
- Storing secrets safely with `.env` files

---

*This is part of my Data Science learning journey. Built as a Stage 1 project.*
