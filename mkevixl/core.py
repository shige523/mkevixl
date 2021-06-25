import click


@click.command()
@click.option("--filename", "-f", default="newfile", show_default=True, help="ファイル名称")
@click.argument("sheetname")
def cli(filename, *sheetnames):
    # エビデンス用Excelファイル生成ツール
    # click.echo(arg_name, filename)
    # print(arg_name, filename)
    mkevixl(filename, sheetnames)
    # 動確用
    click.echo(filename)


def mkevixl(filename, *sheetnames):
    for sheetname in sheetnames:
        print(filename, sheetname)
