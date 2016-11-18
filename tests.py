from coverage import coverage

cov = coverage(branch=True, omit=['flask/*', 'tests.py'])
cov.start()

import os
import unittest
from datetime import datetime, timedelta

from config import basedir
from WebGit import app, db
from WebGit.models import User, Repo
from WebGit import password_hash


class TestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()



    def test_password_hash(self):
        password = 'hello world'
        pass_hash = password_hash.generate_password_hash('hello world')
        wrong_pass = 'evil world'
        assert pass_hash != 'hello world'
        assert password_hash.check_password_hash(password=password, password_hash=pass_hash)
        assert not password_hash.check_password_hash(password=wrong_pass, password_hash=pass_hash)

    def test_user(self):
        # make valid nicknames
        n = User.make_valid_nickname('John_123')
        assert n == 'John_123'
        n = User.make_valid_nickname('John_[123]\n')
        assert n == 'John_123'
        # create a user
        u = User(nickname='john', email='john@example.com', password='123456')
        db.session.add(u)
        db.session.commit()
        assert u.is_active() == True
        assert u.is_anonymous() == False
        assert u.id == int(u.get_id())
        assert u.verify_password('123456')
        assert not u.verify_password('123')

if __name__ == '__main__':
    try:
        unittest.main()
    except:
        pass
    cov.stop()
    cov.save()
    print "\n\nCoverage Report:\n"
    cov.report()
    print "\nHTML version: " + os.path.join(basedir, "tmp/coverage/index.html")
    cov.html_report(directory='tmp/coverage')
    cov.erase()