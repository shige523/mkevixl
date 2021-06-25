import click

# from excel_handler import make_file
from mkevixl.excel_handler import make_file

# from excel_handler import make_file


@click.command()
@click.option("--filename", "-f", default="newfile", show_default=True, help="ファイル名称")
@click.option(
    "--mode",
    "-m",
    default="n",
    show_default=True,
    type=int,
    help="作成モード 1:シート名指定 2: 数字指定",
)
@click.option(
    "--sheetcount", "-s", default=1, show_default=True, type=int, help="モード2用:追加するシート数"
)
@click.argument("sheetnames")
def cli(filename, sheetcount, mode, *sheetnames):
    # エビデンス用Excelファイル生成ツール
    # click.echo(arg_name, filename)
    # print(arg_name, filename)
    if len(sheetnames) == 0:
        sheetnames.append("new")

    mkevixl(mode, filename, sheetcount, sheetnames)
    # 動確用
    click.echo(filename)


def mkevixl(mode, filename, sheetcount, sheetnames):

    if mode != 1 and mode != 2:
        return False

    if mode == 2:
        if isint(sheetnames) == False:
            return False

    make_file(filename, sheetcount, mode, sheetnames)


def isint(s):
    try:
        int(s)
    except ValueError:
        print("valuerr")
        return False
    else:
        return True
