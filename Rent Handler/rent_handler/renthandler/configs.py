from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login.login_manager import LoginManager

app = Flask(__name__)
app.config["SECRET_KEY"] ='df9c4a16bb99dbc3fef5f124aa4e974c'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tenant_database.sqlite3"
# app.config["UPLOAD_FOLDER"] = r"C:\Users\Pratham\Desktop\Rent Handler\rent_handler\agreements\images"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
lm = LoginManager(app)
