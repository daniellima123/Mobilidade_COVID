# Utils
import os
import boto3
import pandas as pd
from io import StringIO
from dotenv import load_dotenv

AWS_ID = os.environ['AWS_ID']
AWS_SECRET = os.environ['AWS_SECRET']

CLIENT = boto3.client('s3', aws_access_key_id=AWS_ID,
        aws_secret_access_key=AWS_SECRET)

BUCKET_NAME = 'mobility-data'



def read_mobility():
    
        object_key = 'dados/country_mobility/2020_BR_Region_Mobility_Report.csv'

        csv_obj = CLIENT.get_object(Bucket=BUCKET_NAME, Key=object_key)
        body = csv_obj['Body']
        csv_string = body.read().decode('utf-8')

        df = pd.read_csv(StringIO(csv_string))

        return df

def read_uti():

        object_key = 'dados/datasus/esus-vepi.LeitoOcupacao.csv'

        csv_obj = CLIENT.get_object(Bucket=BUCKET_NAME, Key=object_key)
        body = csv_obj['Body']
        csv_string = body.read().decode('utf-8')

        df = pd.read_csv(StringIO(csv_string))

        return df

def read_historic():

        object_key = 'dados/datasus/HIST_PAINEL_COVIDBR_07mai2021.csv'

        csv_obj = CLIENT.get_object(Bucket=BUCKET_NAME, Key=object_key)
        body = csv_obj['Body']
        csv_string = body.read().decode('utf-8')

        df = pd.read_csv(StringIO(csv_string))

        return df