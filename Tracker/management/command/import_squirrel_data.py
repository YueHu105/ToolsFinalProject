from django.core.management.base import BaseCommand
import pandas as pd
from Tracker.models import Squirrels

class Command(BaseCommand):
    help = 'help string'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str)

    def handle(self, *args, **options):
        df = pd.read_csv(options['file_path'])
        dfn = df.drop_duplicates('Unique_Squirrel_ID','first')
        sqList = []
        for _, row in dfn.iterrows():
            sq = Squirrels(Latitude=row['X'], Longitude=row['Y'], Unique_Squirrel_ID=row['Unique_Squirrel_ID'],
                           Shift=row['Shift'], Date=row['Date'],
                           Age=row['Age'], Primary_Fur_Color=row['Primary_Fur_Color'],
                           Location=row['Location'],
                           Specific_Location=row['Specific_Location'], Running=row['Running'], Chasing=row['Chasing'],
                           Climbing=row['Climbing'], Eating=row['Eating'], Foraging=row['Foraging'],
                           Other_Activities=row['Other_Activities'], Kuks=row['Kuks'], Quaas=row['Quaas'],
                           Moans=row['Moans'], Tail_flags=row['Tail_flags'], Tail_twitches=row['Tail_twitches'],
                           Approaches=row['Approaches'], Indifferent=row['Indifferent'], Runs_from=row['Runs_from']
                           )
            sqList.append(sq)
        Squirrels.objects.bulk_create(sqList)