from django.core.management.base import BaseCommand
import pandas as pd
from sqlalchemy import create_engine
import pymysql
from login.models import Alcaldia

class Command(BaseCommand):
    help = 'A command to add data from a cvs file'

    def handle(self, *args, **options):
        alcaldias_df = pd.read_csv('login/management/commands/alcaldias.csv')
        alcaldias_df = alcaldias_df.drop(columns =  ['cve_alcaldia', 'entidad', 'cve_ent', 'cvegeo', 'geo_shape'])
        alcaldias_df.columns = ['nombre', 'latitud', 'longitud']
        print(alcaldias_df)

        engine = create_engine('mysql+pymysql://root:+Guten224@localhost/tme_002_dev')

        alcaldias_df.to_sql(Alcaldia._meta.db_table, if_exists = 'append', con = engine, index = False)

