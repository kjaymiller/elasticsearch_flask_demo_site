import os

from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = os.urandom(16)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['GET', 'POST'])
def search():
    query = request.args.get('query')
    return render_template('results.html')

if __name__ == "__main__":
    app.run(debug=True)