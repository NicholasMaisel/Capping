import pyodbc

def connect_db():
    server = '127.0.0.1,1401'
    database = 'MusicAnalysis'
    username = 'SA'
    password = 'Capping12345'
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    return cursor


def query_to_dict(query):
    cursor = connect_db()
    # Execute query
    result = cursor.execute(query)
    columns = [column[0] for column in cursor.description]
    data = []
    for row in result:
        data.append(dict(zip(columns, row)))
    return data
