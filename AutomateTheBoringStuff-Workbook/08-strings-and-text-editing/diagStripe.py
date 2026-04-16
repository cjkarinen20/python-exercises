import time, sys


def print_diagonal_pattern(size):
    try:
        while True:
            for i in range(size): # Count up to 50 for the increasing 'O' strip.
                print('O' * i + '.' * (size - i))
                time.sleep(0.01)

            for n in range(size, 0, -1): # Count down from 50 for the decreasing 'O' strip.
                print('O' * n + '.' * (size - n))
                time.sleep(0.01)
    except KeyboardInterrupt:
        sys.exit() # Press Ctrl + C to stop the animation.
            
if __name__ == "__main__":
    print_diagonal_pattern(50)
    