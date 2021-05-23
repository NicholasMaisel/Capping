import connexion
import six
import pandas as pd
import pyodbc
import json

from swagger_server.models.data import Data  # noqa: E501
from swagger_server import util

def connect_db():
    server = '127.0.0.1,1401'
    database = 'MusicAnalysis'
    username = 'SA'
    password = 'Capping12345'
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    return cursor
CURSOR = connect_db()

def query_to_json(query):
    global CURSOR
    # Execute query
    result = CURSOR.execute(query)
    data = []
    for row in result:
        data.append(dict(zip(columns, row)))
    print(data)
    return data#$json.dumps(data)


def pull_data():  # noqa: E501
    """Pulls Data

    Pulls All Base Data # noqa: E501


    :rtype: List[Data]
    """
    return query_to_json("SELECT * FROM Artists")
