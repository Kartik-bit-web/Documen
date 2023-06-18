from flask import Blueprint, request, redirect, render_template
from module_us.login_user import admin_login

admin_login = Blueprint('admin_login', __name__, static_folder="static", template_folder="templates")

@admin_login.route('/admin_login', methods = ['POST', 'GET'])
def admin():
    if request.method == 'POST':
        emails = request.form.get('email')
        psd = request.form.get('psd')
        check = admin_login.engine.execute("Select * from admin_info")
        x = check.fetchall()
        for i in x:
            if i['email'] == emails and i['password'] == psd:
                return redirect('/Dashboard')
            return redirect('/admin')
    else:
        return render_template('/admin/login_as_admin.html')