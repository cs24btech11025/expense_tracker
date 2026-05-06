from flask import Flask,request
import pandas as pd
import re
import os
from datetime import datetime
import requests
from dotenv import load_dotenv
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
app=Flask(__name__)
CSV_FILE="expenses.csv"
if not os.path.exists(CSV_FILE):
    df=pd.DataFrame(columns=["date","category","amount","description"])
    df.to_csv(CSV_FILE,index=False)
def parse_sms(sms):
    amount=None
    description="phonepay transaction"
    amount_match=re.search(r'(?:Rs\.?|INR)\s*(\d+(?:\.\d{2})?)',sms,re.IGNORECASE)
    if amount_match:
        amount=float(amount_match.group(1))
    merchant_match=re.search(r'(?:to|at)\s+([A-Za-z0-9 ]+?)(?:\s+on|\s+via|\.|$)',sms,re.IGNORECASE)
    if merchant_match:
        description=merchant_match.group(1).strip()

    return amount,description

def guess_category(description):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"
    
    body = {
        "contents": [{
            "parts": [{
                "text": f"""Categorize this expense into exactly one of these:
Food, Transport, Entertainment, Shopping, Bills, Health, Education, Other.

Merchant: {description}

Reply with only the category name, nothing else."""
            }]
        }]
    }
    response = requests.post(url, json=body)
    result = response.json()
    category = result['candidates'][0]['content']['parts'][0]['text'].strip()
    return category
@app.route('/sms',methods=['POST'])
def receive_sms():
    data=request.json
    sms_text=data.get("sms","")
    print(f"Received SMS: {sms_text}")
    amount,description=parse_sms(sms_text)
    if amount:
        category=guess_category(description)
        new_row={
            "date":datetime.now().strftime("%Y-%m-%d"),
            "category":category,
            "amount":amount,
            "description":description
        }
        df = pd.read_csv(CSV_FILE)
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_csv(CSV_FILE,index=False)
        print(f"Successfully Added: {category} | ₹{amount} | {description}")
        return {'status': 'success', 'added': new_row}, 200
    else:
        print("Could not parse amount from SMS")
        return {'status': 'skipped'}, 200
if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000)