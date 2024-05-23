from flask_admin import AdminIndexView, Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from auth.models import User, db
from config.settings import app


# Set Admin session
class MyModelView(ModelView):
    def is_accessible(self):
        print(current_user.is_authenticated)
        return current_user.is_authenticated and current_user.is_admin


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        print(current_user.is_authenticated)
        return current_user.is_authenticated and current_user.is_admin


# Define admin here
admin = Admin(app, index_view=MyAdminIndexView(), name='Admin Panel')
admin.add_view(MyModelView(User, db.session))