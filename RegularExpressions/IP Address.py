# Since we cannot use 0-255 range in regular expression we divide the same in 3 groups:
#
# 25[0-5] – represents numbers from 250 to 255
# 2[0-4][0-9] – represents numbers from 200 to 249
# [01]?[0-9][0-9]?- represents numbers from 0 to 199

# importing the module
import re

# opening and reading the file
with open('test2.txt') as fh:
    string = fh.readlines()

# declaring the regex pattern for IP addresses
pattern = re.compile('''((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.)
{3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)''')

# initializing the list objects
valid = []
invalid = []

# extracting the IP addresses
for line in string:
    line = line.rstrip()
    result = pattern.search(line)

    # valid IP addresses
    if result:
        valid.append(line)

    # invalid IP addresses
    else:
        invalid.append(line)

# displaying the IP addresses
print("Valid IPs")
print(valid)
print("Invalid IPs")
print(invalid)
