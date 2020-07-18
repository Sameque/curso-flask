from delivery.ext.db import db
from delivery.ext.db import models


def create_db():
    """Creates database"""
    db.create_all()


def drop_db():
    """Cleans database"""
    db.drop_all()


def populate_db():
    """Populate db with sample data"""
    data = [
        models.User(),
    ]
    db.session.bulk_save_objects(data)
    db.session.commit()
    return models.User.query.all()
