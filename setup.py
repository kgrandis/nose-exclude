import os
from setuptools import setup

f = open(os.path.join(os.path.dirname(__file__), 'README.txt'))
long_description = f.read().strip()
f.close()

setup(
    name = "nose-exclude",
    version = "0.1.2",
    author = "Kurt Grandis",
    author_email = "kgrandis@gmail.com",
    description = "Exclude specific directories from nosetests runs.",
    long_description = long_description,
    license = 'Apache License, Version 2.0',

    py_modules = ['nose_exclude'],
    package_dir = {'':'src'},
    packages = ['nose-exclude'],
    package_data = {'':['README.txt']},
    
    entry_points = {
        'nose.plugins': ['nose_exclude = nose_exclude:NoseExclude']
        },
    install_requires = ['nose'],
)
