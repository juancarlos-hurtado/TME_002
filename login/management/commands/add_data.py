from django.core.management.base import BaseCommand
import pandas as pd
from sqlalchemy import create_engine
import pymysql
from login.models import Colonia

class Command(BaseCommand):
    help = 'A command to add data from a csv file'

    def handle(self, *args, **options):
        dataframe_mx = pd.read_csv('cepes.csv', low_memory = False)
        dataframe_mx.drop_duplicates()

        cdmx_dataframe = dataframe_mx.loc[dataframe_mx['ciudad'] == 'Ciudad de México']

        clean_df = cdmx_dataframe.drop(columns = ['idEstado', 'idMunicipio', 'ciudad', 'zona', 'tipo'])
        clean_df.columns = ['estado', 'delegación', 'cp', 'colonia']
        clean_df['cp'] = clean_df['cp'].astype(str)
        clean_df['count'] = clean_df['cp'].str.len()

        cut_df = clean_df[clean_df['count'] == 5]
        cut_df.drop(columns = 'count')
        cut_df = cut_df[['cp', 'colonia', 'delegación', 'estado']]

        short_cp = clean_df[clean_df['count'] == 4]
        short_cp['cod_post'] = '0' + short_cp['cp'].astype(str)
        short_cp = short_cp.drop(columns = ['cp', 'count'])
        short_cp = short_cp[['cod_post', 'colonia', 'delegación','estado']]
        short_cp.columns = ['cp', 'colonia', 'delegación','estado']

        códigos_postales = pd.concat([cut_df, short_cp])

        print(códigos_postales)

        engine = create_engine('mysql+pymysql://root:+Guten224@localhost/tme_002_dev')
        códigos_postales.to_sql(Colonia._meta.db_table, if_exists = 'append' ,con = engine, index = False) 