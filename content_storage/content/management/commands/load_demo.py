from django.core.management import call_command
from django.core.management.base import BaseCommand

DEMO_FIXTURE = 'demo.json'


class Command(BaseCommand):
    help = 'Load demo data'    # noqa

    def handle(self, *args, **options):
        call_command('loaddata', DEMO_FIXTURE)
        output = self.style.SUCCESS('Demo data has been loaded successfully')
        self.stdout.write(output)
