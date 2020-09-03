import json
import os
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from core.models import Hotdog


class Command(BaseCommand):
    help = 'Generates fixture from raw json scrape data'

    def add_arguments(self, parser):
        parser.add_argument('file', type=str)

    def handle(self, *args, **options):
        with open(options['file']) as scrape_file:
            json_data = json.load(scrape_file)
            fixture_data = []
            index = 1
            for hotdog in json_data:
                hotdog_entry = {
                    'model':  'core.hotdog', 'pk': index,
                    'fields': {
                        'name': hotdog['name'],
                        'link': hotdog['link']
                    }
                }
                fixture_data.append(hotdog_entry)
                index += 1
            fixture_filename = os.path.join(
                settings.BASE_DIR, 'core', 'fixtures', 'hotdog_data.json')
            with open(fixture_filename, 'w') as outfile:
                json.dump(fixture_data, outfile)
