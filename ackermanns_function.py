# ackermanns_function.py
# Exercise Selected: Chapter 12 program 6
# Name of program: Ackermann's Function
# Description of program:  This program uses a version of Ackermann's
#   Function to evaluate how well a computer performs recursion.


def main():
    # Local variables
    results = ''

    # Display the intro to the user.
    fluffy_intro()

    # todo: write the actual program

    # Display the results to the user.
    display_results(results)
    return None


# Displays an introduction to the program and describes what it does.
def fluffy_intro():
    print('Welcome to .')
    return None


# Displays the summation results to the user.
def display_results(results):
    sep = '\n\n{}\n\n'.format('-'*79)
    print('{0}{1} {0}'
          ''.format(sep, results))
    return None