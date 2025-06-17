from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()

# Create Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY')

# Connect Bootstrap to Flask app
Bootstrap5(app)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        print('post received')
    return render_template('index.html')


@app.route('/<string:character>')
def get_quote(character):
    print(character)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
