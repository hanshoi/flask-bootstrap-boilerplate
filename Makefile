VENDOR_FOLDER=app/static/bower_components/
SCSS_FOLDER=app/static/scss/
CSS_FOLDER=app/static/css/

compile:
	sass -I $(VENDOR_FOLDER) $(SCSS_FOLDER)main.scss $(CSS_FOLDER)main.css

watch:
	sass -I $(VENDOR_FOLDER) --watch $(SCSS_FOLDER):$(CSS_FOLDER)

install:
	pip install -r requiremnts.txt
	bower install

build:
	python freeze.py

run:
	python server.py

.PHONY=[compile, run]  # default action

