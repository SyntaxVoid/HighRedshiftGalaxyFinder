import matplotlib.pyplot as plt




def _histo(z,**kwargs):
    plt.figure()
    if len(kwargs) != 0:
        plt.hist(z, bins = [0,1,2,3,4,5,6,7,8],color='g')
        plt.xlim(0,8)
        plt.title(kwargs["title"])
        plt.xlabel(kwargs["xlabel"])
        plt.ylabel(kwargs["ylabel"])
        plt.grid(True)
    return

def run(title,catalog,red_shift_col):
    xlab = "Redshift"
    ylab = "Number Objects"
    with open(catalog) as cat_data:
        z = [ ]
        cat_lines = cat_data.readlines()
        for obj in cat_lines:
            if obj[0] == "#":
                continue
            z.append(float(obj.split()[red_shift_col]))
    _histo(z,title=title,xlabel=xlab,ylabel=ylab)
    return


if __name__ == '__main__':
    # run("B435-Drops\n(Without RMS Maps)","TestCatalogs/MatchedNONE_b435_Z.cat",36)
    # run("V606-Drops\n(Without RMS Maps)","TestCatalogs/MatchedNONE_v606_Z.cat",36)
    # run("I775-Drops\n(Without RMS Maps)","TestCatalogs/MatchedNONE_i775_Z.cat",36)

    # run("B435-Drops\n(With RMS Maps)","TestCatalogs/MatchedRMS_b435_Z.cat",36)
    # run("V606-Drops\n(With RMS Maps)","TestCatalogs/MatchedRMS_v606_Z.cat",36)
    # run("I775-Drops\n(With RMS Maps)","TestCatalogs/MatchedRMS_i775_Z.cat",36)

    # run("B435-Drops\n(Using Candels Catalogs)","TestCatalogs/MatchedCandels_b435.cat",82)
    # run("V606-Drops\n(Using Candels Catalogs)","TestCatalogs/MatchedCandels_v606.cat",82)
    # run("I775-Drops\n(Using Candels Catalogs)","TestCatalogs/MatchedCandels_i775.cat",82)

    plt.show()
