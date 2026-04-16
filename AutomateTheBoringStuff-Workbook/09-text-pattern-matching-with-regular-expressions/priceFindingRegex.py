import re 

def get_price(sentence):
    # Regex: \$ matches literal $, \d+ matches one or more digits, 
    # (?:\.\d{2})? matches an optional period and exactly two digits.
    price_regex = r'\$\d+(?:\.\d{2})?'
    
    # re.findall returns all matches as a list of strings
    return re.findall(price_regex, sentence)

if __name__ == "__main__":
    text = 'It was $5.99 but is now on sale for $5.95!!'
    print(get_price(text)) 