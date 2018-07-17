from app import flask_app, db
from app.models import User, Note


@flask_app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Note': Note}
