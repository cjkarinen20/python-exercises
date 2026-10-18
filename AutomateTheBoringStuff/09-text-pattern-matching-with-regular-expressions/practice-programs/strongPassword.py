import pyperclip, re

letter_case_re = re.compile(r'[a-zA-Z]+')

digit_re = re.compile(r'\d+')

password = str(pyperclip.paste())

def password_checker(password):
    if len(password) < 8:
        return("A strong password must be at least 8 characters in length.")
    if not re.search(letter_case_re, password):
        return("A strong password must have both uppercase and lowercase letters.")
    if not re.search(digit_re, password):
        return("A strong password must have at least one digit.")
    return("Password is strong!")
message_result = password_checker(password)
print(message_result)