from decimal import *


# used for testing
def barrier_set0():
    # bset = [(-1.5, 3.6), (0.8, 4.3), (3.1, 7.6)]
    # bset = [ (-5, 9), (-1,4), (1, 4), (5, 9) ]
    # bset = [(-1, 3), (1, 1), (2, 4)]
    # bset = [(-2, 2), (1, 1)]
    # bset = [(-1, 1), (1, 1)]
    # bset = [(-1, 1), (2, 1)]
    # bset = [(-1, 1), (3, 1)]
    # bset = [(-1, 1)]

    # bset = [(-4, 2), (-1, 1), (3, 1)]
    # bset = [(-4, 3), (-1, 1), (1, 3), (5, 4)]
    # bset = [(-6, 3), (-1, 1), (1, 3), (9, 7)]
    bset = [(-25, 15), (-4, 5), (-1, 1), (1, 2), (12, 9)]
    # bset = [(-6, 3), (-1, 1), (1, 3), (9, 9)]
    # bset = [(-3, 2), (-1, 1), (1, 2), (3, 5)]
    return bset


# when a 0-interval on one side ends a 3-interval begins on the other side
# this could work, but the barrier height needs to be better chosen
# also optimize the starting/initial barrier placements
def barrier_set1():
    bset = [(-4, 5), (-1, 1), (1, 2)]

    for i in range(0, 5):
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
        bset.append((Decimal(((2 * by0) - by1 + dyn) + dxn), Decimal(Decimal(2.7) * by0)))

        # b side
        (bx1, by1) = bset[0]
        (dxn_1, dyn_1) = bset[len(bset) - 2]
        (dxn, dyn) = bset[len(bset) - 1]
        bset.insert(0, (-Decimal(((2 * dyn) - dyn_1 + by1) - bx1), Decimal(Decimal(2.7) * dyn)))

    print(bset)
    return bset

# 1.922135634621904939515293147