import click
import sorter.media.Media as Media
from sorter.media.Media import MediaFactory as mf

@click.group()
def cli():
    pass

@cli.command()
@click.argument('media')
def play(media):
    """Riproduce un Media."""
    click.echo('riproduco ' + media)

@cli.command()
@click.argument('destination', type=click.Path(exists=True))
@click.argument('source', type=click.Path(exists=True), required=False, default='.')
def sort(destination, source):
    """Esegue l'algoritmo di Sort"""
    Media.Paths.addRoot(source)
    Media.Paths.setStore(destination)
    mf.sortAll()

if __name__ == '__main__':
    cli()