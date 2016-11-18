from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)




import os
from flask_login import LoginManager

from config import basedir


lm = LoginManager()
lm.init_app(app)
lm.login_view='login'



from WebGit import views, models

@lm.user_loader
def load_user(user_id):
    return models.User.query.get(user_id)