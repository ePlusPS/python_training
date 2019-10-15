import sqlite3
import sqlalchemy
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from tabulate import tabulate

def printTable(dbSession, table):
    cols = dbSession.connection().execute("PRAGMA table_info({})".format(table))
    headers = []
    for col in cols:
        headers.append(col[1])
    output = []
    rfidList = dbSession.connection().execute("SELECT * FROM {}".format(table))
    for row in rfidList:
        item = []
        for i in range(len(row)):
            item.append(row[i])
        output.append(item)
    print(tabulate(output, headers=headers, tablefmt='rst'))
    print('\n')

def establishConnection(dbName):
    engine = create_engine('sqlite:///databases/{}'.format(dbName))
    Session = sessionmaker()
    Session.configure(bind=engine)
    return Session()


def pause():
    input('Press enter to continue...\n')
