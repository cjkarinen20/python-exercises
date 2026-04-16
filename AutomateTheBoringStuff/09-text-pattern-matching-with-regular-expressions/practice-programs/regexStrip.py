import re
def regex_strip(text, chars = None):
    if chars is None:
        # Matches leading/trailing whitespace
        strip_regex = re.compile(r'^\s+|\s+$')
    else:
        # Escapes special character and matches them at start or end.
        escaped_chars = re.escape(chars)
        strip_regex = re.compile(rf'^[{escaped_chars}]+|[{escaped_chars}]+$')
        
    return strip_regex.sub('', text)

if __name__ == "__main__":
    print(f"'{regex_strip('  hello world  ')}'")      # Output: 'hello world'
    print(regex_strip('SpamSpamBaconSpamEggsSpam', 'Spam')) # Output: 'BaconSpamEggs'