from flask_admin.contrib.sqla import ModelView
from flask_admin.form import FileUploadField
from flask import current_app
from flask_login import current_user
from flask_admin import AdminIndexView, expose
from flask import redirect, url_for
from werkzeug.security import generate_password_hash
from wtforms import PasswordField
import os


class SecureAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated
    
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login'))
    
    @expose('/')
    def index(self):
        return self.render(
            'admin/index.html',
            user=current_user.username
        )


class SecureModelView(ModelView):

    def is_accessible(self):
        return current_user.is_authenticated
    
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login'))


class AdminModelView(SecureModelView):
    form_excluded_columns = ('pw_hash')

    form_extra_fields = {
        'password' : PasswordField("Password")
    }

    def on_model_change(self, form, model, is_created):
        if form.password.data:
            model.pw_hash = generate_password_hash(form.password.data)



class ShowsModelView(SecureModelView):
    def __init__(self, model, session, upload_path):
        self.upload_path = upload_path

        self.form_extra_fields = {
            'img_filename': FileUploadField(
                'Image',
                base_path=self.upload_path
            )
        }

        super().__init__(model, session)

    def on_model_delete(self, model):
        if model.img_filename:
            file_path = os.path.join(self.upload_path, model.img_filename)

            if os.path.exists(file_path):
                os.remove(file_path)



class MerchModelView(SecureModelView):
    def __init__(self, model, session, upload_path):
        self.upload_path = upload_path

        self.form_extra_fields = {
            'img_filename': FileUploadField(
                'Image',
                base_path=self.upload_path
            )
        }

        super().__init__(model, session)

    def on_model_delete(self, model):
        if model.img_filename:
            file_path = os.path.join(self.upload_path, model.img_filename)
            if os.path.exists(file_path):
                os.remove(file_path)
    