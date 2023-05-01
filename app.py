from flask import Flask, request, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from typing import List
import requests
import json



app = Flask(__name__)

app.config["SECRET_KEY"] = 'dolladollabills'
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

def validate_inputs(amount: str, starting_currency: str, converting_currency: str, codes: List[str]) -> bool:
    if not amount.isdigit():
        flash('Amount must be an integer')
        return False
    if starting_currency not in codes:
        flash('Starting currency code not found')
        return False
    if converting_currency not in codes:
        flash('Converting currency code not found')
        return False
    return True

@app.route('/get-currencies')
def get_currencies():
     url = "https://api.exchangerate.host/symbols"
     response = requests.get(url)
     data = json.loads(response.text)
     symbols = data["symbols"]
     codes = list(symbols.keys())
     return codes

@app.route('/get_descriptions')
def get_descriptions():
     url = "https://api.exchangerate.host/symbols"
     response = requests.get(url)
     data = json.loads(response.text)
     descriptions = {key: value['description'] for key, value in data['symbols'].items()}
     return descriptions
    
@app.route('/convert-currencies', methods=["GET"])
def convert_currencies():
    starting_currency = request.args.get('starting_currency')
    amount = request.args.get('amount')
    converting_currency = request.args.get('converting_currency')
    descriptions = get_descriptions()
    codes = get_currencies()
    if validate_inputs(amount, starting_currency, converting_currency, codes):
        url = f'https://api-us.exchangerate.host/convert?from={starting_currency}&to={converting_currency}&amount={amount}'
        response = requests.get(url)
        init_result = response.json()
        result = init_result['result']
        converted_amount = round(result, 2)
        converting_description = descriptions[converting_currency]
        return render_template('result.html', converted_amount=converted_amount, converting_description=converting_description)
    else:
     return redirect('/')
    
@app.route('/')
def home_page():
    codes = get_currencies()
    return render_template("index.html", codes=codes)
