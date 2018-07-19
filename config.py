import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'very-strong-password'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CELERY_BROKER_URL = 'redis://localhost:6379'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379'
    # Debugging variables
    TEMPLATES_AUTO_RELOAD = True
    DEBUG = True
    # File Upload variables
    UPLOAD_FOLDER = '/tmp/'
    MAX_CONTENT_LENGTH = 32 * 1024 * 1024
