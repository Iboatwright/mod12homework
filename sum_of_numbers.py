# sum_of_numbers.py
# Exercise Selected: Chapter 12 program 4
# Name of program: Sum of Numbers
# Description of program:  This program demonstrates recursion by having the
#   user enter a positive integer and sums all integers from 1 to that number.
#   It then displays the sum.


def main():
    # Local variables
    end_program = False

    # Display the intro to the user.
    fluffy_intro()

    while end_program not in ['yes','y']:
        # local loop variables
        number_sum = 0

        # Get user input integer
        user_number = get_user_number()

        # Sum integers from 1 to user number
        number_sum = prev_rec_err(user_number)

        # Display the results to the user.
        display_results(user_number, number_sum)
        end_program = go_again()
    else:
        print("Oh, oh, I see, running away then.")
    return None


# Displays an introduction to the program and describes what it does.
def fluffy_intro():
    print('Welcome to the Sum of Numbers program.  This program\n'
          'demonstrates recursion by summing all the integers from 1\n'
          'to some user entered number.  It then displays the results.')
    return None


# Displays the summation results to the user.
def display_results(user_number, number_sum):
    sep = '\n{}\n'.format('-'*79)
    results = 'The sum of all numbers from 1 to {} is: {}'.format(user_number,
                                                                  number_sum)
    print('{0}{1} {0}'.format(sep, results))
    return None


def get_user_number(num=0):
    print('\nPlease enter a positive integer.', end='')
    while True:
        try:
            num = int(input('  >>> '))
            if num > 0:
                break
            else:
                raise ValueError
        except ValueError:
            print('Invalid entry. Try again.')
    return num


# Program loop control variable with validation.
def go_again():
    end_program = input('Do you want to exit the program? yes or (n)o  >>> ')
    while end_program.lower() not in ['yes','y','no','n','']:
        end_program = input('Error: Invalid entry.  Type yes or no.')
    return end_program.lower()


# Prevent RecursionError by breaking user_number into recursive chunks.
def prev_rec_err(i, num=0):
    if i > 900:
        x = i//900
        num = x * sum_number(900)
        i -= x * 900
    num += sum_number(i)
    return num


def sum_number(i):
    return (i + sum_number(i - 1)) if (i - 1) != 0 else i


# Execute the program.
main()