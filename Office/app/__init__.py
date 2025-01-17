#!/usr/bin/env python3
"""Application instance """

from flask import Flask, request 
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_babel import Babel, lazy_gettext as _l


def get_locale():
    return request.accept_languages.best_match(current_app.config["LANGUAGES"])


# Initialize SQLAlchemy
db = SQLAlchemy()

migrate = Migrate()
login = LoginManager()
login.login_view = "auth.login"
login.login_message = _l("Please log in to access this page.")
mail = Mail()
moment = Moment()
babel = Babel()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    login = LoginManager(app)
    
    # Initialize SQLAlchemy
    db.init_app(app)

    with app.app_context():
        db.create_all()

    migrate.init_app(app, db)
    login.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    babel = Babel(app, locale_selector=get_locale)



    #importation and registration of blueprints
    from app.utils import bp as utils_bp
    app.register_blueprint(utils_bp, url_prefix="/utils")

    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app.main import bp as main_bp
    app.register_blueprint(main_bp, url_prefix="/main")

    



from app import models
