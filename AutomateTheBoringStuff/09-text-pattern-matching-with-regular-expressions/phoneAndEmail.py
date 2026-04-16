# You have been given the task of extracting every phone number and email address from a large document.
# The phone number and email extractor will need to do the following:
# -Get the copied text from the clipboard.
# -Find all phone numbers and email addresses in the text.
# -Paste them onto the clipboard.
# The code will do the following:
# -Use the pyperclip module to copy and paste strings.
# -Create two regexes, one for matching phone numbers and one for matching email addresses.
# -Find all matches (not just the first match) of both regexes.
# -Neatly format the matched strings into a single string to paste.
# -Display some kind of message if no matches were found in the text.

import pyperclip, re

phone_re = re.compile(r'''(
    (\d{3}|\(\d{3}\))?  # Area code
    (\s|-|\.)?  # Separator
    (\d{3})  # First three digits
    (\s|-|\.)  # Separator
    (\d{4})  # Last four digits
    (\s*(ext|x|ext\.)\s*(\d{2,5}))?  # Extension
    )''', re.VERBOSE)

# Create email regex.
email_re = re.compile(r'''(
  ❶ [a-zA-Z0-9._%+-]+  # Username
  ❷ @  # @ symbol
  ❸ [a-zA-Z0-9.-]+  # Domain name
    (\.[a-zA-Z]{2,4})  # Dot-something
    )''', re.VERBOSE)

# Find matches in clipboard text.
text = str(pyperclip.paste())

matches = []
for groups in phone_re.findall(text):
    phone_num = '-'.join([groups[1], groups[3], groups[5]])
    if groups[6] != '':
        phone_num += ' x' + groups[6]
    matches.append(phone_num)
for groups in email_re.findall(text):
    matches.append(groups[0])

# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')