import sqlalchemy as db

engine = db.create_engine("sqlite:///test2.db")
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


def exe(nam, email, num):
    starts = db.insert(data).values(Name=nam, email=email, Number=num)
    engine.execute(starts)

def admin_info(email, psd):
    starts = db.insert(admin_login).values(email=email, password=psd)
    engine.execute(starts)

def hall_post(title, content):
    starts = db.insert(post_hall).values(title= title, content=content)
    engine.execute(starts)



metadata.create_all(engine)