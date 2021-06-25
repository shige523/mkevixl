from openpyxl import Workbook
import os

"""Excelに対する処理を行う"""


def makeNewWorkBook(filename):
    """Excelファイルを作成する

    Args:
        filename ([type]): [description]
    """

    if not filename.endswith(".xlsx"):
        # 拡張子がxlsx以外だったら強制的に変更する
        filename = os.path.splitext(filename)[0] + ".xlsx"

    wb = Workbook()
    wb.save(filename)

    return filename


def add_work_sheet(sheetnames):
    pass
