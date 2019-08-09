#allows us to use user input
from cs50 import get_int

#main function for the code
def main():
    #assigns the user input into the letter n
    while True:
        n = get_int("Enter an integer between 1 and 23: ")
        if n == 0:
            return
        elif n >= 1 and n <= 23:
            break

    #iterates from 0 up to user input to determine the number of rows
    for i in range(n):

        #iterates from 0 to n, determining number of columns.
        for j in range(n + 1):

            #prints either a space or a # depending on value of i and j, corresponding
            #to what row and column is active
            if n - (i + j) >= 2:
                print(' ', end='')
            else:
                print('#', end='')

        #moves to next row
        print()

if __name__ == "__main__":
    main()