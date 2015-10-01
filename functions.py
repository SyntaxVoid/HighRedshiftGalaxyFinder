###                         ###
# Authored by John Gresl 2015 #
###                         ###


import pyfits
import os
import sys
import matplotlib.pyplot
from math import log10
import numpy



def check_paths(paths):
    # Checks a list of file paths to ensure they are valid.
    if len(paths) == 0:
        raise IndexError('Your list of file paths is empty.')
    for f in paths:
        if not os.path.isfile(f):
            raise os.error('File path does not exist: \'{}\''.format(f))
    return

def check_list_type(l,wanted_type):
    # Checks a list 'l' to see if every item is the correct type.
    if type(l) != list:
        raise TypeError('Expected a list as input. Received: {}'.format(type(l)))
    for n,i in enumerate(l):
        if type(i) != wanted_type:
            raise TypeError('Expected {} as elements of the list. Element index {} is {}'\
                            .format(wanted_type,n,type(i)))
    return

def print_ListOfList(x):
    # Prints a list of lists where every sublist is the same size.
    n1 = len(x)
    n2 = len(x[0])
    for i in range(0,n2):
        for j in range(0,n1):
            sys.stdout.write(" -- {:15s}".format(str(x[j][i])))
        sys.stdout.write(' --\n')
    return

def sign(x):
    # Returns + if x > 0, - if x < 0
    return '+' if x > 0 else '-' if x < 0 else ' '

def fits_add(file_paths, destination, header_index = 0, conversion_factor = 1.0):
    # Adds a list of fits files together, uses the header of file_paths[header_index]
    # and multiplies by the conversion factor if you are converting units
    check_paths(file_paths)
    d_list = [ ]
    for f in file_paths:
        HDU = pyfits.open(f)
        d_list.append(HDU[0].data)
        HDU.close()
    h = pyfits.open(file_paths[header_index])[0].header
    data_sum = sum(d_list) * conversion_factor / len(file_paths)
    pyfits.writeto(destination, data_sum, header = h, clobber = 1)
    return



def cat_add(file_paths, destination):
    #
    master_list = [ ]
    num_fields = 0
    check_paths(file_paths)
    top_comments = ""
    for f in file_paths:
        top_comments = ""
        num_fields = 0
        with open(f,'r') as d:
            data = d.readlines()
            for line in data:
                if line[0] == "#":
                    top_comments += line
                    num_fields += 1
                else:
                    master_list.append(line.split()[1:])
    out_str = "{:10d}  " + "{:10s}  "*(num_fields-1)
    with open(destination,'w') as out_file:
        out_file.write(top_comments)
        for (i,item) in enumerate(master_list):
            out_file.write(out_str.format(i+1,*item))
            out_file.write("\n")
    return


def flux2mag(flux):
    # Returns the magnitude of a flux given in uJy
    return -2.5*log10(flux) + 23.9 if flux > 0 else 99.


def flux_list2mag(flux_list):
    # Returns a list of magnitudes from a list of fluxes
    return [flux2mag(x) for x in flux_list]

def mag_errors(matched_catalog,my_mag_column,public_flux_column,data_start,option = None):
    my_mag = param_get(matched_catalog,[my_mag_column],data_start)[0]
    public_flux = param_get(matched_catalog,[public_flux_column],data_start)[0]
    public_mag = flux_list2mag(public_flux)
    deltas = [ ]
    my_mag_OUT = [ ]
    public_mag_OUT = [ ]
    for a,b in zip(my_mag,public_mag):
        if any([a==99.,b==99.]):
            continue
        else:
            deltas.append(a-b)
            my_mag_OUT.append(a)
            public_mag_OUT.append(b)
    if option == None:
        return deltas
    if 'stats' in option:
        sys.stdout.write("Std: "+str(numpy.std(deltas))+"\n")
        sys.stdout.write("Avg: "+str(numpy.mean(deltas))+"\n")
    if 'plot' in option:
        title = matched_catalog.replace("Matches/Cats/Matched_","")
        title = title.replace(".cat","").upper()
        matplotlib.pyplot.figure()
        matplotlib.pyplot.plot(my_mag_OUT,deltas,'go')
        matplotlib.pyplot.grid(True)
        matplotlib.pyplot.xlabel('My Magnitude')
        matplotlib.pyplot.ylabel('My Magnitude - Public Magnitude')
        matplotlib.pyplot.title(title)
        matplotlib.pyplot.show(block=False)
    return [my_mag_OUT,public_mag_OUT,deltas]


def param_get(in_file, columns, data_begin_line = 1):
    # Opens a catalog file written by SExtractor and returns a list of lists of each of the
    # column numbers in 'columns'. Options is None by default which will not do anything.
    # Currently s
    check_list_type(columns,int)
    p_list = [ ]
    n = len(columns)
    for i in range(0,n):
        p_list.append([])
    with open(in_file) as f:
        data_lines = f.readlines()[data_begin_line-1:]
        for line in data_lines:
            x = line.split()
            for i in range(0,n):
                p_list[i].append(float(x[columns[i]-1]))
    return p_list

def list_operate(x1,x2,operation):
    # Returns a list corresponding to the x1 'operation' x2. (for example, x1 + x2)
    class ListSizeMismatch(Exception):
        pass
    if len(x1) != len(x2):
        raise ListSizeMismatch('List sizes do not match: {} and {}'.format(len(x1),len(x2)))
    acceptable_operations = ['+', '-', '*','/']
    if operation == '+':
        return [a + b for a,b in zip(x1,x2)]
    if operation == '-':
        return [a - b  for a,b in zip(x1,x2)]
    if operation == '*':
        return [a * b for a,b in zip(x1,x2)]
    if operation == '/':
        out_list = [ ]
        for a,b in zip(x1,x2):
            if b == 0 and a != 0:
                out_list.append('{}Inf'.format(sign(a)))
            else:
                out_list.append(a/b)
        return out_list
    raise TypeError('Expected an operation from {}'.format(acceptable_operations))

def plot_mag_errors(mag1, mag2):
    errors = [ ]
    my_mag = [ ]
    for x1,x2 in zip(mag1,mag2):
        if x1 == 99. or x2 == 99.:
            pass
        else:
            errors.append(abs(x1-x2))
            my_mag.append(x1)
    plt.plot(errors,my_mag,'bo')
    plt.grid(True)
    plt.show()

    pass

if __name__ == '__main__':
    pass