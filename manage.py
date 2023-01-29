from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_login import (UserMixin, login_user, LoginManager, current_user, logout_user, login_required)
def deploy():
    """Run deployment tasks."""
    from app import create_app, db
    from flask_migrate import upgrade, migrate, init, stamp
    from models import User
    app = create_app()
    app.app_context().push()
    db.create_all()
    # migrate database to latest revision
    init()
    stamp()
    migrate()
    upgrade()


deploy()