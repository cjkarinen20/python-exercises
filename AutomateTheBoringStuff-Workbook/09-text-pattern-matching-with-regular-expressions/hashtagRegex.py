import re

def get_hashtags(sentence):
    # Followed by one or more alphanumeric characters or underscores.
    hashtag_pattern = r'#\w+'
    # Use findall to return all matches as a list of strings.
    return re.findall(hashtag_pattern, sentence)

def main():
    # Ask the user for input.
    user_input = input("Enter a sentence:\n")
    
    # Get the list of hashtags.
    hashtags = get_hashtags(user_input)
    
    # Print each hashtag found on a new line.
    for tag in hashtags:
        print(tag)
    
if __name__ == "__main__":
    main()