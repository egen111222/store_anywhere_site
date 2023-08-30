from flask import Flask
from models import db
import os
from dotenv import load_dotenv
from flask_admin import Admin
from store_models import (Item,Category,Order)
from flask_admin.contrib.sqla import ModelView
from store_part import store_app
from auth_part import auth_app
from cart_part import cart_app
from admin_adapters import ImageView,AdminView
from auth_lib import login_manager
from flask_session import Session
from flask_migrate import Migrate
from mail_lib import mail,send_mail

load_dotenv()

app = Flask(__name__,
            static_url_path='')
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DB"]
app.secret_key = os.environ["SECRET_KEY"]
app.config['FLASK_ADMIN_SWATCH'] = os.environ["ADMIN_THEME"]
app.config["SESSION_TYPE"] = os.environ["SESSION_TYPE"]



app.config["MAIL_SERVER"] = os.environ["MAIL_SERVER"]
app.config["MAIL_PORT"] = os.environ["MAIL_PORT"]
app.config["MAIL_USE_SSL"] = os.environ["MAIL_USE_SSL"]
app.config["MAIL_USERNAME"] = os.environ["MAIL_USERNAME"]
app.config["MAIL_PASSWORD"] = os.environ["MAIL_PASSWORD"]


Session(app)
migrate = Migrate(app, db)
mail.init_app(app)
login_manager.init_app(app)


db.init_app(app)
with app.app_context():
    db.create_all()
    send_mail("Title","body",["egen13@ukr.net"])






admin = Admin(app, name='Перший магазин',
              template_mode='bootstrap3')

app.register_blueprint(store_app)
app.register_blueprint(auth_app)
app.register_blueprint(cart_app)


admin.add_view(ImageView(Item, db.session))
admin.add_view(ImageView(Category, db.session))
admin.add_view(AdminView(Order, db.session))

if __name__ == "__main__":
    app.run()
