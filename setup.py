import os
from setuptools import setup


def read(fname):
    """
    Read README.md as long description if found.
    Otherwise just return short description.
    """
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return "Simple flask boilerplate application."

setup(
    name="flask_boilerplate",
    version="0.1.0",
    author="Antti Ruotsalainen",
    author_email="antti.ruotsalainen@hanshoi.net",
    description=("Simple flask boilerplate application."),
    license="MIT",
    keywords="web flask",
    url="https://github.com/hanshoi/flask-bootstrap-boilerplate",
    packages=['app', ],
    package_data={'flaskp_app': ['static/*', 'templates/*.html']},
    include_package_data=True,
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=[
        'Flask'
    ],
)
