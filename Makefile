compile:
	sass app/static/scss/main.scss app/static/css/main.css

watch:
	sass --watch app/static/scss:app/static/css

install:
	pip install -r requiremnts.txt
	bower install


.PHONY=[install, compile]  # default action

