import sys
import random
from datetime import date, timedelta, datetime
from django.core.management.base import BaseCommand
from django.db.models.base import ObjectDoesNotExist
import pandas as pd
from ...models import banks, branches

class Command(BaseCommand):
    help = 'Populate Banks and Branches with csv file'

    def handle(self, *args, **options):
        df = pd.read_csv('bank_branches.csv')
        for i in range(9900):
            id = int(df.iloc[i, 1])
            name = df.iloc[i, 7]
            ifsc = df.iloc[i, 0]
            branch = df.iloc[i, 2]
            address = df.iloc[i, 3]
            city = df.iloc[i, 4]
            district = df.iloc[i, 5]
            state = df.iloc[i, 6]
            b, created = banks.objects.get_or_create(id=id, name=name)
            branches.objects.get_or_create(bank=b, 
                                           ifsc=ifsc, 
                                           branch=branch, 
                                           city=city, 
                                           district=district, 
                                           state=state, 
                                           address=address)


        