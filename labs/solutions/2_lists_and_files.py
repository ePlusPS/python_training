from common import pause, problem

problem(2.1)
'''
    1. Open the "show_version.txt" file for reading. Use the .read() method to read in the entire file 
    contents to a variable. Print out the file contents to the screen. Also print out the type of the variable 
    (you should have a string at this point).

    Close the file.

    Open the file a second time using a Python context manager (with statement). Read in the file contents 
    using the .readlines() method. Print out the file contents to the screen. Also print out the type of the 
    variable (you should have a list at this point).
    - File handling and reading
'''
# Entire file as a string
f = open("../resources/show_version.txt")
fulltext = f.read()
print(fulltext)
print("\nStored as a {}\n".format(type(fulltext)))
f.close()
pause()

# Breaking file down line by line
f = open("../resources/show_version.txt")
fulltext = f.readlines()
for i in fulltext:
    print(i)
print("\nStored as a {}\n".format(type(fulltext)))
f.close()
pause()

problem(2.2)
'''
    Use the .append() method to add an IP address onto the end of the list. Use the .extend() method to add 
    two more IP addresses to the end of the list. Use list concatenation to add two more IP addresses to the 
    end of the list.

    Print out the entire list of IP addresses. Print out the first IP address in the list. Print out the last 
    IP address in the list.

    Using the .pop() method to remove the first IP address in the list and the last IP address in the list.

    Update the new first IP address in the list to be '2.2.2.2'. Print out the new first IP address in the 
    list.

    Verify the contents of your list by printing the entire list.

    - Lists
    - Manipulating lists
    - Using list methods
'''

#first part
my_ipaddress = ['192.168.1.1', '10.1.1.1', '172.16.31.254', '8.8.8.8', '8.8.4.4']
print('original state:\n')
print(my_ipaddress)
print('\nappend')
my_ipaddress.append('153.32.64.21')
print(my_ipaddress)
print('\nextend')
my_ipaddress.extend(['10.32.69.41', '10.32.69.45'])
print(my_ipaddress)
print('\nconcat')
my_ipaddress = my_ipaddress + ['1.1.1.1', '4.4.4.4']
print(my_ipaddress)

#second part
print(my_ipaddress[0])
print(my_ipaddress[len(my_ipaddress) - 1])

#third part
print('\npopping first and last\n')
print(my_ipaddress.pop(0))
print(my_ipaddress.pop())
print(my_ipaddress)

#fourth
print("\nInserting at front\n")
my_ipaddress.insert(0, '2.2.2.2')
print(my_ipaddress[0])
print(my_ipaddress)

pause()

problem(2.3)
'''
    3. Read in the "show_arp.txt" file using the readlines() method. Use a list slice to remove the header line.

    Use pretty print to print out the resulting list to the screen, syntax is: 
    from pprint import pprint
    pprint(some_var)

    Use the list .sort() method to sort the list based on IP addresses.

    Create a new list slice that is only the first three ARP entries.

    Use the .join() method to join these first three ARP entries back together as a single string using the newline character ('\n') as the separator.

    Write this string containing the three ARP entries out to a file named "arp_entries.txt".

    - Reading files
    - Writing files
'''
from pprint import pprint
f = open('../resources/show_arp.txt')
lines = f.readlines()
f.close()
temp = slice(1,len(lines))
lines = lines[temp]
pprint(lines)
pause()
lines.sort()
pprint(lines)
new_lines = lines[0:3]
new_lines = "".join(new_lines)
o = open('../resources/arp_entries.txt', 'w')
o.write(new_lines)
o.close()

pause()

problem(2.4)
'''
    4. Read the 'show_ip_bgp_summ.txt' file into your program. From this BGP output obtain the first and last lines of the output.

    From the first line use the string .split() method to obtain the local AS number.

    From the last line use the string .split() method to obtain the BGP peer IP address.

    Print both local AS number and the BGP peer IP address to the screen.
'''

f = open("../resources/show_ip_bgp_summ.txt")
# print(f.read())
lines = f.readlines()
first = lines[0]
last = lines[len(lines) - 1]
as_num = first.split()[7]
bgp = last.split()[0]
print()
print(first + last)
print()
print("{:<15} {}".format("AS Number:",as_num))
print("{:<15} {}".format("BGP Peer IP:",bgp))

f.close()

pause()