default: run-server

run-server:
	python manage.py runserver

make-migrations:
	python manage.py makemigrations $(app)
	