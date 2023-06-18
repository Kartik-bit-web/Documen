from flask import Blueprint, request, redirect, render_template
from module_us.login_user import engine, meeting

booking_in = Blueprint('booking_in', __name__, static_folder="static", template_folder="templates")

@booking_in.route('/booking', methods = ["POST", "GET"])
def booking():
    if request.method == 'POST':
        nm = request.form.get('nm')
        dated = request.form.get('dated')
        meeting(nm, dated)
        return redirect('/hall')
    return render_template('booking.html')