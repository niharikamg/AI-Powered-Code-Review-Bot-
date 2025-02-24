import click
from main import main

@click.command()
@click.argument("file_path")
def review(file_path):
    main(file_path)

if __name__ == "__main__":
    review()