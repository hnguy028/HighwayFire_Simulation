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
        if t > 0:
            pass
        elif 10 > t > 0:
            pass
        elif 10 > t > 0:
            pass
        elif 10 > t > 0:
            pass
        else:
            # this would be the forward recursive call
            pass
    else:
        if t > 0:
            pass
        elif 10 > t > 0:
            pass
        elif 10 > t > 0:
            pass
        elif 10 > t > 0:
            pass
        else:
            # this would be the forward recursive call
            pass


# Base case for f_v1
def f_v1_0(t):
    # distance to the top of the first barrier
    b1 = barriers[index_b0 + 1]
    if t <= b1[0] + b1[1]:
        return t
    else:
        # time to get to the top of the first barrier plus recursive call
        return b1[0] + b1[1] + f_v1(1, t)


# need to calculate the distance between to barriers given index i
def get_ci():
    pass


if __name__ == "__main__":
    barriers = []
    index_b0 = 0

    print("Hello World")
