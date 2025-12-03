import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialize extensions
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    # Create and configure the app
    app = Flask(__name__)
    
    # Load configuration from environment variables
    app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///../instance/database.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER')
    # app.config['MAIL_PORT'] = int(os.environ.get('MAIL_PORT', 587))
    # app.config['MAIL_USE_TLS'] = os.environ.get('MAIL_USE_TLS', '1') == '1'
    # app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
    # app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
    # app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_DEFAULT_SENDER', app.config['MAIL_USERNAME'])

    # Initialize extensions with the app
    db.init_app(app)
    login_manager.init_app(app)

    # Configure login manager
    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register blueprints
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/')

    # Register error handlers
    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()
        return render_template('500.html'), 500

    # Create database tables
    with app.app_context():
        db.create_all()

    return app