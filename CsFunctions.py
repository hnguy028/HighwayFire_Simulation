from decimal import *
from BarrierFactory import *

##
#   Used for verification of consumption functions
#   Assumptions :
#   A0 : Barriers are of increasing length
#   A1 : Distance between a barrier and its preceding barrier is at least the distance of the previous barrier's length
#   A2 : The length of a barrier is at least twice the length of the previous barrier
##


# With assumption A0, A1, A2
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
    b1 = barriers[index_b0 + 1]
    if t <= b1[0] + b1[1]:
        return t
    else:
        # time to get to the top of the first barrier plus recursive call
        return b1[0] + b1[1] + f_v1(1, t)


if __name__ == "__main__":
    barriers = barrier_set2()
    index_b0 = 0

    barriers = [i for i in barriers if i[0] > 0]
    print(barriers)

    print(f_v1_0(64))

    print("Hello World")
