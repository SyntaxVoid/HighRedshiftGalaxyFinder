import pyfits
import os




def check_paths(paths):
    for f in paths:
        if not os.path.isfile(f):
            raise os.error('File path does not exist: \'{}\''.format(f))
    return

def fits_add(file_paths, destination, header_index = 0, conversion_factor = 1.0):
    # Adds a list of fits files together, uses the header of file_paths[header_index]
    # and multiplies by the conversion factor if you are converting units
    check_paths(file_paths)
    d_list = [ ]
    for f in file_paths:
        HDU = pyfits.open(f)
        d_list.append(HDU[0].data)
        h = HDU[0].header
        HDU.close()
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

