import sys
sys.dont_write_bytecode = True
# The above stops the cluttering of source folder with .pyc files

import functions
import os



if __name__ == '__main__':
    FITS       = False
    CATS       = False
    GRAPH_ERRS = False
    if FITS:
        print('. . .Compiling Fits Images. . .')
        import FitsCompile
        print ('-'*28)


    if CATS:
        print('. . .Compiling Catalogs. . .')
        import CatCompile
        functions.cat_add(['Catalogs/'+ f for f in os.listdir('Catalogs/')],'MASTER.cat')

    if GRAPH_ERRS:
        matched_catalog = ''
        param_column_nums = [ ]
        [my_mags,public_mags] = functions.param_get(matched_catalog,param_column_nums)
        functions.plot_mag_errors(my_mags,public_mags)

        pass