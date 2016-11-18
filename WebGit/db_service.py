from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from WebGit import app, db, lm
from forms import LoginForm
from models import User, ROLE_USER, ROLE_ADMIN


def try_login(email, password):
    user = User.query.filter_by(email = email).first()
    if user is None: 
        flash('Invalid email. Please, try again.')
        return redirect(url_for('login'))   
    if not user.verify_password(password):    #Here must be hash
        flash('Invalid password. Please, try again')
        return redirect(url_for('login'))   
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember=remember_me)
    return redirect(request.args.get('next') or url_for('index')) 


def add_user(nickname, email, password):
    if nickname is None or email is None or password is None:
        return redirect(url_for('register'))
    if not (User.query.filter_by(nickname = nickname).one_or_none() is None):
        flash('This nickname is busy. Please, try again')
        return redirect(url_for('register'))
    if not (User.query.filter_by(email = email).one_or_none() is None):
        flash('This nickname is busy. Please, try again')
        return redirect(url_for('register'))
    u = User(nickname=nickname, email=email, password=password)
    db.session.add(u)
    db.session.commit()
    return redirect(url_for('login'))

