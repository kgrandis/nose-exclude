import os
from setuptools import setup

f = open(os.path.join(os.path.dirname(__file__), 'README.rst'))
long_description = f.read().strip()
f.close()

VERSION = '0.1.4'

setup(
    name = "nose-exclude",
    version = VERSION,
    author = "Kurt Grandis",
    author_email = "kgrandis@gmail.com",
    description = "Exclude specific directories from nosetests runs.",
    long_description = long_description,
    license = 'GNU LGPL',
    url = "http://bitbucket.org/kgrandis/nose-exclude",
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        ("License :: OSI Approved :: GNU Library or Lesser General " 
        "Public License (LGPL)"), 
        "Topic :: Software Development :: Testing",
        "Programming Language :: Python",
        ],

    py_modules = ['nose_exclude'],
    package_data = {'':['README.rst']},
    zip_safe = False,
    
    entry_points = {
        'nose.plugins': ['nose_exclude = nose_exclude:NoseExclude']
        },
    install_requires = ['nose'],
    test_suite = 'tests',
)
