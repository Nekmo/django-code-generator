from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Generate code for speed development'

    def add_arguments(self, parser):
        parser.add_argument('template', type=str)
        parser.add_argument('app', type=str)

    def handle(self, *args, **options):
        pass
