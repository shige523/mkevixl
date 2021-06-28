import click

# from excel_handler import make_file
from mkevixl.excel_handler import make_file

# from excel_handler import make_file


@click.command()
@click.option("--filename", "-f", default="newfile", show_default=True, help="ファイル名称")
@click.option(
    "--start",
    "-st",
    default=1,
    show_default=True,
    type=int,
    help="シート名称の開始値",
)
@click.option(
    "--sheetcount", "-sh", default=1, show_default=True, type=int, help="モード2用:追加するシート数"
)
def cli(filename, start, sheetcount):

    # エビデンス用Excelファイル生成ツール
    if mkevixl(filename, start, sheetcount) == False:
        return print("処理失敗")
    else:
        return print("処理完了")


def mkevixl(filename, start, sheetcount):

    if __isint(start) == False or __isint(sheetcount) == False:
        return False

    make_file(filename, start, sheetcount)
    return True


def __isint(s):
    try:
        int(s)
    except ValueError:
        print("valuerr")
        return False
    else:
        return True
