from django.core.management.base import BaseCommand
import pandas as pd
from sqlalchemy import create_engine
import pymysql
from locations.models import Entidad_Federativa

class Command(BaseCommand):
    help = 'A command to add data from a json file'

    def handle(self, *args, **options) :
        dataframe_estados = pd.read_json('locations/management/commands/estados_mx.json')
        dataframe_estados = dataframe_estados[['nombre', 'clave']]

        print(dataframe_estados)

        engine = create_engine('mysql+pymysql://root:+Guten224@localhost/tme_002_dev')
        dataframe_estados.to_sql(Entidad_Federativa._meta.db_table, if_exists = 'append', con = engine, index = False)
 