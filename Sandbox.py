##
#
##

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
# xx = np.linspace(-10, 10, 1000)

# a barrier is defined as a tuple of time/x value
# and length/y value
# barrier_data = open('barrier_set.csv','r').read()
barrier_set = [(10,10),(30,25),(60,40)]

lx = -1
ly = -1

dx = 0
dy = 0

t = -1


def animate(i):
   global lx, ly, dx, dy, t
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

   print(str(t) + " -- " + str(i))

   if t >= 10 and t <=20:
       dy += 1

       print("Here")
   else:
       dx += 0.5
       dy += 0.5

       lx += 1
       ly += 1

   xx = np.linspace(-lx/2, lx/2, 1000)
   yy = np.linspace(-ly/2, ly/2, 1000)
   ax1.clear()
   # ax1.plot(xs, ys)
   ax1.plot(-xx + dx, xx + dy, linestyle='solid')
   ax1.plot(yy + i, yy-i, linestyle='solid')

   for p in barrier_set:
       ax1.plot([p[0],p[0]],[0,p[1]], linestyle='dashed')
   ax1.set_xlim([0, 100])
   ax1.set_ylim([0, 100])

   t += 1
   return 0


def find_intersection(line1, line2, barriers):
   # first intersection of any barrier and line1 will determine if line2
   # even exists, and where it would begin

   # handled differently if intersection is at the top of the barrier

   # return empty list if no intersection with barriers
   # else return x,y coordinate of intersection (should be integer coordinates)
   pass


ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()

