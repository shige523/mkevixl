import unittest


class MkevixiTest(unittest.TestCase):
    def test_mkevixl(self):
        from mkevixl.core import mkevixl

        sheet = ["test1", "test2"]
        print(mkevixl(1, "test", 6, sheet))
        self.assertIsNone(mkevixl(1, "test", 6, sheet))

    def test_mode_3_is_false(self):
        from mkevixl.core import mkevixl

        sheet = 10
        self.assertFalse(mkevixl(3, "test.xlsx", 10, sheet))

    def test_mode_2_shnamestr_is_false(self):
        from mkevixl.core import mkevixl

        sheet = 10
        self.assertFalse(mkevixl(2, "test.xlsx", 10, sheet))
