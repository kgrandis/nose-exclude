import unittest


class TestBase(unittest.TestCase):
    def setUp(self):
        super(TestBase, self).setUp()
        return None


class SuperclsTests(TestBase):
    def test_a(self):
        assert True


def test_b(self):
    assert True
