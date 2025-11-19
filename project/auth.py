import smtplib
from email.mime.text import MIMEText
from flask import Blueprint, render_template, redirect, url_for, request, flash, current_app
from flask_login import login_user, logout_user, current_user
from itsdangerous import URLSafeTimedSerializer, BadSignature, SignatureExpired
from .models import User
from .forms import LoginForm, RegistrationForm
from . import db

auth = Blueprint('auth', __name__)


def _get_serializer():
    return URLSafeTimedSerializer(current_app.config['SECRET_KEY'])


def generate_verification_token(email):
    s = _get_serializer()
    return s.dumps(email, salt='email-confirm')


def confirm_verification_token(token, expiration=3600):
    s = _get_serializer()
    return s.loads(token, salt='email-confirm', max_age=expiration)


def send_verification_email(user, confirm_url):
    subject = 'Confirm your Task-Master account'
    body = f"""Hi {user.username},

Please verify your email by clicking the link below:
{confirm_url}

If you did not sign up, please ignore this email.
"""

    sender = current_app.config.get('MAIL_DEFAULT_SENDER') or current_app.config.get('MAIL_USERNAME')
    if not sender:
        current_app.logger.warning('MAIL_DEFAULT_SENDER or MAIL_USERNAME is not configured; skipping sending email to %s', user.email)
        return

    host = current_app.config.get('MAIL_SERVER')
    port = current_app.config.get('MAIL_PORT', 587)
    username = current_app.config.get('MAIL_USERNAME')
    password = current_app.config.get('MAIL_PASSWORD')
    use_tls = current_app.config.get('MAIL_USE_TLS', True)

    if not host:
        current_app.logger.warning('MAIL_SERVER is not configured; skipping sending email to %s', user.email)
        return

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = user.email

    with smtplib.SMTP(host, port) as server:
        if use_tls:
            server.starttls()
        if username and password:
            server.login(username, password)
        server.sendmail(sender, [user.email], msg.as_string())


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()

        token = generate_verification_token(user.email)
        confirm_url = url_for('auth.verify_email', token=token, _external=True)
        current_app.logger.info('Email confirmation link for %s: %s', user.email, confirm_url)
        send_verification_email(user, confirm_url)

        flash('Your account has been created! Please check your email to verify your account.', 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html', title='Register', form=form)


@auth.route('/verify_email/<token>')
def verify_email(token):
    try:
        email = confirm_verification_token(token)
    except SignatureExpired:
        flash('The verification link has expired. Please log in to request a new one.', 'warning')
        return redirect(url_for('auth.login'))
    except BadSignature:
        flash('The verification link is invalid.', 'danger')
        return redirect(url_for('auth.login'))

    user = User.query.filter_by(email=email).first()
    if not user:
        flash('Account not found.', 'danger')
        return redirect(url_for('auth.register'))

    if user.is_email_verified:
        flash('Your email is already verified. Please log in.', 'info')
    else:
        user.is_email_verified = True
        db.session.commit()
        flash('Your email has been verified. You can now log in.', 'success')
    return redirect(url_for('auth.login'))

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            if not user.is_email_verified:
                flash('Please verify your email address before logging in.', 'warning')
                return redirect(url_for('auth.login'))
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.welcome'))