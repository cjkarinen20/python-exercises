def spongeCase(text):
    result = []
    use_upper = False
    
    for char in text:
        if char.isalpha(): # If current char is a letter.
            if use_upper:
                result.append(char.upper())
            else:
                result.append(char.lower())
            use_upper = not use_upper # Toggle case for the next letter.
        else:
            # Non-Letters are added as-is and don't toggle the case.
            result.append(char)
            
    return "".join(result)

if __name__ == "__main__":
    user_input = input("Enter your sentence: ")
    print(spongeCase(user_input))
                