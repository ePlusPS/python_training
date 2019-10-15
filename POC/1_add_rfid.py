import sys
sys.path.append('/usr/local/lib/python3.7/site-packages')

from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from tabulate import tabulate
from universal import printTable, establishConnection, pause

Base = declarative_base()

class Rfid(Base):
    __tablename__ = "rfids"

    id = Column(Integer, primary_key=True)
    product_name = Column(String)
    location = Column(String)
    manufacturerID = Column(String, unique=True)
    
    def __repr__(self):
        return "----RFID Object----\nProduct: {}\nLocation: {}\nManufacturer ID: {}\n--------------------"\
        .format( self.product_name, self.location, self.manufacturerID)

print('Running addOne.py...\n')

# Connect to the RFID database
session = establishConnection('_rfid.db')

# Fetch existing db
print('RFID Table:')
printTable(session, 'rfids')
# pause()

# Request RFID information from user. This will obviously work differently IRL
newProd = raw_input("Enter Product Name:\n>> ")
newLocation = raw_input("Enter Location:\n>> ")
newMID = raw_input("Enter Manufacturer's ID:\n>> ")

# Create a new row and add it to the DB
newEntry = Rfid(manufacturerID=newMID, product_name=newProd, location=newLocation)
print()
print(newEntry)
print()
# pause()
session.add(newEntry)

# Commit changes to the database
session.commit()

# show DB after changes
printTable(session, 'rfids')
