import sys
sys.path.append('/usr/local/lib/python3.7/site-packages')
print(sys.path)

import sqlite3
import sqlalchemy
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from tabulate import tabulate


print(sqlalchemy.__version__)

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

def setRfidDB():
    engine = create_engine('sqlite:///databases/_rfid.db', echo=True)
    Base = declarative_base()

    class Rfid(Base):
        __tablename__ = "rfids"

        id = Column(Integer, primary_key=True)
        product_name = Column(String)
        location = Column(String)
        manufacturerID = Column(String, unique=True)
        pid = Column(String)
        asset_tag = Column(String)
        
        def __repr__(self):
            return "({})-------------------\nProduct: {}\nLocation: {}\nManufacturer ID: {}".format(self.id, self.product_name, self.location, self.manufacturerID)

    # rfids = Table('rfids', Base.metadata,)

    Base.metadata.create_all(engine)

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    try:
        print("*********************************\n")
        newRfid = Rfid(product_name='Catalyst 9000', location='Milpitas Lab', manufacturerID='c4t92341', pid='780th20')
        session.add_all([
            Rfid(product_name='Catalyst 9000', location='San Diego Office', manufacturerID='c4t93400', pid='780th20', asset_tag = '4990'),
            Rfid(product_name='Cloud Service Router 1000V', location='Austin Lab', manufacturerID='csr378943',asset_tag='5003'),
            Rfid(product_name='Cloud Service Router 1000V', location='Saratoga Lab', manufacturerID='csr238421'),
            Rfid(product_name='UCS C125 Rack Server', location='Fremont', manufacturerID='UCS67328912')
        ])
        print('Setting RFID Values!!!!!!!!!!!!')
        session.add(newRfid)
        print('Success Setting RFID Values!!!!!!!!!!!!')
        session.commit()
        print(newRfid)

        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        # print(session.query(Rfid))
        # print(Rfid.__table__)
        hello = session.query(Rfid).order_by(Rfid.product_name)
    except:
        print("\ncould not seed DB\n")
        session.rollback()

    printTable(session, 'rfids')

def setPidDB():
    engine = create_engine('sqlite:///databases/_pid.db')
    Base = declarative_base()

    
    class Pid(Base):
        __tablename__ = "pids"

        id = Column(Integer, primary_key=True)
        product_name = Column(String)
        company_pid = Column(String, unique=True)
        
        def __repr__(self):
            return "({})-------------------\nuManufacturer ID: {}\nPID:{}".format(self.id, self.product_name, self.company_pid)

    Base.metadata.create_all(engine)

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    
    try:
        print("*********************************\n")
        newPid = Pid(product_name='Ikea Table', company_pid='1k8230r')
        session.add_all([
            Pid(product_name='Catalyst 9000', company_pid='780th20'),
            Pid(product_name='Cloud Service Router 1000V', company_pid='nu230p65'),
            Pid(product_name='UCS C125 Rack Server', company_pid='d4652yt'),
            Pid(product_name='test', company_pid='n0pa4t5'),
            Pid(company_pid='fb1d10000'),
            Pid(company_pid='fb1d10001'),
            Pid(company_pid='fb1d10002'),
            Pid(company_pid='fb1d10003'),
            Pid(company_pid='fb1d10004'),
            Pid(company_pid='fb1d10005'),
            Pid(company_pid='fb1d10076'),
            Pid(company_pid='fb1d10406'),
            Pid(company_pid='fb1d10008'),
            Pid(company_pid='fb1d10009'),
            Pid(company_pid='fb1d10067'),
            Pid(company_pid='fb1d10034'),
            Pid(company_pid='fb1d10060'),
            Pid(company_pid='fb1d10032'),
            Pid(company_pid='fb1d1000i'),
            Pid(company_pid='fb1d100pp'),
        ])
        session.add(newPid)
        session.commit()
        print(newPid)

        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        # print(session.query(Pid))
        # print(Pid.__table__)
        hello = session.query(Pid).order_by(Pid.product_name)
        print(hello)
    except:
        print("\ncould not seed DB\n")
        session.rollback()

    printTable(session, 'pids')


def setAssetDB():
    engine = create_engine('sqlite:///databases/_asset.db')
    Base = declarative_base()

    
    class AssetTag(Base):
        __tablename__ = "assetTags"

        id = Column(Integer, primary_key=True)
        assetTag = Column(String, unique=True)
        manufacturerID = Column(String)
        
        def __repr__(self):
            return "({})-------------------\nuAsset Tag #: {}\nManufacturer ID:{}".format(self.id, self.assetTag, self.manufacturerID)

    Base.metadata.create_all(engine)

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    
    try:
        print("*********************************\n")
        session.add_all([
            AssetTag(assetTag='4990', manufacturerID='c4t93400'), AssetTag(assetTag='5003', manufacturerID='csr378943'),
            AssetTag(assetTag='5016'),
            AssetTag(assetTag='5029'), AssetTag(assetTag='5042'), AssetTag(assetTag='5055'),
            AssetTag(assetTag='5068'), AssetTag(assetTag='5081'), AssetTag(assetTag='5094'),
            AssetTag(assetTag='5107'), AssetTag(assetTag='5120'), AssetTag(assetTag='5133'),
            AssetTag(assetTag='5146'), AssetTag(assetTag='5159'), AssetTag(assetTag='5172'),
            AssetTag(assetTag='5185'), AssetTag(assetTag='5198'), AssetTag(assetTag='5211'),
            AssetTag(assetTag='5124'), AssetTag(assetTag='5137'), AssetTag(assetTag='5140'),
            AssetTag(assetTag='5153'), AssetTag(assetTag='5166'), AssetTag(assetTag='5179')
        ])
        session.commit()
        print(newAssetTag)

        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        # print(session.query(AssetTag))
        # print(AssetTag.__table__)
        hello = session.query(AssetTag).order_by(AssetTag.assetTag)
        print(hello)
    except:
        print("\ncould not seed DB\n")
        session.rollback()

    printTable(session, 'assetTags')

setRfidDB()
setPidDB()
setAssetDB()
# setTablesLite()
print("done.")
