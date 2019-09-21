import click
from django.core import management
from cfn_flip import to_json
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


@main.command()
@click.argument('yaml_file')
def yaml_to_json(yaml_file):
    with open(yaml_file, 'r') as file, \
            open('tacocat_cf.json', 'w', encoding='utf-8') as output:
        try:
            output.write(to_json(file.read()))
            click.echo('File written successfully')
        except Exception as e:
            click.echo(e)


@main.command()
@click.argument('project_name')
def create_django_app(project_name):
    if not commons.is_palindrome(project_name):
        raise Exception('Project name is not a palindrome')
    management.call_command('startproject', project_name, directory='part2')
