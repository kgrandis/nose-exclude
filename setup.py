import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read().strip()

VERSION = '0.1.9'

setup(
    name = "nose-exclude",
    version = VERSION,
    author = "Kurt Grandis",
    author_email = "kgrandis@gmail.com",
    description = "Exclude specific directories from nosetests runs.",
    long_description = read('README.rst'),
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
    zip_safe = False,
    
    entry_points = {
        'nose.plugins': ['nose_exclude = nose_exclude:NoseExclude']
        },
    install_requires = ['nose'],
    test_suite = 'tests',
)
