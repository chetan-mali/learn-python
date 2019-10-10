"""
SQL Loader Script CBR Data
"""
import pandas as pd
import configparser
import pyodbc as pdb
import json

config = configparser.ConfigParser()
config.read('config.ini')

def cursor():
    print('Connecting to DataBase')
    con = pdb.connect("DRIVER={" + str(config['sql']['driver']) + "};SERVER=" +
                      str(config['sql']['dbserver']) +
                      ";DATABASE=" + str(config['sql']['dbname'])
                      + ";UID=" + str(config['sql']['username']) + ";pwd=" +
                      str(config['sql']['password']))
    cur = con.cursor()
    print('Connection Established')
    #Enabling ExecuteMany option
    cur.fast_executemany = True
    return cur


def get_insert_query(table_name: str, col_list: list):
    placeholders = ','.join(["?"]*len(col_list))
    col_list_str = ','.join(col_list)
    return f'INSERT INTO {table_name}({col_list_str}) values({placeholders})'


def insert_into_sql(file,mapfile,table):
    cur = cursor()
    
    print("Reading file data.....")
    file_data = pd.read_csv(file, iterator=True,
                            chunksize=500, keep_default_na=False, skiprows=0,)
    
    with open(mapfile) as f:
        mapping = json.load(f)
        f.close()
   
    file_col_list = pd.read_csv(
    file, nrows=1, skiprows=0).columns.tolist()
    sql_col_list = [mapping[x] for x in file_col_list]
    
    insert_query = get_insert_query(table_name=table, col_list=sql_col_list)

    print('Starting to insert into DB')
    count = 0
    #Creating tuple list
    for chunk in file_data:
        data = []
        for row in chunk.itertuples(index=False):
            count += 1
            data.append(tuple(row))
        cur.executemany(insert_query, data)
        cur.commit()
        data.clear()
        print(f"{count} rows inserted")
    print('Insertion Complete')

def main():
    insert_into_sql(file = config['file']['cbr'],
                    mapfile=config['mapping']['cbr'],
                    table=config['table']['cbr'])

if __name__ == '__main__':
    main()
