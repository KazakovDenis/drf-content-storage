from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db import IntegrityError

USERNAME = 'admin'
EMAIL = 'john@doe.com'
PASSWORD = 'admin'


class Command(BaseCommand):
    help = 'Create admin user'    # noqa

    def handle(self, *args, **options):
        UserModel = get_user_model()    # noqa
        try:
            UserModel.objects.create_superuser(username=USERNAME, email=EMAIL, password=PASSWORD)
            message = f'User "{USERNAME}" has been successfully created.'
            self.stdout.write(self.style.SUCCESS(message))
        except IntegrityError:
            message = f'User "{USERNAME}" already exists.'
            self.stdout.write(self.style.NOTICE(message))
