import re


def strip(phrase,key):
    if key == "":
        # if user press Enter without typing
        string = re.compile(r'^\s*')    # left strip
        new_string = string.sub('',phrase)
        string = re.compile(r'\s*$')    # right strip
        new_string = string.sub('',new_string)
        return new_string
    else:
        # user enters an replace string
        string = re.compile(key)
        new_string = string.sub('',phrase)
        return new_string
        
user = input("Enter a string: ")
replace = input("Enter a string to replace: ")
new = strip(user,replace)
print(new)