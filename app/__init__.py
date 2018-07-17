import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from celery import Celery
from config import Config

def make_celery(app):
    celery = Celery(app.import_name, backend=app.config['CELERY_RESULT_BACKEND'],
                    broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery

flask_app = Flask(__name__)
flask_app.config.from_object(Config)


celery = make_celery(flask_app)
db = SQLAlchemy(flask_app)
migrate = Migrate(flask_app, db)

from app import routes, models

# with flask_app.test_request_context():
#     db.init_app(flask_app)
#     db.create_all()
# logging.basicConfig(filename='strava.log', level=logging.DEBUG)
