from flask import url_for
from flask_admin import Admin, form
from flask_login import current_user
from config.settings import app, db
from home.models import Resume, Skill, Project, Information, ContactMe
from auth.models import User
from flask_admin.contrib.sqla import ModelView


# Custom field for multiple image uploads
class MultipleImageUploadField(form.FileUploadField):
    def pre_validate(self, form):
        super().pre_validate(form)
        # Validate each uploaded image (e.g., check file format, size, etc.)


# Custom view for articles
class AdminModelView(ModelView):

    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin


class ProjectModelView(ModelView):
    column_list = ['id', 'name', 'image', 'link', 'user_id']  # Add 'user_id' to the column list
    form_overrides = {
        'image': MultipleImageUploadField,
    }
    form_args = {
        'image': {
            'label': 'Image',
            'base_path': 'static/images/projects',  # Set your desired upload directory
            'allow_overwrite': False,  # Prevent overwriting existing files
        }
    }
    # Add form_ajax_refs to enable editing of the user_id field
    form_ajax_refs = {
        'user': {
            'fields': ['email'],  # Display the 'name' field of the User model in the search field
        }
    }

    def _list_thumbnail(view, context, Project, name):
        if not Project.image:
            return ''

        # Get the URL of the image using url_for
        image_url = url_for('static', filename='images/projects/' + Project.image)

        return image_url

    # Register the column formatter for the 'image' column
    column_formatters = {
        'image': _list_thumbnail,
    }

    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin


class SkillsModelView(ModelView):
    form_ajax_refs = {
        'user': {
            'fields': ['email'],  # Display the 'name' field of the User model in the search field
        }
    }

    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin


class ResumesModelView(ModelView):
    form_ajax_refs = {
        'user': {
            'fields': ['email'],  # Display the 'name' field of the User model in the search field
        }
    }

    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin


class ContactMeModelView(ModelView):

    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin


class InformationsModelView(ModelView):
    form_overrides = {
        'image1': MultipleImageUploadField,
        'image2': MultipleImageUploadField,
        'resume_file': MultipleImageUploadField
    }
    form_args = {
        'resume_file': {
            'label': 'resume_file',
            'base_path': 'static/files',  # Set your desired upload directory
            'allow_overwrite': True,  # Prevent overwriting existing files
        },
        'image1': {
            'label': 'Image1',
            'base_path': 'static/images/profile',  # Set your desired upload directory
            'allow_overwrite': False,  # Prevent overwriting existing files
        },
        'image2': {
            'label': 'Image2',
            'base_path': 'static/images/profile',  # Set your desired upload directory
            'allow_overwrite': False,  # Prevent overwriting existing files
        }
    }
    form_ajax_refs = {
        'user': {
            'fields': ['email'],  # Display the 'name' field of the User model in the search field
        }
    }

    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin


# Define admin here
admin = Admin(app)
admin.add_view(AdminModelView(User, db.session, name='User Admin'))
admin.add_view(ResumesModelView(Resume, db.session, name="Resume"))
admin.add_view(SkillsModelView(Skill, db.session, name="Skill"))
admin.add_view(ProjectModelView(Project, db.session, name="Project"))
admin.add_view(ContactMeModelView(ContactMe, db.session, name="ContactMe"))
admin.add_view(InformationsModelView(Information, db.session, name="Information"))
