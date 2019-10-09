from common import pause, problem

problem(4.1)
'''
    1. Create a dictionary representing a network device. The dictionary should have key-value pairs 
    representing the 'ip_addr', 'vendor', 'username', and 'password' fields.

    Print out the 'ip_addr' key from the dictionary.

    If the 'vendor' key is 'cisco', then set the 'platform' to 'ios'. If the 'vendor' key is 'juniper', then 
    set the 'platform' to 'junos'.

    Create a second dictionary named 'bgp_fields'. The 'bgp_fields' dictionary should have a keys for 'bgp_as'
    'peer_as', and 'peer_ip'.

    Using the .update() method add all of the 'bgp_fields' dictionary key-value pairs to the network device 
    dictionary.

    Using a for-loop, iterate over the dictionary and print out all of the dictionary keys.

    Using a single for-loop, iterate over the dictionary and print out all of the dictionary keys and values.
'''
device = {
    'ip_addr': '10.32.55.66',
    'vendor': 'juniper',
    'username': 'jdoe1234',
    'password': 'secretpass'
}
print(device['ip_addr'])
if device['vendor'] == 'cisco':
    device['platform'] = 'ios'
elif device['vendor'] == 'juniper':
    device['platform'] = 'junos'

for i in device:
    print("{:<12} {}".format(i + ':', device[i]))
pause()

problem(4.2)
'''
    2. Create three separate lists of IP addresses. The first list should be the IP addresses of the Houston 
    data center routers, and it should have over ten RFC1918 IP addresses in it (including some duplicate IP 
    addresses).

    The second list should be the IP addresses of the Atlanta data center routers, and it should have at least 
    eight RFC1918 IP addresses (including some addresses that overlap with the Houston data center).

    The third list should be the IP addresses of the Chicago data center routers, and it should have at least 
    eight RFC1918 IP addresses. The Chicago IP addresses should have some overlap with both the IP addresses 
    in Houston and Atlanta.

    Convert each of these three lists to a set.

    Using a set operation, find the IP addresses that are duplicated between Houston and Atlanta.

    Using set operations, find the IP addresses that are duplicated in all three sites.

    Using set operations, find the IP addresses that are entirely unique in Chicago.
'''
houston_ips = [
    '10.85.27.10',  #
    '10.85.27.11',
    '10.85.27.12',
    '10.85.27.13',
    '10.85.27.14',
    '10.85.43.83',
    '10.85.27.16',
    '10.85.27.17',
    '10.85.27.18',
    '10.85.43.87'   #
]
atlanta_ips = [
    '10.85.43.78',  #
    '10.85.43.79',
    '10.85.43.80',
    '10.85.43.81',
    '10.85.43.82',
    '10.85.43.83',
    '10.85.43.84',
    '10.85.43.85',
    '10.85.43.86',
    '10.85.43.87'   #
]
chicago_ips = [
    '10.85.43.78',  #
    '10.85.27.10',
    '10.85.20.80',
    '10.85.20.81',
    '10.85.20.82',
    '10.85.20.83',
    '10.85.20.84',
    '10.85.20.85',
    '10.85.43.86',  #
    '10.85.43.87'   #
]
a = set(houston_ips)
b = set(atlanta_ips)
c = set(chicago_ips)
print(a)
print(b)
print(c)
print('\n------------')
print("\nIP's in both Houston and Atlanta:")
print(a.intersection(b))

print("\nIP's in all locations:")
print(a.intersection(b).intersection(c))

print("\nIP's unique to Chicago:")
print(c.difference(b).difference(a))


pause()

problem(4.3)
import re
'''
    3.  Read in the 'show_version.txt' file. From this file, use regular expressions to extract the OS version,
     serial number, and configuration register values.

    Your output should look as follows: 
    OS Version: 15.4(2)T1      
    Serial Number: FTX0000038X    
    Config Register: 0x2102
'''
f = open('../resources/show_version.txt')
# print(f.read())

lines = f.readlines()
for i in range(len(lines)):
    #find lines that have key words
    os_line = re.search('OS', lines[i])
    sn_line = re.search("SN", lines[i])
    conf_line = re.search("Configuration register", lines[i])

    if os_line:
        #find end of version key word. followed immediately by the version number
        v_start = re.search("Version", lines[i]).end()
        #iscolating the version number
        os_version = lines[i][v_start:].split()[0]
        #strip the trailing comma
        os_version = os_version[:len(os_version)-1]

    if sn_line:
        #SN is in a table, find index, skip 2 lines and take entry from later row
        for j in range(len(lines[i].split())):
            if lines[i].split()[j] == "SN":
                col = j
        serial = lines[i+2].split()[col]
        # print("col:", col)
    if conf_line:
        # Last word on this line
        conf_reg = lines[i].split()[-1]


print("OS Version: {}".format(os_version))
print("Serial Number: {}".format(serial))
print("Config Reg: {}".format(conf_reg))

        



f.close()
pause()

problem(4.4)
"""
    4.  Using a named regular expression (?P<name>), extract the model from the below string:
    show_version = '''
        Cisco 881 (MPC8300) processor (revision 1.0) with 236544K/25600K bytes of memory.
        Processor board ID FTX0000038X

        5 FastEthernet interfaces
        1 Virtual Private Network (VPN) Module
        256K bytes of non-volatile configuration memory.
        126000K bytes of ATA CompactFlash (Read/Write)
    '''
    Note that, in this example, '881' is the relevant model. Your regular expression should not, however, 
    include '881' in its search pattern since this number changes across devices.

    Using a named regular expression, also extract the '236544K/25600K' memory string.

    Once again, none of the actual digits of the memory on this device should be used in the regular 
    expression search pattern.

    Print both the model number and the memory string to the screen.

"""
show_version = '''
    Cisco 881 (MPC8300) processor (revision 1.0) with 236544K/25600K bytes of memory.
    Processor board ID FTX0000038X

    5 FastEthernet interfaces
    1 Virtual Private Network (VPN) Module
    256K bytes of non-volatile configuration memory.
    126000K bytes of ATA CompactFlash (Read/Write)
'''

print(show_version)

match = re.search('(?P<model>Cisco \d* \([\d\w]*\)) (?P<filler1>.*) (?P<memory>[\dK\/]*) (?P<filler2>bytes of memory)', show_version)
# print(match)
# print()
print('\nModel: ', match.group('model'))
# print(match.group('filler1'))
print('Memory: ',match.group('memory'))
# print(match.group('filler2'))


pause()

problem(4.5)
'''
    5. Read the 'show_ipv6_intf.txt' file.

    From this file, use Python regular expressions to extract the two IPv6 addresses.

    The two relevant IPv6 addresses you need to extract are: 
        2001:11:2233::a1/24
        2001:cc11:22bb:0:2ec2:60ff:fe4f:feb2/64

    Try to use re.DOTALL flag as part of your search. Your search pattern should not include any of the 
    literal characters in the IPv6 address.

    From this, create a list of IPv6 addresses that includes only the above two addresses.

    Print this list to the screen.
'''
f = open('../resources/show_ipv6_intf.txt')

handler = f.read()
print(handler, '\n-----------------------------\n')

match = re.search('(?P<title>IPv6 address\:)(?P<ips>.*)(?P<rest>IPv6 subnet)', handler, re.DOTALL)
ips_str = match.group('ips')
match = re.search('(?P<first>.*) \[VALID\](?P<second>.*)', ips_str, re.DOTALL)
ip_list = [match.group('first').strip(), match.group('second').strip()]
print('Relevant IPs:')
print(ip_list)

f.close()
pause()
