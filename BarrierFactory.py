from decimal import *


class BarrierFactory:

    def __init__(self):
        pass

    def get_set(self, id):
        if id == 1:
            return barrier_set1()


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
    # bset = [(-4, 3), (-1, 1), (1, 3), (5, 4)]
    # bset = [(-6, 3), (-1, 1), (1, 3), (9, 7)]
    bset = [(-25, 15), (-4, 5), (-1, 1), (1, 2), (12, 9)]
    # bset = [(-6, 3), (-1, 1), (1, 3), (9, 9)]
    # bset = [(-3, 2), (-1, 1), (1, 2), (3, 5)]
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