from flask import Blueprint, request, redirect, render_template
from module_us.login_user import engine

date_selection = Blueprint('date_selection', __name__, static_folder="static", template_folder="templates")

@date_selection.route('/date_shown', methods=['POST', 'GET'])
def date_shown():
    if request.method == 'POST':
        dates = request.form.get('dates')
        result = 'SELECT dated FROM date_data'
        show = engine.execute(result)
        x = show.fetchall()
        for i in x:
            if i['dated'] == dates:
                return 'Alread Booked on this date'
            return 'Booking Avalible'

    return render_template('/date_shown.html')