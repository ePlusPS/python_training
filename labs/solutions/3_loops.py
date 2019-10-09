from common import pause, problem

problem(3.1)
'''
    1. Read the "show_vlan.txt" file into your program. Loop through the lines in this file and extract all of
    the VLAN_ID, VLAN_NAME combinations. From these VLAN_ID and VLAN_NAME construct a new list where 
    each element in the list is a tuple consisting of (VLAN_ID, VLAN_NAME). Print this data structure 
    to the screen.
'''
f = open("../resources/show_vlan.txt", 'r')
# print(f.read())
text = f.readlines()
pairs = []
for i in range(2, len(text) ):
    # print( text[i] )
    words = text[i].split()
    if len(words) >= 3:
        pairs.append( ( words[0], words[1] ) )

for i in pairs:
    print(i)


f.close()
pause()

problem(3.2)
'''
    2. Read the contents of the "show_arp.txt" file. Using a for loop, iterate over the lines of this file. 
    Process the lines of the file and separate out the ip_addr and mac_addr for each entry into a separate 
    variable.

    Add a conditional statement that searches for '10.220.88.1'. If 10.220.88.1 is found, print out the string 
    "Default gateway IP/Mac" and the corresponding IP address and MAC Address.

    Using a conditional statement, also search for '10.220.88.30'. If this IP address is found, then print out 
    "Arista3 IP/Mac is" and the corresponding ip_addr and mac_addr.

    Keep track of whether you have found both the Default Gateway and the Arista3 switch. Once you have found 
    both of these devices, 'break' out of the for loop.
'''
f = open("../resources/show_arp.txt", 'r')
text = f.readlines()
found = 0
for i in range(1, len(text)):
    # print(text[i])
    words = text[i].split()
    ip_addr = words[1]
    mac_addr = words[3]
    if ip_addr == '10.220.88.1':
        print("{:<15} {}".format('Default Gateway IP', ip_addr))
        print("{:<15} {}".format('Default Gateway MAC', mac_addr))
        print()
        found += 1
    elif ip_addr == '10.220.88.30':
        print("{:<15} {}".format('Arista3 Gateway IP', ip_addr))
        print("{:<15} {}".format('Arista3 Gateway MAC', mac_addr))
        print()
        found += 1

    if found > 1:
        print("Both targets have been found.")
        print('exiting loop.')
        break

f.close()
pause()

problem(3.3)
'''
    3.  Read the 'show_lldp_neighbors_detail.txt' file. Loop over the lines of this file. Keep reading the 
    lines until you have encountered the remote "System Name" and remote "Port id". Save these two items into 
    variables and print them to the screen. You should extract only the system name and port id from the lines 
    (i.e. your variables should only have 'twb-sf-hpsw1' and '15'). Break out of your loop once you have 
    retrieved these two items.
'''
f = open('../resources/show_lldp_neighbors_detail.txt', 'r')
# print(f.read())
text = f.readlines()
# print(text)
found = 0
sys_name = ""
port_id = ""
for i in text:
    # print( "-"*30)
    if "System Name" in i:
        print(i)
        sys_name = i.split()[len(i.split()) - 1]
        found +=1
    elif "Port id" in i:
        print(i)
        port_id = i.split()[len(i.split()) - 1]
        found +=1
    if found > 1:
        print("Both targets have been found.")
        print('exiting loop.')
        print(sys_name, port_id)
        break

f.close()
pause()

problem(3.4)
'''
    Loop over this data structure and extract all of the MAC addresses. Process all of the MAC addresses to 
    get them into a standard format. Print all of the new standardized MAC address to the screen. The 
    standardized format should be as follows:

    00:62:EC:29:70:FE

    The hex digits should be capitalized. Additionally, there should be a colon between each octet in the MAC 
    address.
'''
arp_table = [('10.220.88.1', '0062.ec29.70fe'),
 ('10.220.88.20', 'c89c.1dea.0eb6'),
 ('10.220.88.21', '1c6a.7aaf.576c'),
 ('10.220.88.28', '5254.aba8.9aea'),
 ('10.220.88.29', '5254.abbe.5b7b'),
 ('10.220.88.30', '5254.ab71.e119'),
 ('10.220.88.32', '5254.abc7.26aa'),
 ('10.220.88.33', '5254.ab3a.8d26'),
 ('10.220.88.35', '5254.abfb.af12'),
 ('10.220.88.37', '0001.00ff.0001'),
 ('10.220.88.38', '0002.00ff.0001'),
 ('10.220.88.39', '6464.9be8.08c8'),
 ('10.220.88.40', '001c.c4bf.826a'),
 ('10.220.88.41', '001b.7873.5634')]

for i in arp_table:
    x = i[1].upper().split('.')
    for j in range(len(x)):
        x[j] = x[j][0:2]+":"+ x[j][2:4]
    x = ":".join(x)
    print(x)
pause()