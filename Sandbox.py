##
#
##

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from Fire import Fire
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
# xx = np.linspace(-10, 10, 1000)

# a barrier is defined as a tuple of time/x value
# and length/y value
# barrier_data = open('barrier_set.csv','r').read()
barrier_set = [(-1,2),(-3,4),(3,3)]

lx = -1
ly = -1

dx = 0
dy = 0

t = -1

flag = False

fire = Fire()

def animate(i):
    global lx, ly, dx, dy, t, flag
   # graph_data = open('data1.csv','r').read()
   # lines = graph_data.split('\n')

   # xs = []
   # ys = []
   # x,y = lines[0].split(',')
   # for line in lines:
   #     if len(line) > 1:
   #         x, y = line.split(',')
   #         xs.append(float(x))
   #         ys.append(float(y))

    # xx = np.linspace(-lx/2, lx/2, 1000)
    # yy = np.linspace(-ly/2, ly/2, 1000)
    ax1.clear()
    # ax1.plot(xs, ys)
    # ax1.plot(-xx + dx, xx + dy, linestyle='solid')
    # ax1.plot(yy + i, yy-i, linestyle='solid')

    for (c1,c2) in fire.get_boundary():
        ax1.plot(c1, c2, linestyle='solid', color='r')

    # draw barriers
    for p in barrier_set:
       ax1.plot([p[0],p[0]],[0,p[1]], linestyle='dashed')

    # fix graph bounds
    ax1.set_xlim([-15, 15])
    ax1.set_ylim([-10, 20])

    fire.increment(barrier_set)

    nu = fire.cs / fire.t
    print(str(fire.cs) + "/" + str(fire.t) + " : " + str(nu))


def find_intersection(line1, line2, barriers):
    pass


def get_xx_yy(coord1, coord2):
    return [coord1[0], coord2[0]],[coord1[1], coord2[1]]


if __name__ == '__main__':
    ani = animation.FuncAnimation(fig, animate, frames=10, interval=1000, repeat=False)
    plt.show()


