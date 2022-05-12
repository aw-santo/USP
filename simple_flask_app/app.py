from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def root(name=None):
    r = getQuote()
    return render_template('index.html', quote=r[0]['q'], author=r[0]['a'])

def getQuote():
    r = requests.get('https://zenquotes.io/api/today')
    r = r.json()
    return r

if __name__ == "__main__":
    app.run(debug=True, port=8000)