##
#
##
from BarrierFactory import *

if __name__ == '__main__':
    b1 = barrier_set7()
    b2 = barrier_set7_v2()

    print(sorted(b1, key=lambda x: x[0]))
    print(sorted(b2, key=lambda x: x[0]))

    print(sorted(b2, key=lambda x: x[0]) == sorted(b1, key=lambda x: x[0]))