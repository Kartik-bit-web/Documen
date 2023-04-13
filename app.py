from flask import Flask, render_template, request, url_for, redirect
from module_us import login_user

app = Flask(__name__)

#Indexing page --------->
@app.route('/')
def hel():
    return render_template('index.html', name='kartik')





#Registration page --------->
@app.route('/register', methods = ['POST', 'GET'])
def resis():
    if request.method == 'POST':
        nam = request.form.get('nam')
        email = request.form.get('email')
        num = request.form.get('num')
        login_user.exe(nam, email, num)
        return redirect('/register')
    else:
        return render_template('resis.html')

@app.route('/logIn', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        emails = request.form.get('email')
        print(emails)
        check = login_user.engine.execute("Select * from info ")
        x = check.fetchall()
        for i in x:
            if i['email'] == emails:
                return redirect('/hall')
        return redirect('/logIn')
    else:
        return render_template('login.html')

@app.route('/admin')
def admin():
    return render_template('/admin/login_as_admin.html')








#Hall page --------->
@app.route('/hall')
def hall():
    return render_template('hall.html')

#Date watching --------->
@app.route('/dated')
def dated():
    return render_template('dated.html')

#Function Organisation page --------->
@app.route('/function')
def fun():
    return render_template('fun.html')

#Booking Details page --------->
@app.route('/booking')
def booking():
    return render_template('booking.html')

#Menus for Functions page --------->
@app.route('/menu')
def menu():
    return render_template('menu.html')

#Blog For every can rating Us --------->
@app.route('/blog')
def blog():
    return render_template('blog.html')
