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

#Login For those who Just create acccount --------->
@app.route('/logIn', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        emails = request.form.get('email')
        check = login_user.engine.execute("Select * from info ")
        x = check.fetchall()
        for i in x:
            if i['email'] == emails:
                return redirect('/hall')
        return redirect('/logIn')
    else:
        return render_template('login.html')

#Admin Login Page Here --------->
@app.route('/admin', methods = ['POST', 'GET'])
def admin():
    if request.method == 'POST':
        emails = request.form.get('email')
        psd = request.form.get('psd')
        check = login_user.engine.execute("Select * from admin_info")
        x = check.fetchall()
        for i in x:
            if i['email'] == emails and i['password'] == psd:
                return redirect('/Dashboard')
            return redirect('/admin')
    else:
        return render_template('/admin/login_as_admin.html')
    
#Regsistration Page End  --------->

#Admin Dashboard --------->
@app.route('/Dashboard')
def dash():
    return render_template('/admin/admin_index.html')



#Hall page --------->
@app.route('/hall')
def hall():
    return render_template('hall.html')

#Hall for admin page --------->
@app.route('/admin_hall')
def admin_hall():
    getHall = login_user.engine.execute('Select * from post_hall')
    x = getHall.fetchall()
    return render_template('admin/admin_hall.html', x=x)

@app.route('/create_post', methods= ["POST", "GET"])
def create_post():
    if request.method == 'POST':
        title = request.form.get('title')
        cmt = request.form.get('cmt')
        login_user.hall_post(title, cmt)
        return redirect('/admin_hall')
    return render_template('admin/create_post.html')

@app.route('/edit_post', methods= ["POST", "GET"])
def edit_post():
    pass









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
