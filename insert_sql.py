import configparser
import csv
import os
import pprint
import sys
import errno
import MySQLdb

TABLE_NAME = 'test_table'
TABLE_COLUMN_COUNT = 2  # INSERT時に指定するカラム数

config = configparser.ConfigParser()
config_path = '../ini/python_db_config.ini'
input_csv_path = 'csv/db_insert.csv'


def config_read():
    config.read(config_path, encoding='utf-8') 


def connect_db():
    db = config['DEFAULT']['Db']
    user = config['DEFAULT']['User']
    passwd = config['DEFAULT']['Passwd']

    if not os.path.exists(config_path):
        raise FileNotFoundError(
            errno.ENOENT, os.strerror(errno.ENOENT), config_path)

    connect = MySQLdb.connect(db=db, user=user, passwd=passwd)
    cursor = connect.cursor()
    return connect, cursor

def drop_table(cursor):
    cursor.execute(f"DROP TABLE IF EXISTS {TABLE_NAME}")
    print(f"TABLE [{TABLE_NAME}] をDROPしました。")


def create_table(cursor):
    cursor.execute(f"create table {TABLE_NAME} (id int(8) PRIMARY KEY, url char(255))")
    print(f"TABLE [{TABLE_NAME}] をCREATEしました。")


def insert_db_from_csv(cursor):
    with open(input_csv_path) as csv:
        for i, line in enumerate(csv):
            list = line.strip().split(',')
            
            # カンマ区切りの数がINSERTでセットするカラム数に一致しているか
            if len(list) != TABLE_COLUMN_COUNT:
                print(f"リストの件数が一致しないのでスキップします: csv {i+1} 行目")
                continue

            id = list[0]
            url = list[1]

            # SQL実行
            cursor.execute(f"INSERT INTO {TABLE_NAME} (id, url) VALUES ({id}, '{url}')")
            print(f"csv {i+1} 行目をテーブルにINSERTしました。")


def close_db(connect, cursor):
    cursor.close()
    connect.commit()
    connect.close()


def main():

    config_read()

    connect, cursor = connect_db()

    # INSERT前にDROPする必要がなければコメントアウトしておく
    drop_table(cursor)

    create_table(cursor)

    insert_db_from_csv(cursor)

    close_db(connect, cursor)


if __name__ == '__main__':
    main()