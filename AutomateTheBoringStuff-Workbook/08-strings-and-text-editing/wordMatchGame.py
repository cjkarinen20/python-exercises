import random

def get_word_hint(secret_word, guess_word):
    
    secret_word = secret_word.lower()
    guess_word = guess_word.lower()
    
    hintStr = ""
    for index1, char1 in enumerate(secret_word):
        
        if char1 == guess_word[index1]:
            hintStr += 'O'
        elif char1 in guess_word:
            hintStr += 'o'
        else:
            hintStr += 'x'
    
    return hintStr

def choose_random_word():
    
    wordDict = 'MITTS FLOAT BRICK LIKED DWARF COMMA GNASH ROOMS UNITE BEARS SPOOL ARMOR'.split()
    
    randNumIndex = random.randint(0, len(wordDict) - 1)
    
    randomNum = wordDict[randNumIndex]
    
    return randomNum

def get_guess_word(secret_word, attempts):
    
    while True: # Retrieve and validate user guess
        
        if attempts == 6: # Display prompt on first guess.
            userGuess = input("Guess the secret five-letter word: ")
            
        elif attempts < 6: # Display attempt count on subsequent guesses.
            userGuess = input(f"{attempts} guesses remaining:")
        
        if not isinstance(userGuess, str): # Guess contains numbers or symbols
            print("Error: Input must be a five-letter word (No numbers or symbols).")
        
        if len(userGuess) > 5:
            print("Error: Guess cannot be more than five letters.")
        
        else:
            break
    
    return userGuess

def game_manager():
    
    # Assign the secret word.
    secret_word = choose_random_word()
    secret_word = secret_word
    
    # Start gameplay loop and display win/loss messages
    attempts = 6
    
    while attempts > 0:
        guess_word = get_guess_word(secret_word, attempts)
        guess_word = guess_word
        hint_str = get_word_hint(secret_word, guess_word)
        print(hint_str + "\n")
        
        if hint_str == 'OOOOO': # User guessed correctly.
            print("You guessed the secret word!")
        
        else:
            attempts -= 1
    # The user ran out of guesses.
    print(f"The secret word was {secret_word}. Try again!")       

if __name__ == "__main__":
    
    game_manager()