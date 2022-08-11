from flask import render_template, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user

from app.authentication.forms import RegistrationForm, LoginForm, PasswdForm
from app.authentication import authentication as auth
from app.authentication.models import User
from app.Hom_File.models import File


@auth.route('/register', methods=['GET', 'POST'])
def register_user():
    if current_user.is_authenticated:
        flash('You are already logged-in')
        return redirect(url_for('Hom_File.home'))
    form = RegistrationForm()

    if form.validate_on_submit():
        User.create_user(
            user=form.name.data,
            email=form.email.data,
            password=form.password.data
        )
        flash('Registration Successful')
        return redirect(url_for('authentication.do_login'))
    return render_template('registration.html', form=form)


@auth.route('/login', methods=['GET', 'POST'])
def do_login():
    if current_user.is_authenticated:
        flash('You are already logged-in')
        return redirect(url_for('Hom_File.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(user_email=form.email.data).first()
        if not user or not user.check_password(form.password.data):
            flash('Invalid credentials, please try again!')
            return redirect(url_for('authentication.do_login'))

        login_user(user, form.stay_loggedin.data)
        return redirect(url_for('Hom_File.home'))

    return render_template('login.html', form=form)


# change password
@auth.route('/change', methods=['GET', 'POST'])
def change_paswd():
    form = PasswdForm()
    return render_template('change_pwd.html', form=form)


@auth.route('/logout')
@login_required
def do_logout():
    logout_user()
    return redirect(url_for('Hom_File.home'))


@auth.route('/der')
def Fil_User():
    userlands = File.query.all()
    return render_template('files.html', userlands=userlands)
