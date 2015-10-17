import sys
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


def mag_errors(matched_catalog,
               flux_or_mag,
               my_data_column,
               public_flux_column,
               data_start,
               zp=23.9,
               options=None):
    if flux_or_mag == 'flux':
        my_flux_jy = param_get(matched_catalog, [my_data_column], data_start)[0]
        my_flux_ujy = [x * pow(10, 6) for x in my_flux_jy]
        my_mag = flux_list2mag(my_flux_ujy)
    elif flux_or_mag == 'mag':
        my_mag = param_get(matched_catalog, [my_data_column], data_start)[0]
    else:
        raise ValueError('Expected flux_or_mag to be either \'flux\' or \'mag\'')

    public_flux = param_get(matched_catalog, [public_flux_column], data_start)[0]
    public_mag = flux_list2mag(public_flux, zp)

    deltas = []
    my_mag_out = []
    public_mag_out = []

    for a, b in zip(my_mag, public_mag):
        if any([a == 99., b == 99.]):
            continue
        else:
            deltas.append(a-b)
            my_mag_out.append(a)
            public_mag_out.append(b)

    if options is None:
        return [my_mag_out, public_mag_out, deltas]
    if 'stats' in options:
        sys.stdout.write("Std: "+str(numpy.std(deltas))+"\n")
        sys.stdout.write("Avg: "+str(numpy.mean(deltas))+"\n")
    if 'plot' in options:
        title = matched_catalog.replace("Matches/Cats/Matched_", "")
        title = title.replace(".cat", "").upper()
        matplotlib.pyplot.figure()
        matplotlib.pyplot.plot(my_mag_out, deltas, 'go')
        # matplotlib.pyplot.plot(my_mag_out,public_mag_out,'go')
        matplotlib.pyplot.grid(True, color='white')
        matplotlib.pyplot.xlabel('My Magnitude')
        matplotlib.pyplot.ylabel('My Magnitude - Public Magnitude')
        # matplotlib.pyplot.ylabel('Public Magnitude')
        ax = matplotlib.pyplot.gca()
        ax.set_axis_bgcolor('black')
        matplotlib.pyplot.title(title)
        matplotlib.pyplot.show(block=False)
    return [my_mag_out, public_mag_out, deltas]


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
    for (n, c) in enumerate(cats):
        if n == 0:
            data = param_get(c, [ra_col, dec_col], data_start)
            num_entries = len(data[0])
            for i in range(num_entries):
                table.append([i+1, data[0][i], data[1][i]])
        data = param_get(c, [flux_col, fluxerr_col], data_start)
        for i in range(num_entries):
            table[i].append(float(data[0][i])*conversion_factor)
            table[i].append(float(data[1][i])*conversion_factor)
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
                p_list[i].append(float(x[columns[i]-1]))
    return p_list
