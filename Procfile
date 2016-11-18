web: python run.py runserver 0.0.0.0:$PORT
init: python db_create.py && pybabel compile -d app/translations
upgrade: python db_upgrade.py && pybabel compile -d app/translations
