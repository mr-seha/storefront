from django.core.management.base import BaseCommand, CommandError
from django.db import connection
import os


class Command(BaseCommand):
    help = "fill database with data"

    def handle(self, *args, **options):
        current_dir = os.path.dirname(__file__)
        file_path = os.path.join(current_dir, 'seed.sql')

        try:
            f = open(file_path)
            sql = f.read()
            with connection.cursor() as cursor:
                cursor.execute(sql)

            self.stdout.write(
                self.style.SUCCESS('Database filled with data successfully')
            )

        except:
            raise CommandError('Operation failed.')
