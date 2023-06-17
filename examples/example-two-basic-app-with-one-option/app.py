import click

@click.group()
def todoist():
    pass

@todoist.command()
@click.option('--count', default=1, type=int, help='number of times to print')
def version(count):
    for _ in range(count):
        click.echo("Todoist 0.1.0")

if __name__ == '__main__':
    todoist()
