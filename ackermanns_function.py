# ackermanns_function.py
# Exercise Selected: Chapter 12 program 6
# Name of program: Ackermann's Function
# Description of program:  This program uses a version of Ackermann's
#   Function to evaluate how well a computer performs recursion.
import timeit
import sys

def main():
    # Local variables
    act = 'count'
    do = dict(count=do_count, time=do_time, draw=do_draw)
    results = ''
    sys.setrecursionlimit(1500)
    # Display the intro to the user.
    fluffy_intro()

    # todo: write the actual program
    m = get_ack_args('1st')
    n = get_ack_args('2nd')
    ackTime = timed_ack(m, n)

    results = do[act](m, n)
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


def do_time(m, n):
    ackTime = timed_ack(m, n)
    return 'It took {} seconds to run ackermann({}, {})'.format(ackTime, m ,n)


def do_count(m, n):
    ackCount = ackermann(m, n)
    return 'The computation of ackermann({}, {}) is {}.'.format(m, n, ackCount)


def do_draw(m, n):
    return "This isn't implemented yet."


def get_ack_args(arg):
    val = 0
    while True:
        try:
            val = int(input("Please enter the {} argument.\n".format(arg)))
            if val >= 0:
                break
            else:
                raise ValueError
        except ValueError:
            print('Invalid entry.  Please enter a nonnegative integer.')
    return val



def timed_ack(m, n):
    setup = "m ,n = {}, {}; from __main__ import ackermann".format(m, n)
    stmt = """ackermann(m, n)"""
    return timeit.timeit(stmt=stmt, setup=setup, number=1)


#
def ackermann(m, n, s='A({}, {})'):
    s = s.format(m, n) if s == 'A({}, {})' else s
    if m == 0:
        s = s.format(n+1)
    elif n == 0:
        s += s.format("A(m-1, 1))")
    else:
        s += s.format("A(m-1, (A(m, n-1))))")
    print(s)
    return (n + 1) if m == 0 else (ackermann(m - 1, 1, s) if n == 0 else
                                   ackermann(m - 1, ackermann(m, n-1, s), s))


main()