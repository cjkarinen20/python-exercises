# October 4th, 2026
# By CJ Karinen
# Inspired by Automate the Boring Stuff Chapter 9
# Description: Finds and collects urls starting with 'http://' and 'https://'.

import pyperclip, re

http_re = re.compile(r'''(

)''', re.VERBOSE)

# Find matches in clipboard text.
text = str(pyperclip.paste())

matches = []
for groups in http_re.findall(text):
    matches.append(groups[0])
    
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')