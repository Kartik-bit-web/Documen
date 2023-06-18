from flask import Blueprint, request, redirect, render_template
from module_us.login_user import engine, blog

blog_in = Blueprint('blog_in', __name__, static_folder="static", template_folder="templates")

@blog_in.route('/blog')
def blog():
    get_it = engine.execute('Select * from blog_add')
    x =get_it.fetchall()
    return render_template('blog.html', x=x)

@blog_in.route('/create_blog', methods=['POST', 'GET'])
def create_blog():
    if request.method == 'POST':
        title = request.form.get('title')
        post = request.form.get('post')
        blog(title, post)
        return redirect('/blog')
    
    return render_template('create_blog.html')