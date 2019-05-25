import os

from django.conf import settings
from django.core.management.base import BaseCommand

from django_code_generator.templates import Template, get_template_directory

TEMPLATES_ENVIRONMENT_VARIABLE = 'DJANGO_CODE_GENERATOR_TEMPLATES'
TEMPLATE_DIRECTORY = '.dcg_templates'
directory = os.path.abspath(os.path.join(os.path.abspath(__file__), '../../../'))


try:
    import __main__
except ImportError:
    main_tpl_directory = ''
else:
    main_tpl_directory = os.path.join(os.path.abspath(__main__.__file__), TEMPLATE_DIRECTORY)


# Get directories from DJANGO_CODE_GENERATOR_TEMPLATES environment variable
template_directories = os.environ.get(TEMPLATES_ENVIRONMENT_VARIABLE, '').split(':')
# Get templates from the folder TEMPLATE_DIRECTORY in current directory
template_directories += [
    os.path.join(os.getcwd(), TEMPLATE_DIRECTORY),
]
# Get templates from DJANGO_CODE_GENERATOR_TEMPLATES settings
template_directories.extend(getattr(settings, 'DJANGO_CODE_GENERATOR_TEMPLATES', []))
template_directories = [
    # Get templates from folder TEMPLATE_DIRECTORY in manage.py directory
    main_tpl_directory,
    # Get default templates from django_code_generator project
    os.path.join(directory, 'templates'),
]


class Command(BaseCommand):
    help = 'Generate code for speed development'

    def add_arguments(self, parser):
        parser.add_argument('template', type=str)
        parser.add_argument('app', type=str)

    def handle(self, *args, **options):
        Template(get_template_directory(template_directories, options['template']), options['app']).render()
