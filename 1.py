# # Problem Statement:  Write a function that takes in a list of names, 
# and verifies that the names are valid names using a regex pattern and match(),
# and prints the name if it is valid, "Invalid name" if the name is not.

# # Use the following list as an argument to test your function.

# # Code Example:

# # names = ["Abraham Lincoln", "Andrew P Garfield", "peter pan", "Connor
#  Milliken", "Jordan Alexander Williams", "Madonna", "programming is cool"]
# Expected Outcome:

# Abraham Lincoln
# Andrew P Garfield
# Invalid name
# Connor Milliken
# Jordan Alexander Williams
# Invalid name

import re

# for name in names:
#     name_match = re.match(r"([A-Z][A-Za-z]+) ?\w ([A-Z]'?[A-Za-z-]+)", name)
#     if name_match:
#         print(name_match.group())
#     else:
#         print('Invalid Name')
  
x ='Abraham Lincoln, Andrew P Garfield, peter pan, Connor Milliken, Jordan Alexander Williams, Madonna, programming is cool'
names = re.split(r', ',  x)
 
def name_check  (names):
    for name in names:
     name_match = re.match(r"([A-Z][A-Za-z]+) ?\w ([A-Z]'?[A-Za-z-]+)", name)
     if name_match:
       print (name_match.group())
     else:
        print('Invalid Name') 
print(name_check(names))
     
