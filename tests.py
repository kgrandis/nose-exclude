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

    env = {'NOSE_EXCLUDE_DIRS': 'test_dirs/build;test_dirs/test_not_me'}

    def test_proper_dirs_omitted(self):
        assert "FAILED" not in self.output


class TestNoseExcludeDirsEnvFile(PluginTester, unittest.TestCase):
    """Test nose-exclude directories using relative paths passed
    by file specified by environment variable
    """

    activate = "-v"
    plugins = [NoseExclude()]
    env = {'NOSE_EXCLUDE_DIRS_FILE': 'test_dirs/exclude_dirs.txt'}
    suitepath = os.path.join(os.getcwd(), 'test_dirs')

    def test_proper_dirs_omitted(self):
        assert "FAILED" not in self.output


class TestNoseExcludeDirs_Arg_Does_Not_Exist(PluginTester, unittest.TestCase):
    """Test nose-exclude directories for a directory that doesn't exist.
    """

    activate = "--exclude-dir=test_dirs/build"
    args = ["--exclude-dir=test_dirs/test_not_me \n --exclude-dir=test_dirs/test_i_dont_exist"]
    plugins = [NoseExclude()]
    suitepath = os.path.join(os.getcwd(), 'test_dirs')

    def test_proper_dirs_omitted(self):
        assert "FAILED" not in self.output


class TestNoseExcludeDirsNoseWorkingDir(PluginTester, unittest.TestCase):
    """Test nose-exclude directories with Nose's working directory."""

    activate = "--exclude-dir=test_not_me"
    args = ["--where=test_dirs"]
    plugins = [NoseExclude()]
    suitepath = os.path.join(os.getcwd(), 'test_dirs')

    def tearDown(self):
        # Nose changes cwd to config.workingDir, need to reset it
        import os
        os.chdir(os.path.join(os.getcwd(), os.path.pardir))

    def test_proper_dirs_omitted(self):
        assert "FAILED" not in self.output


class TestNoseExcludeTest(PluginTester, unittest.TestCase):
    """Test nose-exclude a single test"""

    activate = "--exclude-test=test_dirs.unittest.tests.UnitTests.test_a"
    plugins = [NoseExclude()]
    suitepath = os.path.join(os.getcwd(), 'test_dirs/unittest')

    def test_test_excluded(self):
        assert 'Ran 2 tests' in self.output


class TestNoseExcludeTestNegative(PluginTester, unittest.TestCase):
    """Test nose-exclude a test that does not exist"""

    activate = "--exclude-test=test_dirs.unittest.tests.UnitTests.does_not_exist"
    plugins = [NoseExclude()]
    suitepath = os.path.join(os.getcwd(), 'test_dirs/unittest')

    def test_test_excluded_negative(self):
        assert 'Ran 3 tests' in self.output


class TestNoseExcludeMultipleTest(PluginTester, unittest.TestCase):
    """Test nose-exclude multiple tests"""

    activate = "--exclude-test=test_dirs.unittest.tests.UnitTests.test_a"
    args = [
        "--exclude-test=test_dirs.unittest.tests.UnitTests.test_b",
        "--exclude-test=test_dirs.unittest.tests.test_c"
    ]
    plugins = [NoseExclude()]
    suitepath = os.path.join(os.getcwd(), 'test_dirs/unittest')

    def test_tests_excluded(self):
        assert 'Ran 0 tests' in self.output


class TestNoseExcludeTestViaFile(PluginTester, unittest.TestCase):
    """Test nose-exclude tests with a file"""

    activate = "--exclude-test-file=test_dirs/exclude_tests.txt"
    plugins = [NoseExclude()]
    suitepath = os.path.join(os.getcwd(), 'test_dirs/unittest')

    def test_tests_excluded(self):
        assert 'Ran 1 test' in self.output


class TestNoseExcludeDirAndTests(PluginTester, unittest.TestCase):
    """Test nose-exclude tests by specifying dirs and tests"""

    activate = "--exclude-test=test_dirs.unittest.tests.UnitTests.test_a"
    args = [
        "--exclude-dir=test_dirs/build",
        "--exclude-dir=test_dirs/build2",
        "--exclude-dir=test_dirs/fish",
        "--exclude-dir=test_dirs/test_not_me",
        "--exclude-dir=test_dirs/test_yes",
        "--exclude-dir=test_dirs/test_yes2",
    ]
    plugins = [NoseExclude()]
    suitepath = os.path.join(os.getcwd(), 'test_dirs')

    def test_tests_excluded(self):
        assert 'Ran 2 tests' in self.output


class TestNoseExcludeTestClass(PluginTester, unittest.TestCase):
    """Test nose-exclude tests by class"""

    activate = "--exclude-test=test_dirs.unittest.tests.UnitTests"

    plugins = [NoseExclude()]
    suitepath = os.path.join(os.getcwd(), 'test_dirs/unittest')

    def test_tests_excluded(self):
        assert 'Ran 1 test' in self.output


class TestNoseExcludeTestFunction(PluginTester, unittest.TestCase):
    """Test nose-exclude tests by function"""

    activate = "--exclude-test=test_dirs.unittest.tests.test_c"

    plugins = [NoseExclude()]
    suitepath = os.path.join(os.getcwd(), 'test_dirs/unittest')

    def test_tests_excluded(self):
        assert 'Ran 2 tests' in self.output


class TestNoseExcludeTestModule(PluginTester, unittest.TestCase):
    """Test nose-exclude tests by module"""

    activate = "--exclude-test=test_dirs.unittest.test"

    plugins = [NoseExclude()]
    suitepath = os.path.join(os.getcwd(), 'test_dirs/unittest')

    def test_tests_excluded(self):
        assert 'Ran 3 tests' in self.output

if __name__ == '__main__':
    unittest.main()
