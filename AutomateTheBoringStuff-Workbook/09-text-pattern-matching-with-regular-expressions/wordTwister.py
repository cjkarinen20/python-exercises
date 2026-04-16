import re


if __name__ == "__main__":

    user_input = input("Please enter a sentence to twist: ")    
    pattern = re.compile(r'\b(\w*)(\w)\b')

    print(pattern.sub(r'\2\1', user_input))