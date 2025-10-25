from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required

from app.models.user import User

auth_bp = Blueprint('auth', __name__)


# Root route - redirects to login page
@auth_bp.route('/')
def index():
    return redirect(url_for('auth.login'))


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.validate(username, password)
        if user:
            login_user(user)
            return redirect(url_for('main.home'))  # ← Changed from main.predict to main.home
        flash('Invalid credentials', 'danger')
    return render_template('login.html')


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
