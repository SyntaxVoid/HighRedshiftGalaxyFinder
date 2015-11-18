import sys
sys.dont_write_bytecode = True
import pyfits
import numpy
import math

import matplotlib.pyplot

import jtools


def flux2mag(flux, zp=23.9):
    # Returns the magnitude of a flux given in uJy
    return -2.5 * math.log10(flux) + zp if flux > 0. else 99.


def flux_list2mag(flux_list, zp=23.9):
    # Returns a list of magnitudes from a list of fluxes
    return [flux2mag(x, zp) for x in flux_list]


def snr(x):
    # Returns the signal to noise ratio of a given list (x)
    sigma = numpy.mean(x)
    mu = numpy.std(x)
    return sigma/mu


def fits_add(file_paths, destination, header_index=0, conversion_factor=1.0):
    # Adds a list of fits files together, uses the header of file_paths[header_index]
    # and multiplies by the conversion factor if you are converting units
    jtools.check_paths(file_paths)
    d_list = []
    for f in file_paths:
        hdu = pyfits.open(f)
        d_list.append(hdu[0].data)
        hdu.close()
    hfits = pyfits.open(file_paths[header_index])
    h = hfits[0].header
    hfits.close()
    data_sum = sum(d_list) * conversion_factor / len(file_paths)
    pyfits.writeto(destination, data_sum, header=h, clobber=1)
    return

def color_color(data_sets, xaxis, yaxis, title,
                xlim=[-1,4], ylim=[-1,7],
                xthresh=None, ythresh=None, a=None, b=None,
                graphall = 'no'):
    graph_colors = ['go','ro','bo','mo']
    n = len(data_sets)
    matplotlib.pyplot.figure()
    for (n,ds) in enumerate(data_sets):
        for d in ds:
            matplotlib.pyplot.plot(d[0],d[1],graph_colors[n])
            matplotlib.pyplot.xlabel(xaxis)
            matplotlib.pyplot.ylabel(yaxis)
            matplotlib.pyplot.title(title)
            matplotlib.pyplot.grid(True,color = 'black')
            ax = matplotlib.pyplot.gca()
            ax.set_axis_bgcolor('white')
            matplotlib.pyplot.xlim(*xlim)
            matplotlib.pyplot.ylim(*ylim)
    if xthresh is not None and ythresh is not None and a is not None and b is not None:
        matplotlib.pyplot.plot([xthresh,xthresh],[a+b*xthresh,ylim[1]],color='b',linewidth=2)
        matplotlib.pyplot.plot([xlim[0],(ythresh-a)/b],[ythresh,ythresh],color='b',linewidth=2)
        xx = numpy.linspace((ythresh-a)/b,xthresh)
        yy = a + b * xx
        matplotlib.pyplot.plot(xx,yy,color='b',linewidth=2)
    matplotlib.pyplot.show(block = False if graphall=='yes' else True)
    return

def mag_errors(matched_catalog,myF,pubF,data_begin=1,zp=23.9):
    [myF_uJy,pubF_uJy] = param_get(matched_catalog,[myF,pubF],data_begin)
    myM = flux_list2mag(myF_uJy,zp)
    pubM= flux_list2mag(pubF_uJy,zp)
    deltas   = []
    myM_out  = []
    pubM_out = []
    for m,p in zip(myM,pubM):
        if m > 90 or p > 90:
            continue
        else:
            deltas.append(m-p)
            myM_out.append(m)
            pubM_out.append(p)
    return [myM_out,pubM_out,deltas]

def plot_mag_errors(myM,deltas,title="",xlabel="",ylabel=""):
    fig = matplotlib.pyplot.figure()
    matplotlib.pyplot.plot(myM,deltas,'go')
    matplotlib.pyplot.grid(True,color='white')
    matplotlib.pyplot.xlabel(xlabel)
    matplotlib.pyplot.ylabel(ylabel)
    axes = matplotlib.pyplot.gca()
    axes.set_axis_bgcolor('black')
    matplotlib.pyplot.title(title)
    matplotlib.pyplot.show(block=False)
    return


def combine_catalogs(header, cats, columns, data_start, destination, conversion_factor=1):
    # Combines a list of catalogs (cats) row by row and adds the given header
    # at the top of the file, writes the resulting catalog to (destination)
    # RA and DEC MUST be the first two columns, flux and fluxerr MUST be the
    # next two columns. (There should be 4 columns)
    # Change conversion factor to multiple flux and fluxerr by that value. Useful when
    # converting between Jy and uJy
    jtools.check_paths(cats)
    num_entries = 0  # default value in case something goes wrong.
    table = []
    ra_col = columns[0]
    dec_col = columns[1]
    flux_col = columns[2]
    fluxerr_col = columns[3]
    num_params = len(columns) - 2  # We subtract 2 because of the RA/DEC columns we've already accounted for
    for (n, c) in enumerate(cats):
        if n == 0:
            data = param_get(c, [ra_col, dec_col], data_start)
            num_entries = len(data[0])
            for i in range(num_entries):
                table.append([i+1, data[0][i], data[1][i]])
        data = param_get(c, columns[2:], data_start)
        for i in range(num_entries):
            temp = []
            for j in range(num_params):
                temp.append(data[j][i])
            for t in temp:
                table[i].append(t)
            #table[i].append(float(data[0][i])*conversion_factor)
            #table[i].append(float(data[1][i])*conversion_factor)
    jtools.write_table(table, header, destination)
    return


def param_get(in_file, columns, data_begin_line=1):
    # Opens a catalog file written by SExtractor and returns a list of lists of each of the
    # column numbers in 'columns'. Options is None by default which will not do anything.
    jtools.check_list_type(columns, int)
    p_list = []
    n = len(columns)
    for i in range(0, n):
        p_list.append([])
    with open(in_file) as f:
        data_lines = f.readlines()[data_begin_line-1:]
        for line in data_lines:
            x = line.split()
            for i in range(0, n):
                try:
                    p_list[i].append(float(x[columns[i]-1]))
                except:
                    print(x)
    return p_list
