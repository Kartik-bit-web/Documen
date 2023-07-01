from flask import Blueprint, render_template
from module_us.login_user import *

hall_in = Blueprint('hall_in', __name__, static_folder="static", template_folder="templates")

@hall_in.route('/')
def hall_admin():
    get_it = engine.execute("select * from post_hall")
    x = get_it.fetchall()
    return render_template('hall.html', x=x)