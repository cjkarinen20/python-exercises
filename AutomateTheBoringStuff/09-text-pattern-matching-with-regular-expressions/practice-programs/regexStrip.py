import pyperclip, re

text = str(pyperclip.paste())

def regex_strip(text, chars=None):
    if chars is None:
        # match leading or trailing whitespace
        pattern = r'^\s+|\s+$'
    else:
        escaped_chars = re.escape(chars)
        pattern = f'^[{escaped_chars}]+|[{escaped_chars}]+$'
    
    return re.sub(pattern, '', text)

print(f"'{regex_strip(text)}'")