from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Configure SQLite database
def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)