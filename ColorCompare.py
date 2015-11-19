from GLOBALS import *
from libs.jastro import flux2mag as f2m
import matplotlib.pyplot as plt


def _plot(*args,**kwargs):
    assert len(args) % 2 == 0
    for i in range(0,len(args),2):
        x = args[i]
        y = args[i+1]
        plt.figure()
        plt.plot(x,y,'ro')
        plt.title(kwargs["title"])
        plt.xlabel(kwargs["xlab"])
        plt.ylabel(kwargs["ylab"])
        plt.xlim(15,28)
        plt.ylim(-4,4)
        plt.grid(True)
    return



def run(matched_catalog,title):
    with open(matched_catalog) as cat_data:
        cat_lines = cat_data.readlines()
        x_ax =  [ ]  # H-Band magnitudes
        y_ax1 = [ ] # Color differences (V-I)
        y_ax2 = [ ] # Color differences (I-Z)
        for obj in cat_lines:
            if obj[0] == "#":
                continue
            myVI_color = float(obj.split()[MASTER_COL_DICT["F606W_MAG"]]) \
                        -float(obj.split()[MASTER_COL_DICT["F775W_MAG"]])
            candelsVI_color = f2m(float(MASTER_CANDELS_DICT["F606W_FLUX"])) \
                             -f2m(float(MASTER_CANDELS_DICT["F775W_FLUX"]))

            myIZ_color = float(obj.split()[MASTER_COL_DICT["F775W_MAG"]]) \
                        -float(obj.split()[MASTER_COL_DICT["F850L_MAG"]])
            candelsIZ_color = f2m(float(MASTER_CANDELS_DICT["F775W_FLUX"])) \
                             -f2m(float(MASTER_CANDELS_DICT["F850L_FLUX"]))

            h_mag = float(obj.split()[MASTER_COL_DICT["F160W_MAG"]])
            cd1   = myVI_color-candelsVI_color
            cd2   = myIZ_color-candelsIZ_color
            if abs(h_mag) > 35 or abs(cd1) > 35 or abs(cd2) > 35:
                continue
            x_ax.append(h_mag)
            y_ax1.append(cd1)
            y_ax2.append(cd2)
        _plot(x_ax,y_ax1,title=title,xlab="H-band Magnitude",ylab="My Colors - Candels Colors\n(V-I)")
        _plot(x_ax,y_ax2,title=title,xlab="H-band Magnitude",ylab="My Colors - Candels Colors\n(I-Z)")
    return




if __name__ == '__main__':
    run("TestCatalogs/MatchedNONE.cat","Color-Color Comparison \n(Without RMS Maps)")
    run("TestCatalogs/MatchedRMS.cat","Color-Color Comparison \n(With RMS Maps)")
    plt.show()
    pass