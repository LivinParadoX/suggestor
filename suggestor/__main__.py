"""
"""

from importlib import resources

import click
import icecream

with resources.path("suggestor", "banner.txt") as banner_path:
    with open(banner_path) as f:
        BANNER = f.read()


@click.command()
def main():
    """"""
    click.echo(BANNER)
