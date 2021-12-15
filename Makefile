default: run-server

run-server:
	python manage.py runserver --settings='bakeademy_project.settings.dev'

make-migrations:
	python manage.py makemigrations ${app} --settings='bakeademy_project.settings.dev'

migrate:
	python manage.py migrate ${app} --settings='bakeademy_project.settings.dev'
	