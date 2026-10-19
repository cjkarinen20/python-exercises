# October 4th, 2026
# By CJ Karinen
# Inspired by Automate the Boring Stuff Chapter 9
# Description: Finds text in different date formats (mm/dd/yyyy, mm-dd-yyyy, yyyy/mm/dd, yyyy-mm-dd) and changes
# them to make the format specified by the user.

import pyperclip, re

date_re = re.compile(r'''(
    ([0-9]{2}|[0-9]{4}) # MM or YYYY
    ([/.-]) # Separator 1
    ([0-9]{2}) # DD or MM
    ([/.-]) # Separator 2
    ([0-9]{2}|[0-9]{4}) # YYYY or DD
    )''', re.VERBOSE)

# Find matches in clipboard text.
text = str(pyperclip.paste())

match = re.search(date_re, text)
print(match)

def change_format(date):
    if len(date.group(2)) == 4:
        year = date.group(2)
        month = date.group(4)
        day = date.group(6)
    elif len(date.group(2)) == 2:
        month = date.group(2)
        day = date.group(4)
        year = date.group(6)
    date_reformatted = month + "/" + day + "/" + year
    return date_reformatted

matches = [] # List of matches
for groups in date_re.findall(text):
    matches.append(change_format(match))
    
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches)) 
    # Copies current match to clipboard
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No valid URLs found.')