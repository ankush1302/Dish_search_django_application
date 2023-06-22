import csv
from django.core.management.base import BaseCommand
from food.models import Restaurant

class Command(BaseCommand):
    help = 'Import data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                items = eval(row['items'])
                Restaurant.objects.create(
                    name=row['name'],
                    location=row['location'],
                    items=items,
                    lat_long=row['lat_long'],
                    full_details=row['full_details']
                )
        self.stdout.write(self.style.SUCCESS('Data imported successfully.'))
