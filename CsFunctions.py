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


#
if __name__ == "__main__":
    barriers = barrier_set7()
    t = Decimal('1000000000')
    index_b0 = 0

    barriers_pos = [i for i in barriers if i[0] > 0]
    barriers_pos.insert(0, (0, 0))

    barriers_neg = [(abs(i[0]), i[1]) for i in barriers if i[0] < 0]
    barriers_neg.append((0, 0))
    barriers_neg.reverse()

    print(barriers_pos)
    print(barriers_neg)

    cs_t_max = 0
    for _t in range(3, 30):
        barriers = barriers_pos
        cs_t_pos = f_v1_0(_t)

        barriers = barriers_neg
        cs_t_neg = f_v1_0(_t)

        cs_t = (cs_t_pos + cs_t_neg) / _t
        cs_t_max = max(cs_t_max, cs_t)

    print(str(cs_t_max))

    print("Hello World")
