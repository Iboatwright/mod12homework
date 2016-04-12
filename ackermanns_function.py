# ackermanns_function.py
# Exercise Selected: Chapter 12 program 6
# Name of program: Ackermann's Function
# Description of program:  This program uses a version of Ackermann's
#   Function to evaluate how well a computer performs recursion.


import timeit
import sys

COUNT = 1

def main():
    # Local variables
    m, n = 3, 3

    results = ''
    sys.setrecursionlimit(3500) # 3500 can run 3,8
    # Display the intro to the user.
    fluffy_intro()

    # todo: write the actual
    sup = "m ,n = {}, {}; from __main__ import ack_{{}}".format(m, n)
    case_c = dict(tit='Count', sup=sup.format('c'), stat="""ack_c(m, n)""")
    case_t = dict(tit='Ternary', sup=sup.format('t'), stat="""ack_t(m, n)""")

    run_set = (case_c, case_t)

    for _ in range(1):
        global COUNT
        COUNT = 1
        ret_set = []
        t_comp(ret_set, run_set, 't')
        print(t_rep(ret_set), end='')
        print('Count = {}'.format(COUNT))
    # results = do_time(m, n)
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


def t_rep(ret):
    """ Takes a list of paired (title, results) tuples and
    formats them into a single return string. """
    pr = ''
    for c in ret:
        pr += "Case: {1}{0:^5}{2}\n".format('-', c[0], c[1])
    return pr


def t_comp(ret, cases, t='r'):
    """ ret is a reference pointer to an empty list
    cases is a list of dicts with the timeit args """
    for d in cases:
        if 'num' not in d: d['num'] = 1
        if t == 'r':
            if 'rep' not in d: d['rep'] = 3
            ret.append((
                        d['tit'],
                        timeit.repeat(d['stat'], d['sup'], repeat=d['rep'], number=d['num'])
                      ))
        else:
            ret.append((
                        d['tit'],
                        timeit.timeit(d['stat'], d['sup'], number=d['num'])
                       ))
    return None


def ack_c(m, n):
    global COUNT
    COUNT += 1
    print('m: {}, n: {}, count: {}'.format(m, n, COUNT))
    return (n + 1) if m == 0 else (ack_c(m - 1, 1) if n == 0 else
                                   ack_c(m - 1, ack_c(m, n-1)))


def ack_t(m, n):
    """ Ackermann's Function as a Ternary in the return """
    return (n + 1) if m == 0 else (ack_t(m - 1, 1) if n == 0 else
                                   ack_t(m - 1, ack_t(m, n-1)))


def do_time(m, n):
    ackTime = timed_ack(m, n)
    return 'It took {} seconds to run ackermann({}, {})\n' \
           ' with a recursion depth of {}'.format(ackTime, m ,n, COUNT)


def timed_ack(m, n):
    setup = "m ,n = {}, {}; from __main__ import ackermann".format(m, n)
    stmt = """ackermann(m, n)"""
    return timeit.timeit(stmt=stmt, setup=setup, number=1)






main()
