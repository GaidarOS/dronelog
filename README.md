# DroneLogBook

## App components
- Flask/Jinja2
- Flask-login
- SQLAlchemy
- Alembic
- Celery (This and the next are not completely integrated yet)
- Redis

## Run your own
 - clone repo
 - `cd dronelog`
 - create a file named `api.html` in `app/templates`
    - add the following in the file
     ```
     {% extends "table.html" %}
     {% block API %}YOUR_GOOGLE_API_KEY_HERE{% endblock %}
    ```
 - `$ export FLASK_APP=dronelog.py`
 - `$ flask run --port [#] --host [#.#.#.#]`
 - optionally `--debug` can be added to run in a debug environment

## Features

- Secured features behind login requirements
- Create a log with several dropdown options


## Issues and Planned Features
 - Issue: Password Recovery
 - Issue: Migrate to a more reliable DB (PostgreSQL/MongoDB)
 - Feature: SSL Security

## Development Process
Side project, working on spare time
May be slow but bear with me will be good(eventually)


## Project Story
TBA


## License
- All content is licensed under a CC­BY­NC­SA 4.0 license.
- All software code is licensed under GNU GPLv3.

## Contact
 - karvouniaris.b@gmail.com