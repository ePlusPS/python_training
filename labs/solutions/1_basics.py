from common import pause, problem

problem(1.1)
'''
    1. Create a Python script that has three variables: ip_addr1, ip_addr2, ip_addr3, all representing corresponding IP addresses. Print all of them to standard output using a singular print statement
    - Terminal output
    - Variable assignment
'''
ip_addr1 = "1.1.100.41"
ip_addr2 = "1.1.100.93"
ip_addr3 = "1.1.100.52"

print(ip_addr1, ip_addr2, ip_addr3)

pause()

problem(1.2)
'''
    2. Prompt a user to enter an IP address from the command line. Break the IP down into individual octets and print each octet as a decimal, binary and hexadecimal.
    - Taking user input
    - String manipulation
    - Type conversion
'''
ip = input("Please enter a valid IP Address:\n>>> ")

if ip == "":
    ip = '1'

octets = ip.split(".")
for i in octets:
    i = int(i)
    print("Integer: {}".format(i))
    print("Binary: {}".format( bin(i) ))
    print("Hex: {}".format( hex(i) ))
    print('-'*40)

pause()

problem(1.3)
'''
    3. Create 3 variables that represent different ipv6 addresses. Check to see if they equal each other.
    - Comparisons
    - Booleans
'''
print(ip_addr1 == ip_addr2)
print(ip_addr1 == ip_addr3)
print(ip_addr3 == ip_addr2)
print(ip_addr3 == ip_addr3)

pause()

problem(1.4)
'''
    Remove all the excess whitespace. Use the .split() method (of the string class) to extract both the model and serial number. Check to see if the model number contains the word 'cisco' (not case sensitive). Print the model number and serial number to the command line.
    - String manipulation
    - String class methods
'''


show_version = "*0  	  CISCO881-SEC-K9       FTX0000038X    "

show_version = show_version.strip()
# print('|'+ show_version+ '|')
show_version = show_version.split()
# print('|', show_version, '|')

if "cisco" in show_version[1].lower():
    print("cisco product")
else:
    print("not cisco product")

print("Model number: {}".format(show_version[1]))
print("Serial number: {}".format(show_version[2]))

pause()

problem(1.5)
'''
    isolate the IP address and MAC address of each listing and print them to console in an orderly manner (use the .format() method).
    - String manipulation
    - string formatting
'''

mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"

mac1 = mac1.split()
mac2 = mac2.split()
mac3 = mac3.split()
print("IP: {}  |||  MAC: {}".format(mac1[1],mac1[3]))
print("IP: {}  |||  MAC: {}".format(mac2[1],mac2[3]))
print("IP: {}  |||  MAC: {}".format(mac3[1],mac3[3]))

pause()