all:
	@echo "Use 'make help' to get targets"

help:
	@grep "^#? " [Mm]akefile

#? -------------------------------- PRODUCTION --------------------------------
#? production:     Run production server
production:
	gunicorn content_storage.core.wsgi:application -w 4 -b 0.0.0.0:8000

#? -------------------------------- DEVELOPMENT -------------------------------
#? dev:            Run development server
dev:
	python3 -m manage runserver 0.0.0.0:8000

#? lint:           Run static code analysis
lint:
	flake8

#? test:           Run linter and unit tests
test:
	python3 -m pytest -v

#? cover:          Run code test coverage measurement
cover:
	python3 -m coverage run
	python3 -m coverage report
	python3 -m coverage html

#? qa:             Run complex code analysis
qa: lint cover

#? translate:      Generate translations to russian locale
translate:
	 python3 manage.py makemessages --locale=ru --ignore=venv/* --ignore=volumes/*
