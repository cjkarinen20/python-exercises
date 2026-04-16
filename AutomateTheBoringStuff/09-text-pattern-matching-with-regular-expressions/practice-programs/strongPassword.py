import re

def is_strong_password(password):
    # Rule 1: Must be at least eight characters long.
    if len(password) < 8:
        return False
    
    # Rule 2: Contains both uppercase and lowercase characters.
    lower_regex = re.compile(r'[a-z]')
    upper_regex = re.compile(r'[A-Z]')
    
    if not lower_regex.search(password) or not upper_regex.search(password):
        return False
    
    # If all checks pass
    return True