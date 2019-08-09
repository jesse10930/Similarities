import cs50
from cs50 import get_int

def main():

    #get credit card number from user and check it is an integer greater than 0
    while True:
        card_number = get_int("Enter Credit Card Number: ")
        if type(card_number) == int and card_number > 0:
            break

    #multiply every other digit by 2 (backward from second to last), and sum digits
    counter = 10
    first_sum = 0
    while card_number // counter > 0:
        buffer_sum = (((card_number // counter) % 10) * 2)
        if buffer_sum < 10:
            first_sum = first_sum + buffer_sum
        else:
            first_sum = first_sum + (buffer_sum - 9)
        counter = counter * 100

    #sum all digits not involved above
    counter = 1
    second_sum = 0
    while card_number // counter > 0:
        second_sum = second_sum + ((card_number // counter) % 10)
        counter = counter * 100

    #sum the two sums
    real_sum = first_sum + second_sum

    #check the brand of the credit card, if the number passes the algorithm above
    if real_sum % 10 == 0:
        if 340000000000000 <= card_number and card_number <= 349999999999999:
            print("AMEX")
        elif 370000000000000 <= card_number and card_number <= 379999999999999:
            print("AMEX")
        elif 5100000000000000 <= card_number and card_number <= 5599999999999999:
            print("MASTERCARD")
        elif 4000000000000 <= card_number and card_number <= 4999999999999:
            print("VISA")
        elif 4000000000000000 <= card_number and card_number <= 4999999999999999:
            print("VISA")
        else:
            print("INVALID")
    else:
        print("INVALID")

if __name__ == "__main__":
    main()