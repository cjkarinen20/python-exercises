

def collatz(number):
    
    if number % 2 == 0: # Number is even.
        print(number // 2, sep = ' ', end = ' ')
        return number // 2
        
    else: # Number is odd.
        print(3 * number + 1, sep = ' ', end = ' ')
        return 3 * number + 1

if __name__ == "__main__":
    
    collatzResult = 0
    
    while True:
        try:
            numInput = int(input("Please enter a number: "))
            # Process user inputted number and convert it to an int.
            break
        except ValueError:
            print("Non-integer detected, please enter an integer value.")
    while collatzResult != 1:
        numInput = collatz(numInput)
        collatzResult = numInput
    
    
