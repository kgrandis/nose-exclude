import os
import unittest
from nose.plugins import PluginTester

from nose_exclude import NoseExclude

class TestNoseExcludeDirs_Relative_Args(PluginTester, unittest.TestCase):

    exclude_args = "--exclude-dir=test_dirs/build"
    activate = exclude_args
    root = os.getcwd()
    target_arg = os.path.join(root, 'test_dirs')
    suitepath = target_arg
    args = ['-vvvv', '--exclude-dir=test_dirs/test_not_me']
    plugins = [NoseExclude()]

    #def __init__(self, *args, **kwargs):
    #    super(TestNoseExclude, self).__init__(*args, **kwargs) 
        

    def test_output(self):
        assert "FAILED" not in self.output

    def me(self):
        print self.argv
        #print self.addargs
        print "XXXX", self.nose, dir(self.nose)
        print "test Names", self.nose.testNames
        print "want", self.nose.__dict__
        for line in self.output:
            print "out", line

    #def runTest(self):
    #    pass

    #def makeSuite(self):
    #    #return self.target_arg
    #    return unittest.TestSuite(tests=[TestNoseExclude()])

if __name__ == '__main__':
    unittest.main()
