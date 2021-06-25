import unittest


class MkevixiTest(unittest.TestCase):
    def test_mkevixl(self):
        from mkevixl.core import mkevixl

        self.assertIsNone(mkevixl("test", "test1", "test2"))
