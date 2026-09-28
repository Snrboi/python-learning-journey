def countdown(number):

    if number == 0:
        print("Finished")
        return

    print(number)

    countdown(number - 1)


countdown(3) # This prints 3, 2, 1, finished

# exercise 2
def count_up(number):

    if number == 5:
        return

    print(number)

    count_up(number + 1) # the bug is here as the base case has the recussion stop at 5 and with -1 it never gets to 5


count_up(1)

# exercise 3
def print_numbers(number):

    if number == 0:
        print('Done')
        return
    print(number)

    print_numbers(number - 1)

print_numbers(4)