from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from dotenv import load_dotenv
import os
import requests
import random

LOTR_API = 'https://the-one-api.dev/v2/'

# Load variables from .env file
load_dotenv()

# Create Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY')

# Connect Bootstrap to Flask app
Bootstrap5(app)

characters = {
    'aragorn': '5cd99d4bde30eff6ebccfbe6',
    'gandalf': '5cd99d4bde30eff6ebccfea0',
    'frodo': '5cd99d4bde30eff6ebccfc15'
}


@app.route('/')
def home():
    return render_template('index.html', characters=characters)


@app.route('/quote/<string:character>')
def get_quote(character):
    if character in characters:
        # Call LOTR API
        lotr_url = LOTR_API + 'character/' + characters[character] + '/quote'
        lotr_headers = {
            'Authorization': f'Bearer {os.getenv("LOTR_API_ACCESS_TOKEN")}'
        }
        response = requests.get(url=lotr_url, headers=lotr_headers)
        response.raise_for_status()

        # Extract a random quote from the LOTR API response
        quote_results = response.json()['docs']
        random_quote = random.choice(quote_results)['dialog']

        return render_template(
            'quote.html',
            quote=random_quote,
            character=character
        )
    else:
        # Invalid character
        return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
