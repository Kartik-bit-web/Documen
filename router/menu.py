from flask import Blueprint, request, redirect, render_template
from module_us.login_user import engine, meeting

menu_in = Blueprint('menu_in', __name__, static_folder="static", template_folder="templates")

@menu_in.route('/menu')
def menu():
    getDate = engine.execute('Select * from menu_add')
    x = getDate.fetchall()
    return render_template('menu.html', x=x)