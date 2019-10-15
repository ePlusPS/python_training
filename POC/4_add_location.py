import sys
sys.path.append('/usr/local/lib/python3.7/site-packages')
print(sys.path)

from universal import printTable, establishConnection, pause

print()

session = establishConnection('_rfid.db')

# Show status of DBs
print("RFID Table:")
printTable(session, 'rfids')
# pause()
print("Change location script\n")
mID = raw_input("Enter Manufacturer's ID:\n>> ")
try:
    targetRFID = session.connection().execute("SELECT * FROM 'rfids' WHERE manufacturerID='{}'".format(mID))
    # print(targetRFID)
    found = False
    for i in targetRFID:
        print(i)
        found = True
    
    if not found:
        raw_input('No RFID with that manufacturer ID "{}" was found. Press enter to continue'.format(mID))

    else:

        newLoc = raw_input("Enter new location for device:\n>>")

        session.connection().execute(\
        "UPDATE rfids SET location='{}' WHERE manufacturerID='{}'".format(newLoc, mID))
        session.commit()

        raw_input('DBs have been updated. press enter to continue')
except:
    raw_input("An error has occurred. press enter to continue.")
print("RFID Table:")
printTable(session, 'rfids')
# pause()
