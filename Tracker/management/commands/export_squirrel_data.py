from django.core.management.base import BaseCommand
import pandas as pd
import sqlite3 as sql3

class Command(BaseCommand):
    help = 'help string'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str)

    def handle(self, *args, **options):
        with sql3.connect( './db.sqlite3') as con:
            dfe = pd.read_sql_query('select * from Tracker_Squirrels', con=con)
            dfe.to_csv(options['file_path'])