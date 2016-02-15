# flask-bootstrap-boilerplate
Simple flask boilerplate with bootstrap, jquery and bower.

Using bower for dynamically install packages rather than using fixed packages.

Supporting Frozen-Flask for using pure html sites as well as app.

## Prequisities
* npm (install node)
* pip (python installed)
** we also recommend `virtualenv` and `virtualenvwrapper`
* bower `npm install -g bower`
* sass `gem install sass`

## Install
We need to install python dependencies and bower packages.
```bash
make install
```

Note that for developing you need to install development dependencies.
`pip install -r requirements/development.txt`

## Usage
Run server with `python server.py`

Watch changes and compile sass
```bash
make watch
# in other terminal
make run  # starts a server in localhost:5000
```


## Freeze
To create a static bundle of your application using Frozen-Flask do following.
```bash
pip install -r requirements/development.txt  # for right dependencies
python freeze.py
```


## References
Big thanks to [romainbergers yeoman-flask generator](https://github.com/romainberger/yeoman-flask) for providing some valuable guidelines.