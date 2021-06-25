import unittest
import pathlib


class MakeNewWorkBookTest(unittest.TestCase):
    def tearDown(self):
        # テスト用のファイルを削除
        file = pathlib.Path("test.xlsx")
        if file.exists():
            file.unlink()

    def test_returnfilename(self):
        from mkevixl.excel_handler import makeNewWorkBook

        self.assertEqual(makeNewWorkBook("test"), "test.xlsx")

    def test_exist_excelfile(self):
        from mkevixl.excel_handler import makeNewWorkBook

        makeNewWorkBook("test.xlsx")
        self.assertTrue(pathlib.Path("test.xlsx").exists())

    def test_wrongfilename(self):
        from mkevixl.excel_handler import makeNewWorkBook

        makeNewWorkBook("test.txt")
        self.assertTrue(pathlib.Path("test.xlsx").exists())
