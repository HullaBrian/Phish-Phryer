from typer import Typer


app = Typer()


@app.callback()
def callback() -> None:
    """
    Dummy command!
    """


@app.command()
def dummy_test():
    """
    Dummy test command
    """
    print("Hello World!")
