# tool to get the email and phone number
# select the text and copy it to clipboard and run the file
# The founded email and phone Number are copied to clipboard

import re, pyperclip
numReg = re.compile(r'''
        (\d{2}|\(\d{2}\))?      # area code  (optional)
        (\s|-|\.)?              # hypens and gaps  (optional)
        (\d{10,12})''',         # main number
         re.VERBOSE)
emailReg = re.compile(r'''(
        [a-zA-Z0-9._%+-]+      # username
        @                      # keyword
        [a-zA-z0-9]+           # doamin name
        (\.[a-zA-Z]{2,4}))     # dot something
''',re.VERBOSE)
text = str(pyperclip.paste())
matches = []
for group in numReg.findall(text):
    phonenum = ''.join([group[0],group[2]])
    matches.append(phonenum)
for group in emailReg.findall(text):
    matches.append(group[0])
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied')
    print('\n'.join(matches))
else:
    print('No email and phone number found')




