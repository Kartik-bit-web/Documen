from flask import Flask, render_template, request, url_for, redirect
from module_us import login_user

app = Flask(__name__)

#Indexing page --------->
@app.route('/')
def hel():
    return render_template('index.html', name='kartik')


#Registration page --------->
@app.route('/register', methods = ['POST', 'GET'])
def resis():
    if request.method == 'POST':
        nam = request.form.get('nam')
        email = request.form.get('email')
        num = request.form.get('num')
        login_user.exe(nam, email, num)
        return redirect('/register')
    else:
        return render_template('resis.html')

#Login For those who Just create acccount --------->
@app.route('/logIn', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        emails = request.form.get('email')
        check = login_user.engine.execute("Select * from info ")
        x = check.fetchall()
        for i in x:
            if i['email'] == emails:
                return redirect('/hall')
        return redirect('/logIn')
    else:
        return render_template('login.html')

#Admin Login Page Here --------->
@app.route('/admin', methods = ['POST', 'GET'])
def admin():
    if request.method == 'POST':
        emails = request.form.get('email')
        psd = request.form.get('psd')
        check = login_user.engine.execute("Select * from admin_info")
        x = check.fetchall()
        for i in x:
            if i['email'] == emails and i['password'] == psd:
                return redirect('/Dashboard')
            return redirect('/admin')
    else:
        return render_template('/admin/login_as_admin.html')
    
#Regsistration Page End  --------->

#Admin Dashboard --------->
@app.route('/Dashboard')
def dash():
    return render_template('/admin/admin_index.html')


#Hall page --------->
@app.route('/hall')
def hall():
    get_it = login_user.engine.execute("Select * from post_hall")
    x = get_it.fetchall()
    return render_template('hall.html', x=x)

#Hall for admin page --------->
@app.route('/admin_hall')
def admin_hall():
    getHall = login_user.engine.execute('Select * from post_hall')
    x = getHall.fetchall()
    return render_template('admin/admin_hall.html', x=x)

@app.route('/create_post', methods= ["POST", "GET"])
def create_post():
    if request.method == 'POST':
        title = request.form.get('title')
        cmt = request.form.get('cmt')
        login_user.hall_post(title, cmt)
        return redirect('/admin_hall')
    return render_template('admin/create_post.html')

@app.route('/edit_post/<id>', methods= ["POST", "GET"])
def edit_post(id):
    if request.method == 'POST':
        title = request.form.get('title')
        cmt = request.form.get('cmt')
        login_user.hall_edit(title, cmt, id)
        return redirect('/admin_hall')
        
    return render_template('/admin/edit_post.html')

@app.route('/del_post/<id>')
def del_post(id):
    delQuery = "delete from post_hall where id=?"
    login_user.engine.execute(delQuery, id)
    return redirect('/admin_hall')


#Date watching for admin page --------->
@app.route('/dated')
def date_index():
    return render_template('admin/index_date.html')

@app.route('/date_data')
def booking_data():
    result = 'SELECT * FROM date_data'
    show = login_user.engine.execute(result)
    x = show.fetchall()
    return render_template('admin/booking_data.html', x=x)

@app.route('/create_event', methods= ["POST", "GET"])
def create_event():
    if request.method == 'POST':
        dat = request.form.get('date')
        opts = request.form.get('opt')
        nm = request.form.get('on')
        nums = request.form.get('num')
        if dat=='' and nums== '' and nm=='':
            return redirect('/event')
        else:
            login_user.data_date(dat, opts, nm, nums)
            return redirect('/Dashboard')
    
    return render_template('admin/createEvent.html')

@app.route('/edit_event/<id>', methods= ["POST", "GET"])
def edit_event(id):
    if request.method == 'POST':
        dat = request.form.get('date')
        opts = request.form.get('opt')
        nm = request.form.get('on')
        nums = request.form.get('num')
        login_user.update_date(dat, opts, nm, nums, id)
    return render_template('admin/editEvent.html')

@app.route('/deleteBooking/<id>', methods=['POST', 'GET'])
def deleteHere(id):
    delQuery = "delete from date_data where id=?"
    login_user.engine.execute(delQuery, id)

    return redirect('/date_data')

#Date watching for admin page End  here--------->


#Booking Details page --------->
@app.route('/booking', methods = ["POST", "GET"])
def booking():
    if request.method == 'POST':
        nm = request.form.get('nm')
        dated = request.form.get('dated')
        login_user.meeting(nm, dated)
        return redirect('/hall')
    return render_template('booking.html')

@app.route('/meeting')
def meet_date():
    getDate = login_user.engine.execute('Select * from meet_date')
    x = getDate.fetchall()
    return render_template('/admin/show_meet_date.html', x=x)
#Booking Details page Ended here --------->


#Menus for Functions page --------->
@app.route('/menu')
def menu():
    getDate = login_user.engine.execute('Select * from menu_add')
    x = getDate.fetchall()
    return render_template('menu.html', x=x)

#menu for admin can control --->
@app.route('/admin_menu', methods= ['POST', 'GET'])
def admin_menu():
    if request.method == 'POST':
        st = request.form.get('st')
        bf = request.form.get('bf')
        lh = request.form.get('lh')
        dn = request.form.get('dn')
        sp = request.form.get('sp')
        login_user.menu_admin(st, bf, lh, dn, sp)
        return redirect('/admin_menu')
    
    getDate = login_user.engine.execute('Select * from menu_add')
    x = getDate.fetchall()

    return render_template('admin/admin_menu.html', x=x)

#edit menu---->
@app.route('/edit_menu/<int:id>', methods= ['POST', 'GET'])
def edit_menu(id):
    if request.method == 'POST':
        st = request.form.get('st')
        bf = request.form.get('bf')
        lh = request.form.get('lh')
        dn = request.form.get('dn')
        sp = request.form.get('sp')
        login_user.update_menu(st, bf, lh, dn, sp, id)
        return redirect('/admin_menu')
    
    return render_template('/admin/edit_menu.html')

#Delete the menu----->
@app.route('/del_menu/<int:id>', methods= ['POST', 'GET'])
def del_menu(id):
    delQuery = "delete from menu_add where id=?"
    login_user.engine.execute(delQuery, id)
    return redirect('/admin_hall')

#Menu is end here ------------------------->


#Blog For every can rating Us --------->
@app.route('/blog')
def blog():
    get_it = login_user.engine.execute('Select * from blog_add')
    x =get_it.fetchall()
    return render_template('blog.html', x=x)

@app.route('/create_blog', methods=['POST', 'GET'])
def create_blog():
    if request.method == 'POST':
        title = request.form.get('title')
        post = request.form.get('post')
        login_user.blog(title, post)
        return redirect('/blog')
    
    return render_template('create_blog.html')

@app.route('/admin_blog', methods=['POST', 'GET'])
def admin_blog():
    get_it = login_user.engine.execute('Select * from blog_add')
    x =get_it.fetchall()
    return render_template('/admin/admin_blog.html', x=x)

@app.route('/edit_blog/<int:id>', methods=['POST', 'GET'])
def edit_blog(id):
    if request.method == 'POST':
        title = request.form.get('title')
        post = request.form.get('post')
        get_it = ('update blog_add set title=?, post=? where id=?')
        exe = (title, post, id)
        login_user.engine.execute(get_it, exe)
        return redirect('/Dashboard')
    
    return render_template('/admin/edit_blog.html')

@app.route('/del_blog/<int:id>', methods=['POST', 'GET'])
def del_blog(id):
    get_it = 'Delete from blog_add where id=?'
    login_user.engine.execute(get_it, id)
    return redirect('/Dashboard')