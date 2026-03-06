from models import Admins
from app import app, db
import getpass
from werkzeug.security import generate_password_hash


def get_admin_info() -> tuple:
    username = input("Enter Your Username: \n")

    while True:
        password = getpass.getpass("Enter Your Password: \n")
        confirm = getpass.getpass("Confirm Password: \n")

        if password == confirm:
            break
        else:
            print("Passwords do not match. Try again.\n")


    return (username, password)



with app.app_context():
    username, password = get_admin_info()

    existing = Admins.query.filter_by(username=username).first()
    if existing:
        print("Username already exists")
    else:
        pw_hash = generate_password_hash(password)

        admin = Admins(
            username=username,
            pw_hash=pw_hash
        )

        db.session.add(admin)
        db.session.commit()

        print(f"User '{username}' added to admins.")


