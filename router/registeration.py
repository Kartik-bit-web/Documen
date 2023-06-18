from flask import Blueprint, request, redirect, render_template
from module_us.login_user import data

register = Blueprint('register', __name__, static_folder="static", template_folder="templates")

@register.route('/register', methods = ['POST', 'GET'])
def resis():
    if request.method == 'POST':
        nam = request.form.get('nam')
        email = request.form.get('email')
        num = request.form.get('num')
        data.exe(nam, email, num)
    return render_template('resis.html')