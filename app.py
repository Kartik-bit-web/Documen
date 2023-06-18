from flask import Flask, render_template, request, url_for, redirect, Blueprint
from module_us import login_user

from router.registeration import register
from router.login_user import loginn
from router.admin_login.admin_login import admin_login
from router.admin_login.admin_in import admin_main
from router.hall import hall_in
from router.date_shown import date_selection
from router.booking import booking_in
from router.menu import menu_in
from router.blog import blog_in


app = Flask(__name__)

blueprint = Blueprint()

#Indexing page --------->
@app.route('/')
def hel():
    return render_template('index.html')


#Registration page --------->
app.register_blueprint(register , url_prefix="/register")
@app.route('/register', methods = ['POST', 'GET'])
def resis():
    return render_template('resis.html')

#Login For those who Just create acccount --------->
app.register_blueprint(loginn , url_prefix="/loginn")
@app.route('/logIn', methods = ['POST', 'GET'])
def loginn():
    return render_template('login.html')

#Admin Login Page Here --------->
app.register_blueprint(admin_login , url_prefix="/admin_login")
@app.route('/admin_login', methods = ['POST', 'GET'])
def admin(): 
    return render_template('/admin/login_as_admin.html')
    

#Admin Dashboard --------->
app.register_blueprint(admin_main , url_prefix="/admin_main")
@app.route('/Dashboard')
def admin_dash():
    return render_template('/admin/admin_index.html')


#Hall page --------->
app.register_blueprint(hall_in , url_prefix="/hall")
@app.route('/hall')
def hall():
    return render_template('hall.html')


#Date shown for Users here------>
app.register_blueprint(date_selection , url_prefix="/date_selection")
@app.route('/date_shown', methods=['POST', 'GET'])
def date_shown():
    return render_template('/date_shown.html')
    

#Booking Details page --------->
app.register_blueprint(booking_in , url_prefix="/booking_in")
@app.route('/booking', methods = ["POST", "GET"])
def booking():
    return render_template('booking.html')

@app.route('/meeting')
def meet_date():
    getDate = login_user.engine.execute('Select * from meet_date')
    x = getDate.fetchall()
    return render_template('/admin/show_meet_date.html', x=x)
#Booking Details page Ended here --------->


#Menus for Functions page --------->
app.register_blueprint(menu_in , url_prefix="/menu_in")
@app.route('/menu')
def menu():
    return render_template('menu.html')


#Blog For every can rating Us --------->
app.register_blueprint(blog_in , url_prefix="/blog_in")
@app.route('/blog')
def blog():
    return render_template('blog.html')