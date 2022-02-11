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


@ iget.command()
@ click.option('--username', default=creds['instagram_username'], help="username")
@ click.option('--link', required=True, help="link to post")
def media(username, link):
    params = utils.get_creds()
    params['id'] = username
    params['permalink'] = link
    response = get_content.get_media_details(params)
    click.echo("")
    click.echo('Link: ' + str(response['permalink']))
    click.echo('Id: ' + str(response['id']))
    click.echo('Comment count: ' + str(response['comments_count']))
    click.echo('Like count:' + str(response['like_count']))
    click.echo('Caption: ' + str(response['caption']))
    # click.echo(response)


@ iget.command()
@ click.option('--username', default=creds['instagram_username'])
def userinsights(username):
    params = utils.get_creds()
    response = get_content.get_user_insights(params)
    # for i in response['business_discovery']
    click.echo(response)


@ iget.command()
@ click.option('--username', default=creds['instagram_username'])
@ click.option('--link', required=True, help="link to post")
def mediainsights(username, link):
    params = utils.get_creds()
    params['id'] = username
    params['permalink'] = link
    post = get_content.get_media_details(params)
    params['media_id'] = post['id']
    response = get_content.get_media_insights(params)
    # for i in response['business_discovery']
    click.echo(response)


@ iget.command()
@ click.option('--caption', default='')
@ click.option('--media_url', required=True, help="link to image")
def post(caption, media_url):
    params = utils.get_creds()
    params['caption'] = caption
    params['media_url'] = media_url
    params['media_type'] = 'IMAGE'
    media_id = post_content.create_media_object(params)
    response = post_content.publish_media(media_id['id'], params)
    click.echo(response.get('id', 'Could not post'))


@iget.command()
@click.option("--access_token", required=True)
@click.option("--client_id")
@click.option("--client_secret")
def set(access_token, client_id, client_secret):
    with open("credentials.json", "r") as jsonFile:
        cred = json.load(jsonFile)
    cred["access_token"] = access_token
    if client_id:
        cred["client_id"] = client_id
    if client_secret:
        cred["client_secret"] = client_secret
    with open("credentials.json", "w") as jsonFile:
        json.dump(cred, jsonFile)

    click.echo("Set successfully")
# demopost = "https://i.ytimg.com/vi/Mu3BfD6wmPg/maxresdefault.jpg"
