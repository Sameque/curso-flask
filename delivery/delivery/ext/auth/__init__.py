from delivery.ext.admin import admin
from delivery.ext.db import db
from delivery.ext.db.models import User
from flask_admin.contrib.sqla import ModelView
from flask_admin.actions import action
from flask_admin.contrib.sqla import filters
from flask import flash


def format_email(self, request, obj, *_):
    return obj.email.replace("@", " at ")


class UserAdmin(ModelView):
    column_list = ['email', 'admin']
    can_edit = False
    column_formatters = {"email": format_email}
    column_labels = {"email": "User login"}
    column_searchable_list = [User.email]
    column_filters = (
        'email',
        'admin',
        filters.FilterLike(
            User.email,
            'Fixed Title',
            options=(('test1', 'Test 1'), ('test2', 'Test 2'))
        )
    )

    @action(
        'notify',
        'Notify users',
        'Are you sure you want to notify the selected users?'
    )
    def action_notify_users(self, ids):
        for _id in ids:
            print(f"Notifying user {_id} ....")

        flash(f'{len(ids)} users notified.', 'success')

    @action('toggle_admin', 'Toggle admin permission', 'Are you sure?')
    def toggle_admin(self, ids):
        for user in User.query.filter(User.id.in_(ids)).all():
            user.admin = not user.admin
        db.session.commit()


def init_app(app):
    admin.add_view(UserAdmin(User, db.session))
