from setuptools import setup

setup(
    name = "nose-exclude",
    version = "0.1.1",
    py_modules = ['nose_exclude'],
    
    entry_points = {
        'nose.plugins': ['nose-exclude = nose_exclude:NoseExclude']
        },
    install_requires = ['nose'],
)
