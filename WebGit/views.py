from flask import render_template, flash, redirect, session, url_for, request, g, jsonify, abort
from flask_login import login_user, logout_user, current_user, login_required
from WebGit import app, db, lm, db_service, models
from forms import LoginForm, RegistrationForm, RepositoryAddForm
from models import User, ROLE_USER, ROLE_ADMIN


@app.before_request
def before_request():
    g.user = current_user


@app.route('/')
@app.route('/index')
@login_required
def index():
    user = g.user
    form = RepositoryAddForm(request.form)
    repos = models.Repo.query.all()
    for repo in repos:
        repo.user_name = User.query.filter_by(id = repo.user_id).first().nickname
    return render_template('index.html',
                           title='Home',
                           form=form,
                           user=user,
                           repos=repos)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm(request.form)
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return db_service.try_login(form.email.data, form.password.data)
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           )


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm(request.form)
    if form.validate_on_submit():
        return db_service.add_user(nickname=form.username.data, email=form.email.data,
                                   password=form.password.data)
    return render_template('register.html', form=form)


@app.route('/add_repository', methods=['POST'])
@login_required
def create_repo():
    print request.json
    print request.json['url']
    if not request.json or not 'url' in request.json:
        abort(401)
    print request.json['url']
    print request.json['comment']
    repo = db_service.add_repository(request.json['url'], request.json['comment'], g.user.id)
    return jsonify('success'), 201
