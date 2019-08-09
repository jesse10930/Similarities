#import necessary libraries
import cs50
import sys
from cs50 import get_int
from cs50 import get_string

#get integer input from user
def main():

    if len(sys.argv) != 2:
        print("Enter exactly 1 integer value for k.")
        exit(1)

    #change input integer to a value from 0 to 25
    code_number = int(sys.argv[1]) % 26

    #get a plaintext input from user
    message = get_string("plaintext: ")

    print("ciphertext: ", end='')

    #iterate through characters from plaintext input
    for character in message:

        #if between a and z, encrypt character, and then print
        if character >= 'a' and character <= 'z':
            if ord(character) + code_number <= ord('z'):
                print(chr(ord(character) + code_number), end="")
            else:
                print(chr(ord(character) - (26 - code_number)), end="")

        #if between A and Z, encrypt character, and then print
        elif character >= 'A' and character <= 'Z':
            if ord(character) + code_number <= ord('Z'):
                print(chr(ord(character) + code_number), end="")
            else:
                print(chr(ord(character) - (26 - code_number)), end="")

        #if character not a letter, print original character
        else:
            print(character, end="")

    #print nothing to get to next line
    print("")

if __name__ == "__main__":
    main()