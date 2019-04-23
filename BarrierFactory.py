from decimal import *
import math


# used for testing
def barrier_set0():
    bset = [(1, 1), (2, 2)]

    for i in range(0,5):
        x, y = bset[len(bset)-1]
        bset.append((Decimal(x + 2 * y), Decimal('2.7') * Decimal(y)))

    return bset


# when a 0-interval on one side ends a 3-interval begins on the other side
# this could work, but the barrier height needs to be better chosen
# also optimize the starting/initial barrier placements
def barrier_set1():
    bset = [(-4, 5), (-1, 1), (1, 2)]

    for i in range(0, 10):
        (bx0, by0) = bset[0]
        (bx1, by1) = bset[1]
        (dxn, dyn) = bset[len(bset) - 1]
        bset.append((Decimal(((2 * by0) - by1 + dyn) + dxn), Decimal(2 * by0 + 1)))

        (bx1, by1) = bset[0]
        (dxn_1, dyn_1) = bset[len(bset) - 2]
        (dxn, dyn) = bset[len(bset) - 1]
        bset.insert(0, (-Decimal(((2 * dyn) - dyn_1 + by1) - bx1), Decimal(2 * dyn + 1)))

    print(bset)
    return bset


# essentially the next barrier to be consumed on the adjacent side will have a 3-interval of size d
# the 0-interval on the current side must be greater than it?!?!
# max qst approx = 1.928571428571428571428571429
# todo : prove this
def barrier_set2():
    bset = [(-4, 5), (-1, 1), (1, 2)]

    for i in range(0, 10):
        # d side
        (bx0, by0) = bset[0]
        (bx1, by1) = bset[1]
        (dxn, dyn) = bset[len(bset) - 1]
        bset.append((Decimal(((2 * by0) - by1 + dyn) + dxn), Decimal(3 * by0 + 1)))

        # b side
        (bx1, by1) = bset[0]
        (dxn_1, dyn_1) = bset[len(bset) - 2]
        (dxn, dyn) = bset[len(bset) - 1]
        bset.insert(0, (-Decimal(((2 * dyn) - dyn_1 + by1) - bx1), Decimal(3 * dyn + 1)))

    print(bset)
    return bset


# max qst aprox = 1.9375 for 4
# 1.922135634621904939515293147 for 2.7
# modified version of bs2, where barriers are 4 times the 3-interval time span
def barrier_set3():
    bset = [(-4, 5), (-1, 1), (1, 2)]

    for i in range(0, 10):
        # d side
        (bx0, by0) = bset[0]
        (bx1, by1) = bset[1]
        (dxn, dyn) = bset[len(bset) - 1]
        bset.append((Decimal(((2 * by0) - by1 + dyn) + dxn), Decimal(Decimal('2.7') * by0)))

        # b side
        (bx1, by1) = bset[0]
        (dxn_1, dyn_1) = bset[len(bset) - 2]
        (dxn, dyn) = bset[len(bset) - 1]
        bset.insert(0, (-Decimal(((2 * dyn) - dyn_1 + by1) - bx1), Decimal(Decimal('2.7') * dyn)))

    print(bset)
    return bset


# 1.919501133786848072562358277
def barrier_set4():
    bset = [(-1, 1), (1, Decimal('1.71'))]
    # bset = [(-3, 5), (-1, 1), (1, Decimal('2.0'))]
    bset.insert(0, (-2*bset[len(bset)-1][1], Decimal('5.4')))

    for i in range(0, 10):
        # d side
        (bx0, by0) = bset[0]
        (bx1, by1) = bset[1]
        (dxn, dyn) = bset[len(bset) - 1]
        # bset.append((Decimal(((2 * by0) - by1 + dyn) + dxn), Decimal(Decimal('2.71828') * by0)))
        # bset.append((Decimal(((2 * by0) + abs(bx0)) - dyn), Decimal(Decimal('2.71828') * by0)))
        bset.append((Decimal(((2 * by0) + abs(bx0))), Decimal(Decimal('3.0') * by0)))

        # b side
        (bx1, by1) = bset[0]
        (dxn_1, dyn_1) = bset[len(bset) - 2]
        (dxn, dyn) = bset[len(bset) - 1]
        # bset.insert(0, (-Decimal(((2 * dyn) + abs(dxn) - abs(by1))), Decimal(Decimal('2.71828') * dyn)))
        bset.insert(0, (-Decimal(((2 * dyn) + abs(dxn))), Decimal(Decimal('3.0') * dyn)))

    print(bset)
    return bset


# Max slope in simulation: 1.909090691376169890151095273, 1.118420935352472970684445554, 1.118420935352472970684445554
def barrier_set5():
    mult = Decimal('3.0')

    bset = [(-6, 9), (-1, 1), (1, Decimal('3.0'))]

    for i in range(0, 10):
        # d side
        (bx0, by0) = bset[0]
        (bx1, by1) = bset[1]
        (dxn, dyn) = bset[len(bset) - 1]
        # bset.append((Decimal(((2 * by0) - by1 + dyn) + dxn), Decimal(Decimal('2.71828') * by0)))
        # bset.append((Decimal(((2 * by0) + abs(bx0)) - dyn), Decimal(Decimal('2.71828') * by0)))
        bset.append((Decimal(((2 * by0) + abs(bx0)) - dyn), Decimal(mult * by0)))

        # b side
        (bx1, by1) = bset[0]
        (dxn_1, dyn_1) = bset[len(bset) - 2]
        (dxn, dyn) = bset[len(bset) - 1]
        # bset.insert(0, (-Decimal(((2 * dyn) + abs(dxn) - abs(by1))), Decimal(Decimal('2.71828') * dyn)))
        bset.insert(0, (-Decimal(((2 * dyn) + abs(dxn) - abs(by1))), Decimal(mult * dyn)))

    print(bset)
    return bset


# Max slope in simulation: 1.899999774198744243949655352, 1.140624834618166422636583344, 1.140624834618166422636583344
def barrier_set6():
    mult = Decimal('3.0')

    # bset = [(-1, 1), (1, Decimal('2.0'))]
    # bset.insert(0, (-2 * bset[len(bset) - 1][1], mult * Decimal('2.0')))
    bset = [(-5, 9), (-1, 1), (1, Decimal('3.0'))]

    for i in range(0, 10):
        # d side
        (bx0, by0) = bset[0]
        (bx1, by1) = bset[1]
        (dxn, dyn) = bset[len(bset) - 1]
        # bset.append((Decimal(((2 * by0) - by1 + dyn) + dxn), Decimal(Decimal('2.71828') * by0)))
        # bset.append((Decimal(((2 * by0) + abs(bx0)) - dyn), Decimal(Decimal('2.71828') * by0)))
        bset.append((Decimal(((2 * by0) + abs(bx0)) - Decimal('2.0') * dyn), Decimal(mult * by0)))

        # b side
        (bx1, by1) = bset[0]
        (dxn_1, dyn_1) = bset[len(bset) - 2]
        (dxn, dyn) = bset[len(bset) - 1]
        # bset.insert(0, (-Decimal(((2 * dyn) + abs(dxn) - abs(by1))), Decimal(Decimal('2.71828') * dyn)))
        bset.insert(0, (-Decimal(((2 * dyn) + abs(dxn) - Decimal('2.0') * abs(by1))), Decimal(mult * dyn)))

    print(bset)
    return bset


# Max slope in simulation: 1.891890110554033432594262029, 1.163633441286720624885688263, 1.163633441286720624885688263
def barrier_set7():
    mult = Decimal('3.0')
    dist_offset_mult = Decimal('2.75')

    # bset = [(-1, 1), (1, Decimal('2.0'))]
    # bset.insert(0, (-2 * bset[len(bset) - 1][1], mult * Decimal('2.0')))
    bset = [(-5, 9), (-1, 1), (1, Decimal('3.0'))]

    for i in range(0, 10):
        # d side
        (bx0, by0) = bset[0]
        (bx1, by1) = bset[1]
        (dxn, dyn) = bset[len(bset) - 1]
        # bset.append((Decimal(((2 * by0) - by1 + dyn) + dxn), Decimal(Decimal('2.71828') * by0)))
        # bset.append((Decimal(((2 * by0) + abs(bx0)) - dyn), Decimal(Decimal('2.71828') * by0)))
        bset.append((Decimal(((2 * by0) + abs(bx0)) - dist_offset_mult * dyn), Decimal(mult * by0)))

        # b side
        (bx1, by1) = bset[0]
        (dxn_1, dyn_1) = bset[len(bset) - 2]
        (dxn, dyn) = bset[len(bset) - 1]
        # bset.insert(0, (-Decimal(((2 * dyn) + abs(dxn) - abs(by1))), Decimal(Decimal('2.71828') * dyn)))
        bset.insert(0, (-Decimal(((2 * dyn) + abs(dxn) - dist_offset_mult * abs(by1))), Decimal(mult * dyn)))

    # print(bset)
    return bset


# Max slope in simulation: 1.891890110554033432594262029, 1.163633441286720624885688263, 1.163633441286720624885688263
# linear loop, create ith barrier using information from previous 2 barriers
def barrier_set7_v2():
    beta = Decimal('3.0')
    alpha = Decimal('2.75')

    bset = [(-1, 1), (1, 3), (-5, 9)]

    for i in range(4, 24):
        (xi_m1, yi_m1) = bset[len(bset) - 1]
        (xi_m2, yi_m2) = bset[len(bset) - 2]
        bset.append((Decimal(((2 * yi_m1) + abs(xi_m1)) - alpha * yi_m2) * ((-1)**i), Decimal(beta * yi_m1)))

    print(bset)
    return bset


def barrier_set8_sol():
    beta = Decimal('3.0')
    alpha = Decimal('2.75')

    mu = (Decimal('2.0') + Decimal(math.sqrt(Decimal('5.0')))) / Decimal(math.sqrt(Decimal('5.0')))

    a1 = Decimal('1.0')
    s = Decimal('1.0')

    b1 = s * Decimal(math.pow(2.0 + math.sqrt(5.0), 2))
    d1 = s * Decimal(math.pow(2.0 + math.sqrt(5.0), 3))

    c1 = (mu - 2) * d1 + (2*s) + b1

    a2 = 2*d1 + c1 - a1 - b1
    b2 = s * Decimal(math.pow(2.0 + math.sqrt(5.0), 4))

    bset = [(-a1, b1), (c1, d1), (-a2, b2)]

    for i in range(4, 24):
        (xi_m1, yi_m1) = bset[len(bset) - 1]
        (xi_m2, yi_m2) = bset[len(bset) - 2]
        bset.append((Decimal(((2 * yi_m1) + abs(xi_m1)) - alpha * yi_m2) * ((-1)**i), Decimal(beta * yi_m1)))

    # print(bset)
    return bset


def barrier_set_sol():
    mu = (Decimal('2.0') + Decimal(math.sqrt(Decimal('5.0')))) / Decimal(math.sqrt(Decimal('5.0')))

    a1 = Decimal('1.0')
    s = Decimal('1.0')

    b1 = s * Decimal(math.pow(2.0 + math.sqrt(5.0), 2))
    d1 = s * Decimal(math.pow(2.0 + math.sqrt(5.0), 3))

    c1 = (mu - 2) * d1 + (2*s) + b1

    a2 = 2*d1 + c1 - a1 - b1
    b2 = s * Decimal(math.pow(2.0 + math.sqrt(5.0), 4))

    bset = [(-a2, b2), (-a1, b1), (c1, d1)]
    i = 2

    for j in range(0, 10):
        (bx0, by0) = bset[0]
        (bx1, by1) = bset[1]
        (dxn, dyn) = bset[len(bset) - 1]
        bset.append((Decimal(((2 * by0) - dyn) + dxn), Decimal(s * Decimal(math.pow(Decimal('2.0') + Decimal(math.sqrt(Decimal('5.0'))), (2 * i) + 1)))))

        i += 1

        (bx1, by1) = bset[0]
        (dxn_1, dyn_1) = bset[len(bset) - 2]
        (dxn, dyn) = bset[len(bset) - 1]
        bset.insert(0, (-Decimal(((2 * dyn) - by1) - bx1),
                     Decimal(s * Decimal(math.pow(Decimal('2.0') + Decimal(math.sqrt(Decimal('5.0'))), 2*i)))))

    print(bset)
    return bset