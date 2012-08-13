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
    # Start a line with a '#' to include
    # Comments
    test_dirs/test_not_me

Using Environment Variables
---------------------------

``--exclude-dir=`` can be set by the environment variables ``NOSE_EXCLUDE_DIRS``.
Multiple exclude paths may be entered by separating them using a ``;``.
The environment variable ``NOSE_EXCLUDE_DIRS_FILE`` when set to the path of a
file-based exclusion list functions as though it were passed in with ``--exclude-dir-file=``.


Nose Configuration Files
========================

``nose-exclude`` options can also be passed to ``nosetests`` using a ``.noserc`` or ``nose.cfg`` file. If you more than one directory are to be excluded 
separate their values with newlines using the same configuration key: ::

    [nosetests]
    exclude-dir=test_dirs/exclude_dirs
                test_dirs/more_excludes



Bugs
====
Please report all bugs (and patches) to http://bitbucket.org/kgrandis/nose-exclude/

