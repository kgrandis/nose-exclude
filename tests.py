import os
import unittest
from nose.plugins import PluginTester
from nose_exclude import NoseExclude

class TestNoseExcludeDirs_Relative_Args(PluginTester, unittest.TestCase):
    """Test nose-exclude directories using relative paths passed
    on the commandline via --exclude-dir
    """

    activate = "--exclude-dir=test_dirs/build"
    args = ['--exclude-dir=test_dirs/test_not_me']
    plugins = [NoseExclude()]
    suitepath = os.path.join(os.getcwd(), 'test_dirs')

    def test_proper_dirs_omitted(self):
        assert "FAILED" not in self.output

class TestNoseExcludeDirs_Absolute_Args(PluginTester, unittest.TestCase):
    """Test nose-exclude directories using absolute paths passed
    on the commandline via --exclude-dir
    """

    plugins = [NoseExclude()]
    suitepath = os.path.join(os.getcwd(), 'test_dirs')

    def __init__(self, *args, **kwargs):
        self.activate = "--exclude-dir=%s" % \
                os.path.join(self.suitepath, 'build') 
        arg_path = os.path.join(self.suitepath, 'test_not_me')
        self.args = ['--exclude-dir=%s' % arg_path]
        super(TestNoseExcludeDirs_Absolute_Args, self).__init__(*args, **kwargs)

    def test_proper_dirs_omitted(self):
        assert "FAILED" not in self.output

class TestNoseExcludeDirs_Relative_Args_File(PluginTester, unittest.TestCase):
    """Test nose-exclude directories using relative paths passed
    by file using --exclude-dir-file
    """

    activate = "--exclude-dir-file=test_dirs/exclude_dirs.txt"
    plugins = [NoseExclude()]
    suitepath = os.path.join(os.getcwd(), 'test_dirs')

    def test_proper_dirs_omitted(self):
        assert "FAILED" not in self.output

class TestNoseExcludeDirs_Relative_Args_Mixed(PluginTester, unittest.TestCase):
    """Test nose-exclude directories using paths passed
    by file and commandline
    """

    activate = "--exclude-dir-file=test_dirs/exclude_dirs2.txt"
    args = ["--exclude-dir=test_dirs/test_not_me"]
    plugins = [NoseExclude()]
    suitepath = os.path.join(os.getcwd(), 'test_dirs')

    def test_proper_dirs_omitted(self):
        assert "FAILED" not in self.output

class TestNoseExcludeEnvVariables(PluginTester, unittest.TestCase):
    """Test nose-exclude's use of environment variables"""
    
    #args = ['--exclude-dir=test_dirs/test_not_me']
    activate = "-v"
    plugins = [NoseExclude()]
    suitepath = os.path.join(os.getcwd(), 'test_dirs')
    
    env = {'NOSE_EXCLUDE_DIRS':'test_dirs/build;test_dirs/test_not_me'}

    def test_proper_dirs_omitted(self):
        assert "FAILED" not in self.output

class TestNoseExcludeDirsEnvFile(PluginTester, unittest.TestCase):
    """Test nose-exclude directories using relative paths passed
    by file specified by environment variable
    """

    activate = "-v"
    plugins = [NoseExclude()]
    env = {'NOSE_EXCLUDE_DIRS_FILE':'test_dirs/exclude_dirs.txt'}
    suitepath = os.path.join(os.getcwd(), 'test_dirs')

    def test_proper_dirs_omitted(self):
        assert "FAILED" not in self.output


if __name__ == '__main__':
    unittest.main()
