import sys
from libs.jtools import check_list_type


def _real_values(v):
    # Returns true if all values in (v) have a |value| < 99.
    for i in v:
        if abs(i) == 99.:
            return False
    return True

def b435_dropout(b435,v606,i775,z850,SNv606,SNi775):
    # From Stark et. al.
    if not _real_values([b435,v606,i775,z850,SNv606,SNi775]):
        return False
    c1 = (b435 - v606) > (1.1 + v606 - z850)
    c2 = (b435 - v606) > (1.1)
    c3 = (v606 - z850) < 1.6
    c4 = SNv606 > 5
    c5 = SNi775 > 3
    return all([c1,c2,c3,c4,c5])


def v606_dropout(b435,v606,i775,z850,SNz850,SNb435):
    # From Stark et. al.
    if not _real_values([b435,v606,i775,z850,SNz850,SNb435]):
        return False
    c1 = ((v606 - i775) > (1.47 + 0.89*(i775 - z850))) or (v606 - i775)  > 2
    c2 = (v606 - i775) > (1.2)
    c3 = (i775 - z850) < (1.3)
    c4 = (SNz850) > (5)
    c5 = (b435 - i775) > (v606 - i775 + 1) or  ((SNb435) < 2)
    return all([c1,c2,c3,c4,c5])


def i775_dropout(v606,i775,z850,SNz850,SNv606, identifier = None):
    # From Stark et. al.
    if not _real_values([v606,i775,z850,SNz850,SNv606]):
        return False
    c1 = (i775 - z850) > (1.3)
    c2 = (SNz850) > (5)
    c3 = ((SNv606) < 2) or ((v606-z850) > (2.8))
    return all([c1,c2,c3])


def z4(j125,b435,v606,i775):
    #From Bouwen et. al.
    c1 = b435-v606 > 1
    c2 = i775 - j125 < 1
    c3 = b435-v606 > 1.6*(i775-j125) + 1
    c4 = 1 #Not in z ~ 5 selection

    return all([c1,c2,c3,c4])

def z5(h160,v606,i775,z850,SNb435):
    #From Bouwen et. al.
    c1 = v606-i775 > 1.2
    c2 = z850-h160 < 1.3
    c3 = v606-i775 > 0.8*(z850-h160) + 1.2

    c4 = SNb435 < 1

    c5 = 1 #Not in z ~ 6 selection

    return all([c1,c2,c3,c4,c5])

def z6(y105,j125,h160,v606,i775,i814,z850,SNb435,SNv606,SNi814):
    #From Bouwen et. al.
    c1 = i775-z850 > 1
    c2 = y105-h160 < 1
    c3 = i775-z850 > 0.78*(y105-h160)+1.2

    c4 = SNb435 < 2
    c5 = (v606-z850  > 2.7) or (SNv606 < 2)

    c6 = 1 #Not in z ~ 7 selection

    return all([c1,c2,c3,c4,c5,c6])

def z7(y105,j125,h160,i814,z850,SNb435,SNv606,SNi775,SNi814):
    #From Bouwen et. al.
    c1 = z850-y105 > 0.7
    c2 = j125-h160 < 0.45
    c3 = z850 - y105 < 0.8*(j125-h160) + 1.0
    c4 = (i814 - j125 > 1.0) or (SNi814 < 1.5)

    c5 = SNb435 < 2
    c6 = SNv606 < 2
    c7 = SNi775 < 2
    c8 = 1 #chi^2(bvi) < 3

    c9 = 1 #not in z ~ 8 selection

    return all([c1,c2,c3,c4,c5,c6,c7,c8,c9])

def z8(y105,j125,h160,SNb435,SNv606,SNi775,SNi814):
    #From Bouwen et. al.
    c1 = y105 - j125 < 0.45
    c2 = j125 - h160 < 0.5
    c3 = y105 - j125 > 0.75*(j125-h160) + 0.525

    c4 = SNb435 < 2
    c5 = SNv606 < 2
    c6 = SNi775 < 2
    c7 = SNi814 < 2
    c8 = 1 #chi^2(bviI) < 3

    return all([c1,c2,c3,c4,c5,c6,c7,c8])