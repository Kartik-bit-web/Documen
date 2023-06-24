from flask import Blueprint, request, redirect, render_template, flash
from module_us.login_user import data

register = Blueprint('register', __name__, static_folder="static", template_folder="templates")

@register.route('/', methods = ['POST', 'GET'])
def resis():
    if request.method == 'POST':
        nam = request.form.get('nam')
        email = request.form.get('email')
        num = request.form.get('num')
        if nam == '' and email == '':
            flash('Plase enter the email and name')
            return redirect('/register/')
        data.exe(nam, email, num)
    return render_template('resis.html')