import os

from django.core.management.base import BaseCommand, CommandError

from django_code_generator.templates import Template


directory = os.path.abspath(os.path.join(os.path.abspath(__file__), '../../../'))


class Command(BaseCommand):
    help = 'Generate code for speed development'

    def add_arguments(self, parser):
        parser.add_argument('template', type=str)
        parser.add_argument('app', type=str)

    def handle(self, *args, **options):

        Template(os.path.join(directory, 'templates', options['template']), options['app'])
