Overview
========

nose-exclude is a `Nose`_ plugin that allows you to easily specify
directories to be excluded from testing.

.. _Nose: http://somethingaboutorange.com/mrl/projects/nose


Exclude Directories
===================

The ``--exclude-dir=`` option is made available after installation of the
plugin. The option may be used multiple times to exclude multiple directories 
from testing. The directory paths provided may be absolute or relative.

Example::
    
    $ nosetests --exclude-dir=test_dirs/build \
        --exclude-dir=test_dirs/test_not_me test_dirs
    ....
    ----------------------------------------------------------------------
    Ran 4 tests in 0.006s
    
    OK

This example will exclude the directories test_dirs/build and 
test_dirs/test_not_me from nosetests' test searching.

Using File-Based Exclusion List
-------------------------------

The ``--exclude-dir-file=`` option can be used to pass in a predefined
list of directories contained within a file. ``nose-exclude`` expects each
directory to be excluded to be on its own line.

Example::
    
    $ nosetests --exclude-dir-file=test_dirs/exclude_dirs.txt \
        test_dirs
    ....
    ----------------------------------------------------------------------
    Ran 4 tests in 0.006s
    
    OK

where ``exclude_dirs.txt`` might look like: ::

    test_dirs/build
    test_dirs/test_not_me


Bugs
====
Please report all bugs (and patches) to http://bitbucket.org/kgrandis/nose-exclude/

