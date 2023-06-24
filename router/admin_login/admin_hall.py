from flask import Blueprint, request, redirect, render_template
from module_us.login_user import *

admin_main = Blueprint('admin_main', __name__, static_folder="static", template_folder="templates")




