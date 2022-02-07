import get_content
import post_content
import utils
import click
import json

creds = utils.get_creds()


@click.group()
def iget():
    pass


@ iget.command()
@ click.option('--username', default=creds['instagram_username'], help="username")
def discovery(username):
    params = utils.get_creds()
    params['instagram_account_id'] = username
    response = get_content.get_business_discovery(params)
    for i in response['business_discovery']:
        if i == "media":
            for j in response['business_discovery'][i]['data']:
                click.echo()
                click.echo('Comment count: ' + str(j['comments_count']))
                click.echo('Like count:' + str(j['like_count']))
                click.echo("Link: " + j['permalink'])
            continue
        click.echo(i)
        click.echo(response['business_discovery'][i])
    # click.echo(response)


@iget.command()
@click.option('--username', default=creds['instagram_username'], help="username")
def userdetails(username):
    params = utils.get_creds()
    params['id'] = username
    response = get_content.get_user_data(params)
    for i in response['business_discovery']:
        click.echo(i + ": " + str(response['business_discovery'][i]))
        # click.echo(response['business_discovery'][i])
    # click.echo(response)


@iget.command()
@click.option('--username', default=creds['instagram_username'], help="username")
def usermedia(username):
    params = utils.get_creds()
    params['id'] = username
    response = get_content.get_user_media(params)
    for i in response['business_discovery']['media']['data']:
        click.echo("\n\n\n")
        click.echo('Link: ' + str(i['permalink']))
        click.echo('Id: ' + str(i['id']))
        click.echo('Comment count: ' + str(i['comments_count']))
        click.echo('Like count:' + str(i['like_count']))
        click.echo('Caption: ' + str(i['caption']))
    # click.echo(response)
