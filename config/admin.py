from flask_admin import Admin, form
from flask_login import current_user
from config.settings import app, db
from home.models import Resume, Skill, Project
from auth.models import User
from flask_admin.contrib.sqla import ModelView


# Custom field for multiple image uploads
class MultipleImageUploadField(form.FileUploadField):
    def pre_validate(self, form):
        super().pre_validate(form)
        # Validate each uploaded image (e.g., check file format, size, etc.)


# Custom view for articles
class AdminModelView(ModelView):
    form_overrides = {
        'image1': MultipleImageUploadField,
        'image2': MultipleImageUploadField,
    }
    form_args = {
        'image1': {
            'label': 'Image1',
            'base_path': 'medias/images/profile',  # Set your desired upload directory
            'allow_overwrite': False,  # Prevent overwriting existing files
        },
        'image2': {
            'label': 'Image2',
            'base_path': 'medias/images/profile',  # Set your desired upload directory
            'allow_overwrite': False,  # Prevent overwriting existing files
        }
    }

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
            'base_path': 'medias/images/profile',  # Set your desired upload directory
            'allow_overwrite': False,  # Prevent overwriting existing files
        }
    }
    # Add form_ajax_refs to enable editing of the user_id field
    form_ajax_refs = {
        'user': {
            'fields': ['fullname'],  # Display the 'name' field of the User model in the search field
        }
    }


class SkillsModelView(ModelView):
    form_ajax_refs = {
        'user': {
            'fields': ['fullname'],  # Display the 'name' field of the User model in the search field
        }
    }


class ResumesModelView(ModelView):
    form_ajax_refs = {
        'user': {
            'fields': ['fullname'],  # Display the 'name' field of the User model in the search field
        }
    }


# Define admin here
admin = Admin(app)
admin.add_view(AdminModelView(User, db.session, name='User Admin', category='User Administration'))
admin.add_view(ResumesModelView(Resume, db.session, name="Resume", category="User Administration"))
admin.add_view(SkillsModelView(Skill, db.session, name="Skill", category="User Administration"))
admin.add_view(ProjectModelView(Project, db.session, name="Project", category="User Administration"))
