from common import pause, problem

problem(5.1)
'''
1a. Create an ssh_conn function. This function should have three parameters: ip_addr, username, and password. 
The function should print out each of these three variables and clearly indicate which variable it is 
printing out.

Call this ssh_conn function using entirely positional arguments.

Call this ssh_conn function using entirely named arguments.

Call this ssh_conn function using a mix of positional and named arguments.


1b. Expand on the ssh_conn function from exercise1 except add a fourth parameter 'device_type' with a default 
value of 'cisco_ios'. Print all four of the function variables out as part of the function's execution.

Call the 'ssh_conn2' function both with and without specifying the device_type

Create a dictionary that maps to the function's parameters. Call this ssh_conn2 function using the **kwargs 
technique.
'''
def ssh_conn(ip_addr, username, password, device_type="cisco_ios"):
    print('IP address: ', ip_addr)
    print('Username: ', username)
    print('Password: ', password)
    print('Device Type: ', device_type)
    print()

ssh_conn("10.10.10.10", 'jdoe', '123', 'macbook pro')
ssh_conn(username="cfiggus", password="guest", ip_addr="11.11.11.11")
ssh_conn("22.22.22.22", password='abc123', username='mj')

def ssh_conn2(**kwargs):
    for key in kwargs:
        print("{}: {}".format(key, kwargs[key]))

ssh_conn2(ip_addr='33.33.33.33', username='dkong', password='banana', device_type='mine_cart')

pause()

problem(5.2)
'''
2.  Create a function that randomly generates an IP address for a network. The default base network should be 
'10.10.10.'. For simplicity the network will always be a /24.

You should be able to pass a different base network into your function as an argument.

Randomly pick a number between 1 and 254 for the last octet and return the full IP address.

You can use the following to randomly generate the last octet: 
import random
random.randint(1, 254)

Call your function using no arguments.
Call your function using a positional argument.
Call your function using a named argument.

For each function call print the returned IP address to the screen.

'''
import random
def ip_gen(network="10.10.10."):
    octet = str(random.randint(1,254))
    return(network+octet)

print(ip_gen())
print(ip_gen('9.9.9.'))
print(ip_gen(network="3.4.5."))
pause()

problem(5.3)
'''
3. Similar to lesson3, exercise4 write a function that normalizes a MAC address to the following format:

01:23:45:67:89:AB

This function should handle the lower-case to upper-case conversion.

It should also handle converting from '0000.aaaa.bbbb' and from '00-00-aa-aa-bb-bb' formats.

The function should have one parameter, the mac_address. It should return the normalized MAC address

Single digit bytes should be zero-padded to two digits. In other words, this:

a:b:c:d:e:f

should be converted to:

0A:0B:0C:0D:0E:0F

Write several test cases for your function and verify it is working properly.
'''
import re
def normalize_mac(mac_address):
    
    print()
    print(mac_address)
    mac_address = str(mac_address).upper()

    octet = '[\d\w]{2}'
    short = '[\d\w]:'*5 + '[\d\w]'
    proper = (octet + ':')*5 + octet
    hyphenated = (octet + '-')*5 + octet
    block = '[\d\w]{4}\.'*2 + '[\d\w]{4}'

    if re.search(proper, mac_address):
        print('This is a proper mac address')

    elif re.search(short, mac_address):
        print('converting from shorthand')
        mac_address = mac_address.split(':')
        for i in range(len(mac_address)):
            mac_address[i] = '0' + mac_address[i]
        mac_address = ':'.join(mac_address)

    elif re.search(hyphenated, mac_address):
        print('Converting hyphenated mac address')
        mac_address = mac_address.split('-')
        mac_address = ':'.join(mac_address)

    elif re.search(block, mac_address):
        print('Converting from block format')
        mac_address = mac_address.split('.')
        for i in range(len(mac_address)):
            mac_address[i] = mac_address[i][0:2] + ':' + mac_address[i][2:4]
        mac_address = ':'.join(mac_address)

    else:
        print('this is not a mac address')

    return mac_address

print(normalize_mac('22:f0:pp:90:28:in'))
print(normalize_mac('7:7:7:7:7:7'))
print(normalize_mac('12-23-34-45-56-67'))
print(normalize_mac('1234.2345.3456'))
print(normalize_mac('poop'))
pause()

problem(5.4)
'''
4. Copy your solution from exercise3 to exercise4. Add an 'import pdb' and pdb.set_trace() statement outside of your function (i.e. where you have your function calls).

Inside of pdb, experiment with: 
•	Listing your code.
•	Using 'next' and 'step' to walk through your code. Make sure you understand the difference between next and step.
•	Experiment with 'up' and 'down' to move up and down the code stack.
•	Use p <variable> to inspect a variable.
•	Set a breakpoint and run your code to the breakpoint.
•	Use '!command' to change a variable (for example !new_mac = [])
'''
import pdb
pdb.set_trace()
print(normalize_mac('poop'))
pause()

