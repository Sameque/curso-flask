from flask_admin import Admin

admin = Admin(template_mode="bootstrap2")


def init_app(app):
    admin.init_app(app)
