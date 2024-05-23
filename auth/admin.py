import os
from datetime import datetime

from flask_admin import Admin
from flask_login import current_user
from flask_wtf.file import FileAllowed
from werkzeug.utils import secure_filename

from config.settings import app, db
from .models import User
from flask_admin.contrib.sqla import ModelView
from flask_admin.form.upload import FileUploadField


# Set Admin session

class CustomAdminView(ModelView):
    form_overrides = {'image1': FileUploadField,
                      'image2': FileUploadField
                      }
    form_args = {
        'image1': {
            'validators': [FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!')],
            'base_path': '../medias/images/profile'
        },
        'image2': {
            'validators': [FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!')],
            'base_path': '../medias/images/profile'
        }
    }
    def on_model_change(self, form, model, is_created):
        image1_file = form.image1.data
        if image1_file:
            # Save the file to a desired location
            filename = secure_filename(image1_file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image1_file.save(file_path)

            # Update the model with the file path
            model.image1 = file_path

        super().on_model_change(form, model, is_created)
        model.updated_on = datetime.now()  # Update the field with the current datetime
        return super().on_model_change(form, model, is_created)
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin


# Define admin here
admin = Admin(app, template_mode='bootstrap3')
admin.add_view(CustomAdminView(User, db.session, name='User Admin', category='User Administration'))
