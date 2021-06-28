import unittest


class MkevixiTest(unittest.TestCase):
    @unittest.skip("初期動確用テスト")
    def test_mkevixl(self):
        from mkevixl.core import mkevixl

        sheet = ["test1", "test2"]
        self.assertIsNone(mkevixl("test", 1, 6))

    def test_mkevixl_validation_ok(self):
        """数値チェックOKパターン"""
        from mkevixl.core import mkevixl

        self.assertTrue(mkevixl("test", 1, 6))

    def test_mkevixl_validation_ng_start_1(self):
        """数値チェックNGパターン1 start値"""
        from mkevixl.core import mkevixl

        self.assertFalse(mkevixl("test", "aiueo", 6))

    def test_mkevixl_validation_ng_start_2(self):
        """数値チェックNGパターン2 count値"""
        from mkevixl.core import mkevixl

        self.assertFalse(mkevixl("test", 1, "aiueo"))

    def test_mkevixl_validation_ng_start_3(self):
        """数値チェックNGパターン3 両方NG"""
        from mkevixl.core import mkevixl

        self.assertFalse(mkevixl("test", "aiueo", "aiueo"))
