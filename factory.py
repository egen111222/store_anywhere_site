from auth_models import User
from main import app
from models import db

users = [{"login":"admin",
          "password":"123123"}]


def create_users():
    for user in users:
        new_user = User(login=user["login"],
                        password=user["password"])
        db.session.add(new_user)
    db.session.commit()
    print("Користувачі успішно створені")

with app.app_context():
    create_users()
