from flask import Blueprint, request, redirect, render_template
from module_us.login_user import engine

hall_in = Blueprint('hall_in', __name__, static_folder="static", template_folder="templates")

@hall_in.route('/hall')
def hall_admin():
    get_it = engine.execute("Select * from post_hall")
    x = get_it.fetchall()
    return render_template('hall.html', x=x)