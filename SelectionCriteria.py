import sys
from libs.jtools import check_list_type
from GLOBALS import MASTER_COL_DICT as MCD


def _real_values(v):
    # Returns true if all values in (v) have a |value| < 99.
    for i in v:
        if abs(i) == 99.:
            return False
    return True


def b435_dropout(line):
    x = line.split()
    if not all([num != 99. for num in [x[MCD["F435W_MAG"]],x[MCD["F606w_MAG"]],x[MCD["F775W_MAG"]],x[MCD["F850L_MAG"]],
                                      x[MCD["F606W_FLUX"]],x[MCD["F606W_FLUXERR"]],
                                      x[MCD["F775W_FLUX"]]/x[MCD["F775W_FLUXERR"]]]]):
        return False
    c1 = (x[MCD["F435W_MAG" ]] - x[MCD["F606W_MAG"]]) > (1.1 + x[MCD["F606W_MAG"]] - x[MCD["F850L_MAG"]])
    c2 = (x[MCD["F435W_MAG" ]] - x[MCD["F606W_MAG"]]) > (1.1)
    c3 = (x[MCD["F606W_MAG" ]] - x[MCD["F850L_MAG"]]) < 1.6
    c4 = (x[MCD["F606W_FLUX"]] / x[MCD["F606W_FLUXERR"]]) > (5.0)
    c5 = (x[MCD["F775W_FLUX"]] / x[MCD["F775W_FLUXERR"]]) > (3.0)
    return all([c1,c2,c3,c4,c5])

def v606_dropout(line):
    x = line.split()
    if not all([num != 99. for num in [x[MCD["F435W_MAG"]],x[MCD["F606W_MAG"]],x[MCD["F775W_MAG"]],x[MCD["F850L_MAG"]],
                                      x[MCD["F850L_FLUX"]],x[MCD["F850L_FLUXERR"]],
                                      x[MCD["F435W_FLUX"]],x[MCD["F435W_FLUXERR"]]]]):
        return False
    c1 = (x[MCD["F606W_MAG" ]] - x[MCD["F775W_MAG"]]) > (1.47 + 0.89*(x[MCD["F775W_MAG"]] - x[MCD["F850L_MAG"]]))
    c2 = (x[MCD["F606W_MAG" ]] - x[MCD["F775W_MAG"]]) > (1.2)
    c3 = (x[MCD["F775W_MAG" ]] - x[MCD["F850L_MAG"]]) < (1.3)
    c4 = (x[MCD["F850L_FLUX"]] / x[MCD["F850L_FLUXERR"]]) > (5.0)
    c5 = (x[MCD["F435W_MAG" ]] - x[MCD["F775W_MAG"]]) > (x[MCD["F606W_MAG"]] - x[MCD["F775W_MAG"]] + 1.0)
    return all([c1,c2,c3,c4,c5])

def i775_dropout(line):
    x = line.split()
    if not all([num != 99. for num in [x[MCD["F606W_MAG"]],x[MCD["F775W_MAG"]],x[MCD["F850L_MAG"]],
                                       x[MCD["F850L_FLUX"]],x[MCD["F850L_FLUXERR"]],
                                       x[MCD["F606W_FLUX"]],x[MCD["F606W_FLUXERR"]]]]):
        return False
    c1 = (x[MCD["F775W_MAG" ]] - x[MCD["F850L_MAG"]]) > (1.3)
    c2 = (x[MCD["F850L_FLUX"]] / x[MCD["F850L_FLUXERR"]]) > (5.0)
    c3 = (x[MCD["F606W_FLUX"]] / x[MCD["F606W_FLUXERR"]]) < (2.0) or (x[MCD["F606W_MAG"]]-x[MCD["F850L_MAG"]]) > (2.8)
    return all([c1,c2,c3])

def z4(line):
    x = line.split()
    if not all([num != 99. for num in [x[MCD["F125W_MAG"]],x[MCD["F435W_MAG"]],x[MCD["F606W_MAG"]],x[MCD["F775W_MAG"]]]]):
        return False
    c1 = (x[MCD["F435W_MAG"]] - x[MCD["F606W_MAG"]]) > (1.0)
    c2 = (x[MCD["F775W_MAG"]] - x[MCD["F125W_MAG"]]) < (1.0)
    c3 = (x[BCD["F435W_MAG"]] - x[MCD["F606W_MAG"]]) > (1.6*(x[MCD["F775W_MAG"]] - x[MCD["F125W_MAG"]]) + 1.0)
    c4 = not z5(line)
    return all([c1,c2,c3,c4])

def z5(line):
    x = line.split()
    if not all([num != 99. for num in [x[MCD["F160W_MAG"]],x[MCD["F606W_MAG"]],x[MCD["F775W_MAG"]],x[MCD["F850L_MAG"]],
                                       x[MCD["F435W_FLUX"]],x[MCD["F435W_FLUXERR"]]]]):
        return False
    c1 = (x[MCD["F606W_MAG" ]] - x[MCD["F775W_MAG"]]) > (1.2)
    c2 = (x[MCD["F850L_MAG" ]] - x[MCD["F160W_MAG"]]) < (1.3)
    c3 = (x[MCD["F606W_MAG" ]] - x[MCD["F775W_MAG"]]) > (0.8*(x[MCD["F850L_MAG"]]-x[MCD["F160W_MAG"]]) + 1.2)
    c4 = (x[MCD["F435W_FLUX"]] / x[MCD["F435W_FLUXERR"]]) < (1.0)
    c5 = not z6(line)
    return all([c1,c2,c3,c4,c5])

def z6(line):
    # REPLACED y105 date with j125 since they are close
    # REPLACED I814 data with i775 since they are close
    x = line.split()
    if not all([num != 99. for num in [x[MCD["F125W_MAG"]],x[MCD["F160W_MAG"]],x[MCD["F606W_MAG"]],x[MCD["F775W_MAG"]],
                                       x[MCD["F850L_MAG"]],
                                       x[MCD["F435W_FLUX"]], x[MCD["F435W_FLUXERR"]],
                                       x[MCD["F606W_FLUX"]], x[MCD["F606W_FLUXERR"]],
                                       x[MCD["F775W_FLUX"]], x[MCD["F775W_FLUXERR"]]]]):
        return False
    c1 = (x[MCD["F775W_MAG"]] - x[MCD["F850L_MAG"]]) > (1.0)
    c2 = (x[MCD["F125W_MAG"]] - x[MCD["F160W_MAG"]]) < (1.0)
    c3 = (x[MCD["F775W_MAG"]] - x[MCD["F850L_MAG"]]) > (0.78*(x[MCD["F125W_MAG"]] - x[MCD["F160W_MAG"]]) + 1.2)
    c4 = (x[MCD["F435W_FLUX"]]/x[MCD["F435W_FLUXERR"]]) < (2.0)
    c5 = (x[MCD["F606W_MAG"]] - x[MCD["F850L_MAG"]]) > (2.7) or (x[MCD["F606W_FLUX"]]/x[MCD["F606W_FLUXERR"]]) < (2.0)
    c6 = not z7(line)
    return all([c1,c2,c3,c4,c5,c6])

def z7(line):
    x = line.split()
    if not all([num != 99. for num in [x[MCD["F125W_MAG"]],x[MCD["F160W_MAG"]],x[MCD["F775W_MAG"]],x[MCD["F850L_MAG"]],
                                       x[MCD["F435W_FLUX"]], x[MCD["F435W_FLUXERR"]],
                                       x[MCD["F606W_FLUX"]], x[MCD["F606W_FLUXERR"]],
                                       x[MCD["F775W_FLUX"]], x[MCD["F775W_FLUXERR"]]]]):
        return False

    c1 = (x[MCD["F850L_MAG"]] - x[MCD["F125W_MAG"]]) > (0.7)
    c2 = (x[MCD["F125W_MAG"]] - x[MCD["F160W_MAG"]]) < (0.45)
    c3 = (x[MCD["F850L_MAG"]] - x[MCD["F125W_MAG"]]) < (0.8*((x[MCD["F125W_MAG"]] - x[MCD["F160W_MAG"]])) + 1.0)
    c4 = (x[MCD["F775W_MAG"]] - x[MCD["F125W_MAG"]]) > (1.0) or (x[MCD["F435W_FLUX"]]/x[MCD["F435W_FLUXERR"]]) < (1.5)
    c5 = (x[MCD["F435W_FLUX"]]/x[MCD["F435W_FLUXERR"]]) < (2.0)
    c6 = (x[MCD["F606W_FLUX"]]/x[MCD["F606W_FLUXERR"]]) < (2.0)
    c7 = (x[MCD["F775W_FLUX"]]/x[MCD["F775W_FLUXERR"]]) < (2.0)
    c8 = 1 #chi^2(bvi) < 3
    c9 = not z8(line)
    return all([c1,c2,c3,c4,c5,c6,c7,c8,c9])

def z8(line):
    x = line.split()
    if not all([num != 99. for num in [x[MCD["F125W_MAG"]],x[MCD["F160W_MAG"]],
                                       x[MCD["F435W_FLUX"]], x[MCD["F435W_FLUXERR"]],
                                       x[MCD["F606W_FLUX"]], x[MCD["F606W_FLUXERR"]],
                                       x[MCD["F775W_FLUX"]], x[MCD["F775W_FLUXERR"]]]]):
        return False
    c1 = (x[MCD["F125W_MAG"]] - x[MCD["F125W_MAG"]]) < (0.45)
    c2 = (x[MCD["F125W_MAG"]] - x[MCD["F160W_MAG"]]) < (0.5)
    c3 = (x[MCD["F125W_MAG"]] - x[MCD["F125W_MAG"]]) > (0.75*(x[MCD["F125W_MAG"]] - x[MCD["F160W_MAG"]]) + 0.525)
    c4 = (x[MCD["F435W_FLUX"]]/x[MCD["F435W_FLUXERR"]]) < (2.0)
    c5 = (x[MCD["F606W_FLUX"]]/x[MCD["F606W_FLUXERR"]]) < (2.0)
    c6 = (x[MCD["F775W_FLUX"]]/x[MCD["F775W_FLUXERR"]]) < (2.0)
    c7 = c6
    c8 = 1 #chi^2(bviI) < 3
    return all([c1,c2,c3,c4,c5,c6,c7,c8])
