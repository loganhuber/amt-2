from flask_admin.contrib.sqla import ModelView
from flask_admin.form import FileUploadField
from werkzeug.security import generate_password_hash
from wtforms import PasswordField
import os

class AdminModelView(ModelView):
    form_excluded_columns = ('pw_hash')

    form_extra_fields = {
        'password' : PasswordField("Password")
    }

    def on_model_change(self, form, model, is_created):
        if form.password.data:
            model.pw_hash = generate_password_hash(form.password.data)