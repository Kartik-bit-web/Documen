from flask import Blueprint, request, redirect, render_template, url_for
from module_us.login_user import *

admin_main = Blueprint('admin_main', __name__, static_folder="static", template_folder="templates")

@admin_main.route('/')
def admin_dashs():
    return render_template('/admin/admin_index.html')

#Displaying the Hall for admin page --------->
@admin_main.route('/admin_hall')
def admin_hall():
    getHall = engine.execute('Select * from post_hall')
    x = getHall.fetchall()
    return render_template('admin/admin_hall.html', x=x)

#Creating the post By Admin--------->
@admin_main.route('/create_post', methods= ["POST", "GET"])
def create_post():
    if request.method == 'POST':
        title = request.form.get('title')
        file = request.form.get('file')
        cmt = request.form.get('cmt')
        if title == '' and cmt == '':
            return redirect('/')
        
        hall_post(title, cmt)
        return redirect('/admin_hall')
    return render_template('admin/create_post.html')

#Updateing or Edit the post By Admin--------->
@admin_main.route('/edit_post/<id>', methods= ["POST", "GET"])
def edit_post(id):
    if request.method == 'POST':
        title = request.form.get('title')
        cmt = request.form.get('cmt')
        if title == '' and cmt == '':
            return 'somthing wrong'
            
        hall_edit(title, cmt, id)
        return redirect('/admin_hall')
    return render_template('/admin/edit_post.html')

#Deleting the post By Admin--------->
@admin_main.route('/del_post/<id>')
def del_post(id):
    delQuery = "delete from post_hall where id=?"
    engine.execute(delQuery, id)
    return redirect('/admin_main/admin_hall')







# Start From Here -------------------------------------------------->>>>>>>>>>>.


#Date watching for admin page --------->
@admin_main.route('/dated')
def date_index():
    return render_template('admin/index_date.html')

#Booking Information for admin --------->
@admin_main.route('/date_data')
def booking_data():
    result = 'SELECT * FROM date_data'
    show = engine.execute(result)
    x = show.fetchall()
    return render_template('admin/booking_data.html', x=x)

#Creating the Booking Information for admin --------->
@admin_main.route('/', methods= ["POST", "GET"])
def create_event():
    if request.method == 'POST':
        dat = request.form.get('date')
        opts = request.form.get('opt')
        nm = request.form.get('on')
        nums = request.form.get('num')
        if dat=='' and nums== '' and nm=='':
            return redirect('/event')
        else:
            data_date(dat, opts, nm, nums)
            return redirect('/Dashboard')
    
    return render_template('admin/createEvent.html')

#Edit Booking Information for admin --------->
@admin_main.route('/edit_event/<id>', methods= ["POST", "GET"])
def edit_event(id):
    if request.method == 'POST':
        dat = request.form.get('date')
        opts = request.form.get('opt')
        nm = request.form.get('on')
        nums = request.form.get('num')
        update_date(dat, opts, nm, nums, id)
    return render_template('admin/editEvent.html')

#Delete Booking Information for admin --------->
@admin_main.route('/deleteBooking/<id>', methods=['POST', 'GET'])
def deleteHere(id):
    delQuery = "delete from date_data where id=?"
    engine.execute(delQuery, id)

    return redirect('/admin_main/date_data')





#admin menu---->
@admin_main.route('/admin_menu', methods= ['POST', 'GET'])
def admin_menu():
    if request.method == 'POST':
        st = request.form.get('st')
        bf = request.form.get('bf')
        lh = request.form.get('lh')
        dn = request.form.get('dn')
        sp = request.form.get('sp')
        menu_admin(st, bf, lh, dn, sp)
        return redirect('/admin_main/admin_menu')
    
    getDate = engine.execute('Select * from menu_add')
    x = getDate.fetchall()
    return render_template('admin/admin_menu.html', x=x)

#edit menu---->
@admin_main.route('/edit_menu/<int:id>', methods= ['POST', 'GET'])
def edit_menu(id):
    if request.method == 'POST':
        st = request.form.get('st')
        bf = request.form.get('bf')
        lh = request.form.get('lh')
        dn = request.form.get('dn')
        sp = request.form.get('sp')
        update_menu(st, bf, lh, dn, sp, id)
        return redirect('/admin_main/admin_menu')
    
    return render_template('/admin/edit_menu.html')

#Delete the menu----->
@admin_main.route('/del_menu/<int:id>', methods= ['POST', 'GET'])
def del_menu(id):
    delQuery = "delete from menu_add where id=?"
    engine.execute(delQuery, id)
    return redirect('/admin_main/admin_menu')


#Blog creating here By Admin----->
@admin_main.route('/admin_blog', methods=['POST', 'GET'])
def admin_blog():
    get_it = engine.execute('Select * from blog_add')
    x =get_it.fetchall()
    return render_template('/admin/admin_blog.html', x=x)

#Blog Editing here By Admin----->
@admin_main.route('/edit_blog/<int:id>', methods=['POST', 'GET'])
def edit_blog(id):
    if request.method == 'POST':
        title = request.form.get('title')
        post = request.form.get('post')
        get_it = ('update blog_add set title=?, post=? where id=?')
        exe = (title, post, id)
        engine.execute(get_it, exe)
        return redirect('/admin_main/admin_blog')
    
    return render_template('/admin/edit_blog.html')

#Blog Ddeleting here By Admin----->
@admin_main.route('/del_blog/<int:id>', methods=['POST', 'GET'])
def del_blog(id):
    get_it = 'Delete from blog_add where id=?'
    engine.execute(get_it, id)
    return redirect('/admin_main/admin_blog')
