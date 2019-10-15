import sys
sys.path.append('/usr/local/lib/python3.7/site-packages')
print(sys.path)

from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from tabulate import tabulate
from universal import printTable, establishConnection, pause

print()

#establish connections to DBs
sessionRFID = establishConnection('_rfid.db')
sessionAsset = establishConnection('_asset.db')

# Show status of DBs
print("RFID Table:")
printTable(sessionRFID, 'rfids')
# pause()

print("Asset Tag Table:")
printTable(sessionAsset, 'assetTags')
# pause()

#stage variables
manID = ''
tag = ''
tagExists = ''
# grab latest entry to RFIDs
targetRFID = sessionRFID.connection().execute("SELECT * FROM 'rfids' ORDER BY ID DESC LIMIT 1")
for i in targetRFID:
    print(i)
    manID = i.manufacturerID
    tagExists = i.asset_tag
# pause()

if tagExists:
    print('The Asset tag has already been assigned\nAborting script...')
    quit()
    
# grab first available asset Tag
targetTag = sessionAsset.connection().execute("SELECT * FROM 'assetTags' WHERE manufacturerID IS NULL LIMIT 1")
for i in targetTag:
    print(i)
    tag = i.assetTag
# pause()

# Update and commit records
sessionRFID.connection().execute("UPDATE rfids SET asset_tag='{}' WHERE manufacturerID='{}'".format(tag, manID))
sessionAsset.connection().execute("UPDATE assetTags SET manufacturerID='{}' WHERE assetTag='{}'".format(manID, tag))
sessionRFID.commit()
sessionAsset.commit()

# Show last time
raw_input('DBs have been updated. press enter to continue')
print("RFID Table:")
printTable(sessionRFID, 'rfids')
# pause()

print("Asset Tag Table:")
printTable(sessionAsset, 'assetTags')
# pause()
