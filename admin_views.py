from flask_admin.contrib.sqla import ModelView
from flask_admin.form import FileUploadField
from flask import current_app
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

class ShowsModelView(ModelView):
    def __init__(self, model, session, base_path=None):
        self.base_path = base_path

        self.form_extra_fields = {
            'img_filename': FileUploadField(
                'Image',
                base_path=self.base_path,
                relative_path=''
            )
        }

        super().__init__(model, session)

    def on_model_delete(self, model):
        if model.img_filename:
            file_path = os.path.join(self.base_path, model.img_filename)

            if os.path.exists(file_path):
                os.remove(file_path)


class MerchModelView(ModelView):
    def __init__(self, model, session, base_path=None):
        self.base_path = base_path

        self.form_extra_fields = {
            'image': FileUploadField(
                'Image', base_path=self.base_path,
                relative_path=''
            )
        }

        super().__init__(model, session)
    