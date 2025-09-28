from flask import Flask
from app.extensions import login_manager

def create_app():
    app = Flask(__name__)
    app.secret_key = 'your_secret_key'  # Required for sessions
    
    login_manager.init_app(app)
    
    # Import and register blueprints
    from app.routes.auth import auth_bp
    from app.routes.main import main_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    
    return app
