from program import db

class Todolist(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50), nullable=False,defailt="My Todo List")]