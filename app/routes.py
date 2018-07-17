
from datetime import datetime
from functools import wraps
from flask import Flask, render_template, redirect, request, flash, url_for, session, abort, send_file
from app import flask_app, db
from app.models import User, Note

with flask_app.test_request_context():
    db.init_app(flask_app)
    db.create_all()

def login_required(role="ANY"):
    """ Restricts access to pages only to logged in users"""
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not session.get('logged_in'):
                return abort(403)
            urole = User.query.filter_by(username=session.get('username')).first().get_urole()
            if ((urole != role) and (role != "ANY")):
                return abort(403)
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper


def newLogEntry(obj):
    """
    Modifies the Note object based on the data 
    contained in the request JSON

    return:
        obj: Type Note
    """
    obj.date = request.form.get('date')
    obj.time = request.form.get('time')
    obj.duration = request.form.get('duration')
    obj.regNum = request.form.get('registration')
    obj.droneNum = request.form.get('drone')
    obj.pilot = request.form.get('pilotName')
    obj.pilotNum = request.form.get('pilotNumber')
    obj.location = request.form.get('location')
    obj.altitude = request.form.get('altitude')
    obj.weather = request.form.get('weather')
    obj.distance = request.form.get('distance')
    obj.notes = request.form.get('notes')
    return obj


@flask_app.errorhandler(403)
def bad_request(error):
    """ As the name suggests, it handles 403 errors
    and returns the 403 page"""
    return render_template("errors/403.html")


@flask_app.route('/')
def index():
    """Index page, redirects to login if user is not logged in"""
    myLogs = Note.query.all()
    if not session.get('logged_in'):
        return render_template('login.html')
    return render_template("api.html", myLogs=myLogs)


@flask_app.route("/user_panel/<string:user>")
@login_required()
def panel(user):
    """
        Returns information about the user's logged activity
    """
    user = User.query.filter_by(username=session.get('username')).first()
    logs = Note.query.filter_by(user_id=user.id).all()
    date_count = len([drone.date for drone in Note.query.all() if drone.pilot==session.get('username')])
    drones = set([drone.droneNum for drone in Note.query.all()])
    return render_template("panel.html", user=user, logs=logs.__repr__(),
                           date=date_count, drones=drones)


@flask_app.route('/login', methods=['POST'])
def login():
    """
    Returns the Login page view unless the user is already logged in 
    in which case it redirects to the Index page.
    """
    if session.get('logged_in'):
        return redirect(url_for('index'))

    POST_EMAIL = request.form['email']
    user = User.query.filter_by(email=POST_EMAIL).first()
    if user is None or not user.check_password(request.form['password']):
        flash('Invalid email or password')
        return render_template("login.html", failed="failed")
    session['username'] = user.username
    session['logged_in'] = True
    return redirect(url_for('index'))


@flask_app.route('/logout', methods=['GET', 'POST'])
def logout():
    """
    Logs the User out and redirects to the Login page
    """
    session.pop('username', None)
    session['logged_in'] = False
    return redirect(url_for('index'))


@flask_app.route('/register', methods=['GET', 'POST'])
def register():
    """
    Returns the user registration page when used as a GET request 
    or creates and stores a new user when called as a POST
    """
    if request.method == 'GET':
        return render_template('register.html')
    else:
        new_user = User()
        new_user.username = request.form.get('username')
        new_user.email = request.form.get('email')
        new_user.set_password(request.form.get('password'))
        new_user.user_role = 'user'
        new_user.registered_on = datetime.utcnow()
        db.session.add(new_user)
        db.session.commit()
        flash('User successfully registered')
    return redirect(url_for('index'))


@flask_app.route('/pass_reset', methods=['GET', 'POST'])
def pass_reset():
    """ To Be Implemented   """
    return "<h1>You're all out of luck... now GTFO!!!</h1>"


@flask_app.route('/create', methods=['GET', 'POST'])
@login_required()
def create():
    """    Returns page to create new log entry    """
    if not session.get('logged_in'):
        return render_template('login.html')
    return render_template('create.html')


@flask_app.route('/student', methods=['GET', 'POST'])
def student():
    """    Test method for new features    """
    return render_template('dashboard/dash_view.html')


@flask_app.route('/delete/<int:rowid>', methods=['GET', 'POST'])
@login_required()
def delete(rowid):
    """ Deletes an entry from the log"""
    Note.query.filter_by(id=rowid).delete()
    db.session.commit()
    return redirect(url_for('index'))


@flask_app.route('/edit_log/<int:itemid>', methods=['POST'])
def edit_log(itemid):
    """
    Redirects to the index page after storing edits to the
    passed(by ID) log entry
    """
    edited = Note.query.filter_by(id=itemid).first()
    edited = newLogEntry(edited)
    db.session.commit()
    return redirect(url_for('index'))


@flask_app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        results = request.form
    return render_template("results.html", result=results)


@flask_app.route('/log', methods=['GET', 'POST'])
@login_required()
def new_entry():
    """
    Returns the "main" log view page when used as a GET request 
    or creates and stores a new log entry when called as a POST
    """
    if request.method == "GET":
        return render_template("api.html")
    new_log = Note()
    new_log = newLogEntry(new_log)
    new_log.user = User.query.filter_by(username=session['username']).first()
    db.session.add(new_log)
    db.session.commit()
    flash('Congratulations on creating a new entry!')
    return redirect(url_for('index'))