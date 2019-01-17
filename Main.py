##
#
##
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from Fire1 import *
from Fire2 import *
from matplotlib import style

dir = "data/"

fire = Fire1()
fire2 = Fire2()
barrier_set = [(-1, 2), (-4, 4), (3, 3)]
# barrier_set = [(-3, 4), (-2, 2), (1, 3), (2, 5)]
# barrier_set = [(2, 4), (3, 6), (4, 8)]


def animate(i):
    # l1 fire simulation
    # ax1.clear()

    for (c1, c2) in fire.get_boundary():
        if fire.t == max_frames - 1:
            ax1.plot(c1, c2, linestyle='-', linewidth=2, color='r')
        else :
            ax1.plot(c1, c2, linestyle='dashed', linewidth=1, color='grey')

    # draw barriers
    # for p in barrier_set:
    #     ax1.plot([p[0], p[0]], [0, p[1]], linestyle='solid', color='black')

    # plot of cs(t)
    ax2.clear()
    ax2.plot(fire.cst)

    # increment logic
    fire.increment(barrier_set)

    # print table for time vs barrier consumed
    res_str = "{0:4.0f} | {1:6.0f} | {2:7.5f}".format(fire.t, fire.cs, (fire.cs / fire.t))
    print(res_str)
    file.write("{0:4.0f},{1:6.0f},{2:7.5f}\n".format(fire.t, fire.cs, (fire.cs / fire.t)))

    # fix graph bounds
    ax1.set_xlim([-10, 10])
    ax1.set_ylim([-1, 10])

    ax2.set_xlim([-1, 19])
    ax2.set_ylim([-1, 19])

    if fire.t >= max_frames:
        ani.event_source.stop()
        fig.savefig(dir + "hf_sim" + time_code + ".png")
        file.write(str(fire.cst))
        file.close()
        print("Done")


if __name__ == '__main__':
    style.use('fivethirtyeight')

    time_code = time.strftime("%Y%m%d-%H%M%S")

    fig = plt.figure(figsize=(10, 7))
    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2)

    xlim = [-15, 15]
    ylim = [-1, 20]
    max_frames = 10
    anim_interval = 1000
    repeat = True

    # data output
    file = open(dir + "hf_table" + time_code + ".csv", "w+")
    file.write("time,length,slope\n")

    print("TIME | LENGTH | SLOPE")

    # No clear
    # draw barriers
    for p in barrier_set:
        ax1.plot([p[0], p[0]], [0, p[1]], linestyle='solid', color='black')


    # plot graph and animate
    ani = animation.FuncAnimation(fig, animate, interval=anim_interval, repeat=repeat)
    plt.show()
