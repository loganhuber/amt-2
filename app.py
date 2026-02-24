from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from routes import register_routes
from models import db, Admins, Shows, Merch
from admin_views import AdminModelView, ShowsModelView
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SECRET_KEY'] = 'my_secret'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db.init_app(app)
admin = Admin(app)


admin.add_view(AdminModelView(Admins, db.session))
admin.add_view(
    ShowsModelView(
        Shows,
        db.session,
        base_path=os.path.join(app.root_path, 'static/assets/flyers')
    )
)

admin.add_view(ModelView(Merch, db.session))

register_routes(app)

if __name__=='__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)