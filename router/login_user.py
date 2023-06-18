from flask import Blueprint, request, redirect, render_template
from module_us.login_user import data

loginn = Blueprint('loginn', __name__, static_folder="static", template_folder="templates")

@loginn.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        emails = request.form.get('email')
        check = data.engine.execute("Select * from info ")
        x = check.fetchall()
        for i in x:
            if i['email'] == emails:
                return redirect('/hall')
        return redirect('/logIn')
    else:
        return render_template('login.html')