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
sessionPID = establishConnection('_pid.db')

# Show status of DBs
print("RFID Table:")
printTable(sessionRFID, 'rfids')
# pause()

print("Company PID Table:")
printTable(sessionPID, 'pids')
# pause()

#stage variables
product = ''
pid = ''
singleID = ''

# grab latest entry to RFIDs
targetRFID = sessionRFID.connection().execute("SELECT * FROM 'rfids' ORDER BY ID DESC LIMIT 1")
for i in targetRFID:
    print(i)
    product = i.product_name
    singleID = i.id
# pause()

# grab corresponding PID
targetPID = sessionPID.connection().execute(\
"SELECT * FROM 'pids' WHERE product_name='{}' LIMIT 1".format(product))

for i in targetPID:
    print(i)
    pid = i.company_pid
# pause()

# Update and commit records
sessionRFID.connection().execute(\
"UPDATE rfids SET pid='{}' WHERE id='{}'".format(pid, singleID))
# sessionPID.connection().execute(\
# "UPDATE pids SET product_name='{}' WHERE company_pid='{}'".format(product, pid))
sessionRFID.commit()
# sessionPID.commit()

# Show last time
raw_input('DBs have been updated. press enter to continue')
print("RFID Table:")
printTable(sessionRFID, 'rfids')
# pause()

# print("PID Table:")
# printTable(sessionPID, 'pids')
# pause()
