# ##                         ## #
#  Authored by John Gresl 2015  #
# ##                         ## #

import os
import sys


class ListSizeMismatch(Exception):
        pass


def sign(x):
    # Returns + if x > 0, - if x < 0
    return '+' if x > 0 else '-' if x < 0 else ' '


def check_list_type(lst, wanted_type):
    # Checks a list 'l' to see if every item is the correct type.
    if type(lst) != list:
        raise TypeError('Expected a list as input. Received: {}'.format(type(lst)))
    for n, i in enumerate(lst):
        if type(i) != wanted_type:
            raise TypeError('Expected {} as elements of the list. Element index {} is {}'
                            .format(wanted_type, n, type(i)))
    return


def list_operate(x1, x2, operation):
    # Returns a list corresponding to the x1 'operation' x2. (for example, x1 + x2)
    if len(x1) != len(x2):
        raise ListSizeMismatch('List sizes do not match: {} and {}'.format(len(x1), len(x2)))

    acceptable_operations = ['+', '-', '*', '/']
    if operation == '+':
        return [a + b for a, b in zip(x1, x2)]
    if operation == '-':
        return [a - b for a, b in zip(x1, x2)]
    if operation == '*':
        return [a * b for a, b in zip(x1, x2)]
    if operation == '/':
        out_list = []
        for a, b in zip(x1, x2):
            if b == 0 and a != 0:
                out_list.append('{}Inf'.format(sign(a)))
            else:
                out_list.append(a/b)
        return out_list
    raise TypeError('Expected an operation from {}'.format(acceptable_operations))


def check_paths(paths):
    # Checks a list of file paths to ensure they are valid.
    if len(paths) == 0:
        raise IndexError('Your list of file paths is empty.')
    for f in paths:
        if not os.path.isfile(f):
            raise os.error('File path does not exist: \'{}\''.format(f))
    return


def print_list_of_list(x):
    # Prints a list of lists where every sublist is the same size.
    n1 = len(x)
    n2 = len(x[0])
    for i in range(0, n2):
        for j in range(0, n1):
            sys.stdout.write(" -- {:15s}".format(str(x[j][i])))
        sys.stdout.write(' --\n')
    return


def write_table(table, header, destination):
    with open(destination, 'w') as outfile:
        format_str = "   {:8s}" + "  {:15s}"*(len(table[0])-1)
        outfile.write(header)
        num_lines = len(table)
        for i in range(num_lines):
            outfile.write(format_str.format(*[str(x) for x in table[i]]))
            outfile.write("\n")
    return
