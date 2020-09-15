from flask import Flask
from flask_sqlalchemy import SQLALCHEMY

db = SQLALCHEMY

def create_app():
	app = Flask(__name__, static_url_path="", static_folder="static")
	db.init_app(app)
	with app.app_context():
		from mainroutes import routes
		app.register_blueprint(routes)
		db.create_all()
		return app

