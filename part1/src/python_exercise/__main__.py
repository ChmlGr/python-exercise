import click
from commons import commons


@click.group()
def main():
    """
    Thank you for asking for help. These tools are used to generate a Django project and convert CloudFormation code from YAML to JSON
    """
    pass


@main.command()
@click.argument('project_name')
def check_name(project_name):
    click.echo('Is this project name a palindrome ? ', nl=False)
    click.echo(commons.is_palindrome(project_name))


