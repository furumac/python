import configparser
import csv
import os
import pprint
import sys
import errno
import MySQLdb

TABLE_NAME = 'test_table'
TABLE_COLUMN_COUNT = 2

config = configparser.ConfigParser()
config_path = '../ini/python_db_config.ini'

def main():

    if not os.path.exists(config_path):
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), config_path)

    config.read(config_path, encoding='utf-8') 

    db = config['DEFAULT']['Db']
    user = config['DEFAULT']['User']
    passwd = config['DEFAULT']['Passwd']

    connect = MySQLdb.connect(db=db, user=user, passwd=passwd)
    cursor = connect.cursor()

    cursor.execute(f"DROP TABLE IF EXISTS {TABLE_NAME}")

    print(f"TABLE [{TABLE_NAME}] をDROPしました。")

    cursor.execute(f"create table {TABLE_NAME} (id int(8) PRIMARY KEY, url char(255))")

    print(f"TABLE [{TABLE_NAME}] をCREATEしました。")

    with open('csv/db_insert.csv') as csv:
        for i, line in enumerate(csv):
            list = line.strip().split(',')
            if len(list) != TABLE_COLUMN_COUNT:
                print(f"リストの件数が一致しないのでスキップします: csv {i+1} 行目")
                continue

            id = list[0]
            url = list[1]

            cursor.execute(f"INSERT INTO {TABLE_NAME} (id, url) VALUES ({id}, '{url}')")

            print(f"csv {i+1} 行目をテーブルにINSERTしました。")
    
    cursor.close()
    connect.commit()
    connect.close()
            

if __name__ == '__main__':
    main()