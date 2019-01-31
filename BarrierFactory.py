from decimal import *


def barrier_set1():
    # bset = [(-1.5, 3.6), (0.8, 4.3), (3.1, 7.6)]
    # bset = [ (-5, 9), (-1,4), (1, 4), (5, 9) ]
    # bset = [(-1, 3), (1, 1), (2, 4)]
    # bset = [(-2, 2), (1, 1)]
    # bset = [(-1, 1), (1, 1)]
    # bset = [(-1, 1), (2, 1)]
    # bset = [(-1, 1), (3, 1)]
    # bset = [(-1, 1)]

    # bset = [(-4, 2), (-1, 1), (3, 1)]
    bset = [(-4, 3), (-1, 1), (1, 3), (5, 4)]
    # bset = [(-6, 3), (-1, 1), (1, 3), (9, 7)]
    bset = [(-25, 15), (-4, 5), (-1, 1), (1, 2), (12, 9)]
    # bset = [(-6, 3), (-1, 1), (1, 3), (9, 9)]
    # bset = [(-3, 2), (-1, 1), (1, 2), (3, 5)]

    # for i in range(0, 10):
    #     (px1, py1) = bset[0]
    #     bset.insert(0, (Decimal(px1 - py1), Decimal(1.5) * py1))
    #
    #     (px1, py1) = bset[len(bset)-1]
    #     bset.append((Decimal(px1 + py1), Decimal(1.5) * py1))

    return bset