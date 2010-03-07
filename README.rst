Overview
========

nose-exclude is a `Nose`_ plugin that allows you to easily specify
directories to be excluded from testing.


Exclude Directories
===================

the `--exclude-dir=EXCLUDED_DIR`_ is made available after installation. It
may be used multiple times to exclude multiple directories from testing. The
directory paths may be absolute or relative.

Example::
    
    $ nosetests --exclude-dir=test_dirs/build \
        --exclude-dir=test_dirs/test_not_me test_dirs
    ....
    ----------------------------------------------------------------------
    Ran 4 tests in 0.006s
    
    OK

This example will exclude the directories test_dirs/build and 
test_dirs/test_not_me from nosetests' test searching.

