import unittest
import pathlib
import openpyxl


class make_new_workbook_nameTest(unittest.TestCase):
    def test_no_extension(self):
        from mkevixl.excel_handler import make_new_workbook_name

        self.assertEqual(make_new_workbook_name("test"), "test.xlsx")

    def test_extension(self):
        from mkevixl.excel_handler import make_new_workbook_name

        self.assertEqual(make_new_workbook_name("test.xlsx"), "test.xlsx")

    def test_wrong_extension(self):
        from mkevixl.excel_handler import make_new_workbook_name

        self.assertTrue(make_new_workbook_name("test.txt"), "test.xlsx")


class AddWorkSheetTest(unittest.TestCase):
    # def setUp(self):
    #     wb = openpyxl.Workbook()
    #     wb.save("AddWorkSheetTest.xlsx")

    # def tearDown(self):
    #     # テスト用のファイルを削除
    #     file = pathlib.Path("AddWorkSheetTest.xlsx")
    #     if file.exists():
    #         file.unlink()

    def test_makefile_mode1(self):
        filename = "AddWorkSheetTest_1.xlsx"
        file = pathlib.Path(filename)
        sheetcount = 1
        mode = 1
        sheetnames = ["abc", "dge"]
        from mkevixl.excel_handler import make_file

        make_file(mode, filename, sheetcount, sheetnames)
        self.assertTrue(file.exists())

    def test_makefile_mode2(self):
        filename = "AddWorkSheetTest_2.xlsx"
        file = pathlib.Path(filename)
        sheetcount = 10
        mode = 2
        sheetnames = 5
        from mkevixl.excel_handler import make_file

        make_file(mode, filename, sheetcount, sheetnames)
        self.assertTrue(file.exists())
