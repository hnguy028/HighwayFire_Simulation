from decimal import *
from BarrierFactory import *

##
#   Used for verification of consumption functions
#   Assumptions :
#   A0 : Barriers are of increasing length
#   A1 : Distance between a barrier and its preceding barrier is at least the distance of the previous barrier's length
#   A2 : The length of a barrier is at least twice the length of the previous barrier
##


# With assumption A0, A1
def f_v1(i, t):
    ci, di = pi = barriers[i]
    ci_m1, di_m1 = pi_m1 = barriers[i-1]
    ci_m2, di_m2 = pi_m2 = barriers[i-2]

    if di_m1 >= Decimal(2.0) * di_m2:
        if ci_m1 + di_m2 < t <= ci_m1 + Decimal(2.0) * di_m2:
            return Decimal(3.0) * (t - (ci_m1 + di_m2))
        elif ci_m1 + Decimal(2.0) * di_m2 <= t <= ci_m1 + di_m1:
            return Decimal(3.0) * di_m2 + (t - (ci_m1 + Decimal(2.0) * di_m2))
        elif ci_m1 + di_m1 <= t <= ci_m1 + Decimal(2.0) * di_m1:
            return Decimal(3.0) * di_m2 + di_m1 - Decimal(2.0) * di_m2
        elif ci_m1 + Decimal(2.0) * di_m1 <= t <= ci + di_m1:
            return Decimal(3.0) * di_m2 + di_m1 - Decimal(2.0) * di_m2 + t - (ci_m1 + Decimal(2.0) * di_m1)
        else:
            return Decimal(3.0) * di_m2 + di_m1 - Decimal(2.0) * di_m2 + (ci - ci_m1 - di_m1) + f_v1(i+1, t)
    else:
        if ci_m1 + di_m2 < t <= ci_m1 + di_m1:
            return Decimal(3.0) * (t - (ci_m1 + di_m2))
        elif ci_m1 + di_m1 <= t <= ci_m1 + Decimal(2.0) * di_m2:
            return Decimal(3.0) * (di_m1 - di_m2) + Decimal(2.0) * (t - (ci_m1 + Decimal(2.0) * di_m1))
        elif ci_m1 + Decimal(2.0) * di_m2 <= t <= ci_m1 + Decimal(2.0) * di_m1:
            return Decimal(3.0) * (di_m1 - di_m2) + Decimal(2.0) * (di_m1 - Decimal(2.0) * (di_m1 - di_m2))
        elif ci_m1 + Decimal(2.0) * di_m1 <= t <= ci + di_m1:
            return Decimal(3.0) * (di_m1 - di_m2) + Decimal(2.0) * (di_m1 - Decimal(2.0) * (di_m1 - di_m2)) + (t - (ci_m1 + Decimal(2.0) * di_m1))
        else:
            return Decimal(3.0) * (di_m1 - di_m2) + Decimal(2.0) * (di_m1 - Decimal(2.0) * (di_m1 - di_m2)) + (ci - ci_m1 - di_m1) + f_v1(i+1, t)


# Base case for f_v1
def f_v1_0(t):
    # distance to the top of the first barrier
    c1, d1 = b1 = barriers[index_b0 + 1]
    c2, d2 = b2 = barriers[index_b0 + 2]
    if t <= c1 + d1:
        return t
    elif t <= c1 + Decimal(2.0) * d1:
        return c1 + d1
    elif t <= c2 + d1:
        return c1 + d1 + (t - (c1 + Decimal(2.0) * d1))
    else:
        # time to get to the top of the first barrier plus recursive call
        return c1 + d1 + (c2 - c1 - d1) + f_v1(index_b0 + 3, t)


def f_v2(i, t):
    ci, di = pi = barriers[i]
    ci_m1, di_m1 = pi_m1 = barriers[i-1]

    if ci - ci_m1 <= di_m1:
        if ci_m1 + di_m1 < t <= ci + di_m1:
            return 0
        elif t <= ci_m1 + Decimal(2.0) * di_m1:
            return Decimal(2.0) * (t - (ci + di_m1))
        elif t <= ci + Decimal(2.0) * di_m1:
            return Decimal(2.0) * (di_m1 - (ci - ci_m1)) + Decimal(3.0) * (t - (ci_m1 + Decimal(2.0) * di_m1))
        elif t <= ci + di:
            return Decimal(2.0) * (di_m1 - (ci - ci_m1)) + Decimal(3.0) * (ci - ci_m1 + di_m1) + (t - (ci + Decimal(2.0) * di_m1))
        else:
            return Decimal(2.0) * (di_m1 - (ci - ci_m1)) + Decimal(3.0) * (ci - ci_m1 + di_m1) + (di - Decimal(2.0) * di_m1) + f_v2(i + 1, t)
    else:
        if ci_m1 + di_m1 < t <= ci_m1 + Decimal(2.0) * di_m1:
            return 0
        elif t <= ci + di_m1:
            return t - (ci_m1 + Decimal(2.0) * di_m1)
        elif t <= ci + Decimal(2.0) * di_m1:
            return ci - ci_m1 - di_m1 + Decimal(3.0) * (t - (ci + di_m1))
        elif t <= ci + di:
            return ci - ci_m1 - di_m1 + Decimal(3.0) * di_m1 + (t - (ci + Decimal(2.0) * di_m1))
        else:
            return ci - ci_m1 - di_m1 + Decimal(3.0) * di_m1 + (di - Decimal(2.0) * di_m1) + f_v2(i + 1, t)


def f_v2_0(t):
    # distance to the top of the first barrier
    c1, d1 = b1 = barriers[index_b0 + 1]
    if t <= c1 + d1:
        return t
    else:
        # time to get to the top of the first barrier plus recursive call
        return c1 + d1 + f_v2(index_b0 + 2, t)


def f_slope(i=2):
    # sort by left and right

    # calculate variables
    # i = 1

    _, dim2 = barriers_pos[i-2]
    _, dim1 = barriers_pos[i-1]
    _, di = barriers_pos[i]

    _, bim1 = barriers_neg[i-1]
    _, bi = barriers_neg[i]

    dim1 = Decimal(dim1)
    di = Decimal(di)

    bim1 = Decimal(bim1)
    bi = Decimal(bi)

    # calculate mu
    c03 = (dim1 - Decimal('2') * dim2 + (Decimal('5') / Decimal('4')) * bi + Decimal('3') * bi)
    t03 = ((bi / Decimal('4')) + (Decimal('5') / Decimal('4') * bi) + bi)
    slope03 = c03 / t03

    c37 = (bi - Decimal('2') * bim1 + (Decimal('5') / Decimal('4')) * di + Decimal('3') * di)
    t37 = ((di / Decimal('4')) + (Decimal('5') / Decimal('4') * di) + di)
    slope37 = c37 / t37


    print(str(i) + ": " + str(slope03) + " - " + str(slope37) + " - (" + str(c03) + ", " + str(t03) + ") - (" + str(c37) + ", "+ str(t37) + ")")

    # print(str(bi) + " - " + str(bim1))
    # print(str(di) + " - " + str(dim1))


    # compare to functions

    # loop over the barrier set
    # find time for event points (end of 3 int, to end of 3 int)
    # get diff = consumption rate within interval
    # print
    pass


#
if __name__ == "__main__":
    barriers = barrier_set7_v2()
    # barriers = barrier_set_sol()
    t = Decimal('1000000000')
    index_b0 = 0

    barriers_pos = [i for i in barriers if i[0] > 0]
    barriers_pos.insert(0, (Decimal(0), Decimal(0)))
    barriers_pos = sorted(barriers_pos, key=lambda x: abs(x[0]))

    barriers_neg = [(abs(i[0]), i[1]) for i in barriers if i[0] < 0]
    barriers_neg.append((Decimal(0), Decimal(0)))
    # barriers_neg.reverse()
    barriers_neg = sorted(barriers_neg, key=lambda x: abs(x[0]))

    # sorted(barriers_neg, key=abs)
    _barriers = sorted(barriers, key=lambda x: abs(x[0]))
    out = ""
    for i in range(2, len(_barriers)):
        cim2, dim2 = _barriers[i-2]
        ci, di = _barriers[i]

        d = abs(ci) + 2 * dim2
        out += str(d) + ","
        print(str(d))

    print(out)
    print(barriers_pos)
    print(barriers_neg)

    cs_t_max = 0
    # for _t in range(3, 30):
    #     barriers = barriers_pos
    #     cs_t_pos = f_v1_0(_t)
    #
    #     barriers = barriers_neg
    #     cs_t_neg = f_v1_0(_t)
    #
    #     cs_t = (cs_t_pos + cs_t_neg) / _t
    #     cs_t_max = max(cs_t_max, cs_t)

    for i in range(2,10):
        f_slope(i)

    print(str(cs_t_max))

    print("Hello World")
