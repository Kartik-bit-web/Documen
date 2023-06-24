from flask import Blueprint, request, redirect, render_template, flash
from module_us.login_user import *

loginn = Blueprint('loginn', __name__, static_folder="static", template_folder="templates")

@loginn.route('/', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        emails = request.form.get('email')
        check = data.engine.execute("Select * from info ")
        x = check.fetchall()
        for i in x:
            if i['email'] == emails:
                return redirect('/hall')
        
        redirect('/register')
        return flash('You cannot Logged in. First Registered here:- ')
    return render_template('login.html')