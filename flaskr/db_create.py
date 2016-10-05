from flaskr import db
from models import ETFOrder

db.create_all()


db.session.commit()