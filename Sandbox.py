##
#
##
from BarrierFactory import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


def one():
    kv = [(7, 12), (20.75, 38.75), (62.00, 116.75), (185.750, 350.750), (557.0000, 1052.7500), (1670.75000, 3158.75000),
     (5012.000000, 9476.750000), (15035.7500000, 28430.7500000), (45107.00000000, 85292.75000000),
     (135320.750000000, 255878.750000000), (405962.0000000000, 767636.7500000000),
     (1217885.75000000000, 2302910.75000000000), (3653657.000000000000, 6908732.750000000000),
     (10960970.7500000000000, 20726198.7500000000000), (32882912.00000000000000, 62178596.75000000000000),
     (98648735.750000000000000, 186535790.750000000000000)]

    for i in range(1, len(kv)):
        t0, c0 = kv[i-1]
        t1, c1 = kv[i]

        c = c1 - c0
        t = t1 - t0
        # print(str(c/t) + " - (" + str(c) +", "+ str(t) + ")")


    # b1 = barrier_set7()
    b2 = barrier_set7_v2()

    # todo : handle the recursive part and check if the values match the experimental values

    b = [i for i in b2 if i[0] > 0]
    b.insert(0, (0, 0))
    m = 0
    cs_t1 = cs_t2 = cs_t3 = cs_t4 = 0

    for i in range(2, 10):
        ci, di = b[i]
        ci = Decimal(ci)
        di = Decimal(di)

        ci_m1, di_m1 = b[i-1]
        ci_m1 = Decimal(ci_m1)
        di_m1 = Decimal(di_m1)

        cs_t1 = ((ci - ci_m1 + Decimal('2.0') * di_m1)+4) / (ci + Decimal('2.0') * di_m1)
        cs_t2 = ((ci - ci_m1 + di + di_m1)+4) / (ci + di)
        cs_t3 = ((ci - ci_m1 + Decimal('2.0') * di_m1)+4) / (ci + Decimal('2.0') * di_m1)
        cs_t4 = ((ci - ci_m1 + di)+4) / (ci + di)

        print(m, cs_t1, cs_t2, cs_t3, cs_t4)
        m = max(m, cs_t1, cs_t2, cs_t3, cs_t4)

    print(str(m))
    out = ""
    for i in range(6, 23):
        a, b = b2[i-2]
        c, d = b2[i]
        out += str(int(d - b)) + ","

    print(out)
    a,b = b2[6]
    print(a)

    # print(sorted(b1, key=lambda x: x[0]))
    # print(sorted(b2, key=lambda x: x[0]))
    #
    # print(sorted(b2, key=lambda x: x[0]) == sorted(b1, key=lambda x: x[0]))


def a(b, i):
    if i == 1:
        return b[1][0]

    return b[i][0] - b[i-1][0]


def two():
    barriers = barrier_set7_v2()

    barriers_pos = [i for i in barriers if i[0] > 0]
    barriers_pos.insert(0, (Decimal(0), Decimal(0)))
    barriers_pos = sorted(barriers_pos, key=lambda x: abs(x[0]))

    barriers_neg = [(abs(i[0]), i[1]) for i in barriers if i[0] < 0]
    barriers_neg.append((Decimal(0), Decimal(0)))
    # barriers_neg.reverse()
    barriers_neg = sorted(barriers_neg, key=lambda x: abs(x[0]))

    # sorted(barriers_neg, key=abs)
    # _barriers = sorted(barriers, key=lambda x: abs(x[0]))

    print(barriers_pos)
    print(barriers_neg)

    for i in range(1, len(barriers_neg)-1):
        ai = a(barriers_neg, i+1)
        bi = barriers_neg[i][1]

        print((ai-bi)/bi)


def plot_lines(line1, line2):

    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.25)
    #
    # t = np.arange(0.0, 1000.0, 0.1)
    # s = np.sin(2*np.pi*t)
    plt.axis([0, 1, -1, 1])

    plt.axhline(y=0.5, color='r', linestyle='-')
    plt.axhline(y=-0.5, color='b', linestyle='-')

    l1, = plt.plot(line1, [0.5]*len(line1), 'bo')
    l2, = plt.plot(line2, [-0.5]*len(line2), 'ro')

    axcolor = 'lightgoldenrodyellow'
    axpos = plt.axes([0.2, 0.1, 0.65, 0.03], axisbg=axcolor)

    spos = Slider(axpos, 'Pos', 0.1, 900.0)

    def update(val):
        pos = spos.val
        ax.axis([pos,pos+10,-1,1])
        fig.canvas.draw_idle()

    spos.on_changed(update)

    plt.show()


if __name__ == '__main__':
    # one()
    # two()
    barrier_set_sol()
    # plot_lines([10, 20, 40], [5, 15, 75])
