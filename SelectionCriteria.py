import sys
from libs.jtools import check_list_type
from libs.jastro import flux2mag as f2m

def _float_split(s):
    out = []
    for n in s.split():
        try:
            t = float(n)
        except ValueError:
            t = n
        out.append(t)
    return out
def div(x1,x2):
    try:
        return x1/x2
    except ZeroDivisionError:
        print("Div 0")
        return 0



def b435_dropout(line,MCD):
    x = _float_split(line)
    try:
        if not all([num != 99. for num in [x[MCD["F435W_MAG"]],x[MCD["F606W_MAG"]],x[MCD["F775W_MAG"]],x[MCD["F850L_MAG"]],
                                          x[MCD["F606W_FLUX"]],x[MCD["F606W_FLUXERR"]],
                                          x[MCD["F775W_FLUX"]]/x[MCD["F775W_FLUXERR"]]]]):
            return False
        c1 = (x[MCD["F435W_MAG" ]] - x[MCD["F606W_MAG"]]) > (1.1 + x[MCD["F606W_MAG"]] - x[MCD["F850L_MAG"]])
        c2 = (x[MCD["F435W_MAG" ]] - x[MCD["F606W_MAG"]]) > (1.1)
        c3 = (x[MCD["F606W_MAG" ]] - x[MCD["F850L_MAG"]]) < 1.6
        c4 = div(x[MCD["F606W_FLUX"]],x[MCD["F606W_FLUXERR"]]) > (5.0)
        c5 = div(x[MCD["F775W_FLUX"]],x[MCD["F775W_FLUXERR"]]) > (3.0)
    except KeyError:
        # Means there is no Magnitude entries; only flux. Assuming zp=23.9
        c1 = (f2m(x[MCD["F435W_FLUX"]]) - f2m(x[MCD["F606W_FLUX"]])) \
           > (1.1 + f2m(x[MCD["F606W_FLUX"]]) - f2m(x[MCD["F850L_FLUX"]]))
        c2 = (f2m(x[MCD["F435W_FLUX" ]]) - f2m(x[MCD["F606W_FLUX"]])) \
           > (1.1)
        c3 = (f2m(x[MCD["F606W_FLUX"]]) - f2m(x[MCD["F850L_FLUX"]])) \
           < (1.6)
        c4 = div(x[MCD["F606W_FLUX"]],x[MCD["F606W_FLUXERR"]]) > (5.0)
        c5 = div(x[MCD["F775W_FLUX"]],x[MCD["F775W_FLUXERR"]]) > (3.0)
    return all([c1,c2,c3,c4,c5])




def v606_dropout(line,MCD):
    x = _float_split(line)
    try:
        if not all([num != 99. for num in [x[MCD["F435W_MAG"]],x[MCD["F606W_MAG"]],x[MCD["F775W_MAG"]],x[MCD["F850L_MAG"]],
                                          x[MCD["F850L_FLUX"]],x[MCD["F850L_FLUXERR"]],
                                          x[MCD["F435W_FLUX"]],x[MCD["F435W_FLUXERR"]]]]):
            return False
        c1 = (x[MCD["F606W_MAG" ]] - x[MCD["F775W_MAG"]]) > (1.47 + 0.89*(x[MCD["F775W_MAG"]] - x[MCD["F850L_MAG"]]))
        c2 = (x[MCD["F606W_MAG" ]] - x[MCD["F775W_MAG"]]) > (1.2)
        c3 = (x[MCD["F775W_MAG" ]] - x[MCD["F850L_MAG"]]) < (1.3)
        c4 = div(x[MCD["F850L_FLUX"]],x[MCD["F850L_FLUXERR"]]) > (5.0)
        c5 = (x[MCD["F435W_MAG" ]] - x[MCD["F775W_MAG"]]) > (x[MCD["F606W_MAG"]] - x[MCD["F775W_MAG"]] + 1.0)
    except KeyError:
        c1 = (f2m(x[MCD["F606W_FLUX"]]) - f2m(x[MCD["F775W_FLUX"]])) \
           > (1.47 + 0.89*(f2m(x[MCD["F775W_FLUX"]]) - f2m(x[MCD["F850L_FLUX"]])))
        c2 = (f2m(x[MCD["F606W_FLUX"]]) - f2m(x[MCD["F775W_FLUX"]])) \
           > (1.2)
        c3 = (f2m(x[MCD["F775W_FLUX"]]) - f2m(x[MCD["F850L_FLUX"]])) \
           < (1.3)
        c4 = div(x[MCD["F850L_FLUX"]],x[MCD["F850L_FLUXERR"]]) > (5.0)
        c5 = (f2m(x[MCD["F435W_FLUX"]]) - f2m(x[MCD["F775W_FLUX"]])) \
           > (f2m(x[MCD["F606W_FLUX"]]) - f2m(x[MCD["F775W_FLUX"]]) + 1.0)
    return all([c1,c2,c3,c4,c5])

def i775_dropout(line,MCD):
    x = _float_split(line)
    try:
        if not all([num != 99. for num in [x[MCD["F606W_MAG"]],x[MCD["F775W_MAG"]],x[MCD["F850L_MAG"]],
                                           x[MCD["F850L_FLUX"]],x[MCD["F850L_FLUXERR"]],
                                           x[MCD["F606W_FLUX"]],x[MCD["F606W_FLUXERR"]]]]):
            return False
        c1 = (x[MCD["F775W_MAG" ]] - x[MCD["F850L_MAG"]]) > (1.3)
        c2 = div(x[MCD["F850L_FLUX"]],x[MCD["F850L_FLUXERR"]]) > (5.0)
        c3 = (x[MCD["F606W_MAG"]]-x[MCD["F850L_MAG"]]) > (2.8) # or (x[MCD["F606W_FLUX"]] / x[MCD["F606W_FLUXERR"]]) < (2.0
    except KeyError:
        c1 = (f2m(x[MCD["F775W_FLUX"]]) - f2m(x[MCD["F850L_FLUX"]])) \
           > (1.3)
        c2 = div(x[MCD["F850L_FLUX"]],x[MCD["F850L_FLUXERR"]]) > (5.0)
        c3 = (f2m(x[MCD["F606W_FLUX"]]) - f2m(x[MCD["F850L_FLUX"]])) \
           > (2.8)
    return all([c1,c2,c3])

def z8(line,MCD):
    x = _float_split(line)
    try:
        if not all([num != 99. for num in [x[MCD["F125W_MAG"]],x[MCD["F160W_MAG"]],
                                           x[MCD["F435W_FLUX"]], x[MCD["F435W_FLUXERR"]],
                                           x[MCD["F606W_FLUX"]], x[MCD["F606W_FLUXERR"]],
                                           x[MCD["F775W_FLUX"]], x[MCD["F775W_FLUXERR"]]]]):
            return False
        c1 = (x[MCD["F125W_MAG"]] - x[MCD["F125W_MAG"]]) < (0.45)
        c2 = (x[MCD["F125W_MAG"]] - x[MCD["F160W_MAG"]]) < (0.5)
        c3 = (x[MCD["F125W_MAG"]] - x[MCD["F125W_MAG"]]) > (0.75*(x[MCD["F125W_MAG"]] - x[MCD["F160W_MAG"]]) + 0.525)
        c4 = div(x[MCD["F435W_FLUX"]],x[MCD["F435W_FLUXERR"]]) < (2.0)
        c5 = div(x[MCD["F606W_FLUX"]],x[MCD["F606W_FLUXERR"]]) < (2.0)
        c6 = div(x[MCD["F775W_FLUX"]],x[MCD["F775W_FLUXERR"]]) < (2.0)
        c7 = c6
        c8 = 1 #chi^2(bviI) < 3
    except KeyError:
        c1 = (f2m(x[MCD["F125W_FLUX"]]) - f2m(x[MCD["F125W_FLUX"]])) \
           < (0.45)
        c2 = (f2m(x[MCD["F125W_FLUX"]]) - f2m(x[MCD["F160W_FLUX"]])) \
           < (0.5)
        c3 = (f2m(x[MCD["F125W_FLUX"]]) - f2m(x[MCD["F125W_FLUX"]])) \
           > (0.75*(f2m(x[MCD["F125W_FLUX"]]) - f2m(x[MCD["F160W_FLUX"]])) + 0.525)
        c4 = div(x[MCD["F435W_FLUX"]],x[MCD["F435W_FLUXERR"]]) < (2.0)
        c5 = div(x[MCD["F606W_FLUX"]],x[MCD["F606W_FLUXERR"]]) < (2.0)
        c6 = div(x[MCD["F775W_FLUX"]],x[MCD["F775W_FLUXERR"]]) < (2.0)
        c7 = c6
        c8 = 1 #chi^2(bviI) < 3
    return all([c1,c2,c3,c4,c5,c6,c7,c8])

def z7(line,MCD):
    x = _float_split(line)
    try:
        if not all([num != 99. for num in [x[MCD["F125W_MAG"]],x[MCD["F160W_MAG"]],x[MCD["F775W_MAG"]],x[MCD["F850L_MAG"]],
                                           x[MCD["F435W_FLUX"]], x[MCD["F435W_FLUXERR"]],
                                           x[MCD["F606W_FLUX"]], x[MCD["F606W_FLUXERR"]],
                                           x[MCD["F775W_FLUX"]], x[MCD["F775W_FLUXERR"]]]]):
            return False

        c1 = (x[MCD["F850L_MAG"]] - x[MCD["F125W_MAG"]]) > (0.7)
        c2 = (x[MCD["F125W_MAG"]] - x[MCD["F160W_MAG"]]) < (0.45)
        c3 = (x[MCD["F850L_MAG"]] - x[MCD["F125W_MAG"]]) < (0.8*((x[MCD["F125W_MAG"]] - x[MCD["F160W_MAG"]])) + 1.0)
        c4 = (x[MCD["F775W_MAG"]] - x[MCD["F125W_MAG"]]) > (1.0) or div(x[MCD["F435W_FLUX"]],x[MCD["F435W_FLUXERR"]]) < (1.5)
        c5 = div(x[MCD["F435W_FLUX"]],x[MCD["F435W_FLUXERR"]]) < (2.0)
        c6 = div(x[MCD["F606W_FLUX"]],x[MCD["F606W_FLUXERR"]]) < (2.0)
        c7 = div(x[MCD["F775W_FLUX"]],x[MCD["F775W_FLUXERR"]]) < (2.0)
        c8 = 1 #chi^2(bvi) < 3
    except KeyError:
        c1 = (f2m(x[MCD["F850L_FLUX"]]) - f2m(x[MCD["F125W_FLUX"]])) \
           > (0.7)
        c2 = (f2m(x[MCD["F125W_FLUX"]]) - f2m(x[MCD["F160W_FLUX"]])) \
           < (0.45)
        c3 = (f2m(x[MCD["F850L_FLUX"]]) - f2m(x[MCD["F125W_FLUX"]])) \
           < (0.8*(f2m(x[MCD["F125W_FLUX"]]) - f2m(x[MCD["F160W_FLUX"]])) + 1.0)
        c4 = (f2m(x[MCD["F775W_FLUX"]]) - f2m(x[MCD["F125W_FLUX"]])) \
           > (1.0) \
          or div(x[MCD["F435W_FLUX"]],x[MCD["F435W_FLUXERR"]]) < (1.5)
        c5 = div(x[MCD["F435W_FLUX"]],x[MCD["F435W_FLUXERR"]]) < (2.0)
        c6 = div(x[MCD["F606W_FLUX"]],x[MCD["F606W_FLUXERR"]]) < (2.0)
        c7 = div(x[MCD["F775W_FLUX"]],x[MCD["F775W_FLUXERR"]]) < (2.0)
        c8 = 1 #chi^2(bvi) < 3
    c9 = not z8(line,MCD)
    return all([c1,c2,c3,c4,c5,c6,c7,c8,c9])

def z6(line,MCD):
    # REPLACED y105 date with j125 since they are close
    # REPLACED I814 data with i775 since they are close
    x = _float_split(line)
    try:
        if not all([num != 99. for num in [x[MCD["F125W_MAG"]],x[MCD["F160W_MAG"]],x[MCD["F606W_MAG"]],x[MCD["F775W_MAG"]],
                                           x[MCD["F850L_MAG"]],
                                           x[MCD["F435W_FLUX"]], x[MCD["F435W_FLUXERR"]],
                                           x[MCD["F606W_FLUX"]], x[MCD["F606W_FLUXERR"]],
                                           x[MCD["F775W_FLUX"]], x[MCD["F775W_FLUXERR"]]]]):
            return False
        c1 = (x[MCD["F775W_MAG"]] - x[MCD["F850L_MAG"]]) > (1.0)
        c2 = (x[MCD["F125W_MAG"]] - x[MCD["F160W_MAG"]]) < (1.0)
        c3 = (x[MCD["F775W_MAG"]] - x[MCD["F850L_MAG"]]) > (0.78*(x[MCD["F125W_MAG"]] - x[MCD["F160W_MAG"]]) + 1.2)
        c4 = div(x[MCD["F435W_FLUX"]],x[MCD["F435W_FLUXERR"]]) < (2.0)
        c5 = (x[MCD["F606W_MAG"]] - x[MCD["F850L_MAG"]]) > (2.7) or div(x[MCD["F606W_FLUX"]],x[MCD["F606W_FLUXERR"]]) < (2.0)
    except KeyError:
        c1 = (f2m(x[MCD["F775W_FLUX"]]) - f2m(x[MCD["F850L_FLUX"]])) \
           > (1.0)
        c2 = (f2m(x[MCD["F125W_FLUX"]]) - f2m(x[MCD["F160W_FLUX"]])) \
           < (1.0)
        c3 = (f2m(x[MCD["F775W_FLUX"]]) - f2m(x[MCD["F850L_FLUX"]])) \
           > (0.78*(f2m(x[MCD["F125W_FLUX"]]) - f2m(x[MCD["F160W_FLUX"]])) + 1.2)
        c4 = div(x[MCD["F435W_FLUX"]],x[MCD["F435W_FLUXERR"]]) < (2.0)
        c5 = (f2m(x[MCD["F606W_FLUX"]]) - f2m(x[MCD["F850L_FLUX"]])) \
           > (2.7) \
          or div(x[MCD["F606W_FLUX"]],x[MCD["F606W_FLUXERR"]]) \
           < (2.0)

    c6 = not z7(line,MCD)
    return all([c1,c2,c3,c4,c5,c6])


def z5(line,MCD):
    x = _float_split(line)
    try:
        if not all([num != 99. for num in [x[MCD["F160W_MAG"]],x[MCD["F606W_MAG"]],x[MCD["F775W_MAG"]],x[MCD["F850L_MAG"]],
                                           x[MCD["F435W_FLUX"]],x[MCD["F435W_FLUXERR"]]]]):
            return False
        c1 = (x[MCD["F606W_MAG" ]] - x[MCD["F775W_MAG"]]) > (1.2)
        c2 = (x[MCD["F850L_MAG" ]] - x[MCD["F160W_MAG"]]) < (1.3)
        c3 = (x[MCD["F606W_MAG" ]] - x[MCD["F775W_MAG"]]) > (0.8*(x[MCD["F850L_MAG"]]-x[MCD["F160W_MAG"]]) + 1.2)
        c4 = div(x[MCD["F435W_FLUX"]],x[MCD["F435W_FLUXERR"]]) < (1.0)
    except KeyError:
        c1 = (f2m(x[MCD["F606W_FLUX"]]) - f2m(x[MCD["F775W_FLUX"]])) \
           > (1.2)
        c2 = (f2m(x[MCD["F850L_FLUX"]]) - f2m(x[MCD["F160W_FLUX"]])) \
           < (1.3)
        c3 = (f2m(x[MCD["F606W_FLUX"]]) - f2m(x[MCD["F775W_FLUX"]])) \
           > (0.8*(f2m(x[MCD["F850L_FLUX"]]) - f2m(x[MCD["F160W_FLUX"]])) + 1.2)
        c4 = div(x[MCD["F435W_FLUX"]],x[MCD["F435W_FLUXERR"]]) < (1.0)
    c5 = not z6(line,MCD)
    return all([c1,c2,c3,c4,c5])

def z4(line,MCD):
    x = _float_split(line)
    try:
        if not all([num != 99. for num in [x[MCD["F125W_MAG"]],x[MCD["F435W_MAG"]],x[MCD["F606W_MAG"]],x[MCD["F775W_MAG"]]]]):
            return False
        c1 = (x[MCD["F435W_MAG"]] - x[MCD["F606W_MAG"]]) > (1.0)
        c2 = (x[MCD["F775W_MAG"]] - x[MCD["F125W_MAG"]]) < (1.0)
        c3 = (x[MCD["F435W_MAG"]] - x[MCD["F606W_MAG"]]) > (1.6*(x[MCD["F775W_MAG"]] - x[MCD["F125W_MAG"]]) + 1.0)
    except KeyError:
        c1 = (f2m(x[MCD["F435W_FLUX"]]) - f2m(x[MCD["F606W_FLUX"]])) \
           > (1.0)
        c2 = (f2m(x[MCD["F775W_FLUX"]]) - f2m(x[MCD["F125W_FLUX"]])) \
           < (1.0)
        c3 = (f2m(x[MCD["F435W_FLUX"]]) - f2m(x[MCD["F606W_FLUX"]])) \
           > (1.6*(f2m(x[MCD["F775W_FLUX"]]) - f2m(x[MCD["F125W_FLUX"]])) + 1.0)
    c4 = not z5(line,MCD)
    return all([c1,c2,c3,c4])