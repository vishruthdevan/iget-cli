import get_content
import post_content
import utils
import click
import json

creds = utils.get_creds()


@click.group()
def iget():
    pass
