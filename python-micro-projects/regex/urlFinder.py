# October 4th, 2026
# By CJ Karinen
# Inspired by Automate the Boring Stuff Chapter 9
# Description: Finds and collects urls starting with 'http://' and 'https://'.

import pyperclip, re

url_re = re.compile(r'''(
    (https://|http://) # Protocol
    ([a-zA-Z0-9.]+)? # Sub Domain
    ([a-zA-Z0-9-]+) # Domain 
    (\.[a-zA-Z]{3}) # Top Level Domain
    ([a-zA-Z0-9-=?#&:_/]+)? # Path 
)''', re.VERBOSE)

# Find matches in clipboard text.
text = str(pyperclip.paste())

matches = [] # List of matches
for groups in url_re.findall(text):
    matches.append(groups[0]) # Returns the whole url
    
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches)) 
    # Copies current match to clipboard
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No valid URLs found.')