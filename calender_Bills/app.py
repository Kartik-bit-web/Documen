from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def hel():
    return render_template('myindex.html')

@app.route('/event')
def event():
    return render_template('createEvent.html')
