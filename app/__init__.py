

import os

# external home
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from config import Config


db = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.login_view = 'authentication.do_login'
login_manager.session_protection = 'strong'
bcrypt = Bcrypt()


def create_app(config_class=Config):  # development, production, testing
    app = Flask(__name__)
    app.config.from_object(config_class)
    # initialize folder
    basedir = os.path.abspath(os.path.dirname(__file__))
    UPLOAD_FOLDER = 'static'
    app.secret_key = "secret key"
    app.config['UPLOAD_FOLDER'] = os.path.join(basedir, UPLOAD_FOLDER)
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
    # initialise application with db instance
    db.init_app(app)
    migrate.init_app(app, db)
    # initialize bootstrap
    bootstrap.init_app(app)
    # initialize login manager
    login_manager.init_app(app)
    # initialize bcrypt
    bcrypt.init_app(app)
    # import and register your blueprint name to the instance of application
    from app.Hom_File import Hom_File
    from app.authentication import authentication
    app.register_blueprint(Hom_File)
    app.register_blueprint(authentication)

    return app
