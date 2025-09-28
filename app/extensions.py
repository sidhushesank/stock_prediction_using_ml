from flask_login import LoginManager
login_manager = LoginManager()
login_manager.login_view = 'auth.login'  # Redirect if not logged in

from app.models.user import User

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)
