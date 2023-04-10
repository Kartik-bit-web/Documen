from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def hel():
    return render_template('index.html', name=' kartik')

@app.route('/resis')
def resis():
    return render_template('resis.html')

@app.route('/hall')
def hall():
    return render_template('hall.html')

@app.route('/dated')
def dated():
    return render_template('dated.html')

@app.route('/function')
def fun():
    return render_template('fun.html')

@app.route('/booking')
def booking():
    return render_template('booking.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

