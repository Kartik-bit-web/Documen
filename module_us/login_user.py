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
def exe(nam, email, num):
    starts = db.insert(data).values(Name=nam, email=email, Number=num)
    engine.execute(starts)


metadata.create_all(engine)