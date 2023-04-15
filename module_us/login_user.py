import sqlalchemy as db

engine = db.create_engine("sqlite:///again.db")
conn = engine.connect()
metadata = db.MetaData()

data = db.Table('info', metadata, 
                db.Column('id', db.Integer(), primary_key = True, autoincrement=True),
                db.Column('Name', db.CHAR()),
                db.Column('email', db.Text()), 
                db.Column('Number', db.Integer())
                )

admin_login = db.Table('admin_info', metadata, 
                db.Column('id', db.Integer(), primary_key = True, autoincrement=True),
                db.Column('email', db.Text()),
                db.Column('password', db.Text())
                )

post_hall = db.Table('post_hall', metadata,
                db.Column('id', db.Integer(), primary_key = True, autoincrement=True),
                db.Column('title', db.Text()),
                db.Column('content', db.Text())
                )

meet_date = db.Table('meet_date', metadata,
                db.Column('id', db.Integer(), primary_key = True, autoincrement=True),
                db.Column('name', db.Text()),
                db.Column('dated', db.Text())
                )

menu_add = db.Table('menu_add', metadata, 
                db.Column('id', db.Integer(), primary_key = True, autoincrement=True), 
                db.Column('started', db.Text()),
                db.Column('breakfast', db.Text()),
                db.Column('lunch', db.Text()),
                db.Column('dinner', db.Text()),
                db.Column('special', db.Text())
                )

blog_add = db.Table('blog_add', metadata,
                db.Column('id', db.Integer(), primary_key = True, autoincrement=True),
                db.Column('title', db.Text()),
                db.Column('post', db.Text())
                )



def exe(nam, email, num):
    starts = db.insert(data).values(Name=nam, email=email, Number=num)
    engine.execute(starts)

def admin_info(email, psd):
    starts = db.insert(admin_login).values(email=email, password=psd)
    engine.execute(starts)

#hall item here------>
def hall_post(title, content):
    starts = db.insert(post_hall).values(title= title, content=content)
    engine.execute(starts)

def hall_edit(title, content, id):
    start = "update post_hall set title=?, content=? where id=?"
    add = (title, content, id)
    engine.execute(start, add)
#hall detail end here------>

#meeting items here--------->
def meeting(name, dated):
    starts = db.insert(meet_date).values(name= name, dated=dated)
    engine.execute(starts)
#meeting end here--------->

#menu items here--------->
def menu_admin(started, breakfast, lunch, dinner, special):
    startup = db.insert(menu_add).values(started=started, breakfast=breakfast, lunch=lunch, dinner=dinner, special=special)
    engine.execute(startup)

def update_menu(started, breakfast, lunch, dinner, special, id):
    startup = "Update menu_add set started=?, breakfast=?, lunch=?, dinner=?, special=? where id=?"
    add_it = (started, breakfast, lunch, dinner, special, id)
    engine.execute(startup, add_it)
#menu items here--------->

#blog items here--------->
def blog(title, post):
    getblog = db.insert(blog_add).values(title=title, post=post)
    engine.execute(getblog)
    

metadata.create_all(engine)