from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from routes import register_routes
from models import db, Admins, Shows, Merch
from admin_views import AdminModelView, ShowsModelView, MerchModelView, SecureModelView, SecureAdminIndexView
from flask_login import LoginManager
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SECRET_KEY'] = 'my_secret'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db.init_app(app)
admin = Admin(app, index_view=SecureAdminIndexView())

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return Admins.query.get(int(user_id))


admin.add_view(AdminModelView(Admins, db.session))
admin.add_view(
    ShowsModelView(
        Shows,
        db.session,
        os.path.join(app.root_path, 'static/uploads/flyers')
    )
)

admin.add_view(
    MerchModelView(
        Merch,
        db.session,
        os.path.join(app.root_path, 'static/uploads/merch')
    )
)

register_routes(app)

if __name__=='__main__':
    app.run(debug=True, use_reloader=False, host='10.0.0.151')


# for mobile viewing, pass host='10.0.0.151' to app.run()