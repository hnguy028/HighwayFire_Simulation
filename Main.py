##
#
##
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from Fire import *
from matplotlib import style

dir = "data/"
time_step = 1

fire = Fire(time_step)

# Test Data
barrier_set = [(-1, 2), (-3, 4), (3, 3)]
# barrier_set = [(-3, 4), (-2, 2), (1, 3), (2, 5)]
barrier_set = [(1, 4), (2, 5), (3, 9)]
# barrier_set = [(-2.5, 3.6), (0.8, 4.3), (3.1, 7.6)]

# causes rounding error when k intervals are extremely close together ie smaller than (10^(-10))
# barrier_set = [(-1.5, 3.6), (0.8, 4.3), (3.1, 7.6)]


def animate(i):
    # l1 fire simulation
    # ax1.clear()
    coords = fire.get_boundary()
    for (c1, c2) in coords:
        if fire.t >= end_time:
            ax1.plot(c1, c2, linestyle='-', linewidth=2, color='r')
        else:
            ax1.plot(c1, c2, linestyle='dashed', linewidth=1, color='grey')

    # draw barriers
    # for p in barrier_set:
    #     ax1.plot([p[0], p[0]], [0, p[1]], linestyle='solid', color='black')

    # plot of cs(t)
    ax2.clear()
    ax2.set_xticks(np.arange(ax2_dim[0]-1, ax2_dim[1]+1, ax2_dim[4]))
    ax2.set_yticks(np.arange(ax2_dim[2]-1, ax2_dim[3]+1, ax2_dim[4]))
    ax2.grid(True)

    # if time step != 1, then we need eto give a a second array for the according time increments for each cst
    ax2.plot(fire.cs_t, fire.cst)

    # print table for time vs barrier consumed
    if fire.t > 0:
        res_str = "{0:4.2f} | {1:6.2f} | {2:7.5f}".format(fire.t, fire.cs, (fire.cs / fire.t))
        print(res_str)
        if writeToFile:
            file.write("{0:4.2f},{1:6.2f},{2:7.5f}\n".format(fire.t, fire.cs, (fire.cs / fire.t)))

    # increment logic
    fire.increment(barrier_set)

    # fix graph bounds
    ax1.set_xlim([ax1_dim[0]-1, ax1_dim[1]+1])
    ax1.set_ylim([ax1_dim[2]-1, ax1_dim[3]+1])

    ax2.set_xlim([ax2_dim[0]-1, ax2_dim[1]+1])
    ax2.set_ylim([ax2_dim[2]-1, ax2_dim[3]+1])

    if fire.t >= end_time + 1:
        for (c1, c2) in coords:
            ax1.plot(c1, c2, linestyle='-', linewidth=2, color='r')

        fire.print_bound_points()

        ani.event_source.stop()

        if writeToFile:
            fig.savefig(dir + "hf_sim" + time_code + ".png")
            file.write(str(fire.cst))
            file.close()

        print("Done")


if __name__ == '__main__':
    style.use('fivethirtyeight')

    time_code = time.strftime("%Y%m%d-%H%M%S")
    end_time = 9
    anim_interval = 1000
    repeat = True
    writeToFile = False

    fig = plt.figure(figsize=(10, 7))
    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2)

    # [lower_x, upper_x, lower_y, upper_y, grid_step]

    # ax1_dim = [-10, 10, 0, 10, 1]
    ax1_dim = [-end_time, end_time, 0, end_time, 1]
    ax2_dim = [0, 20, 0, 25, 1]
    # ax2_dim = [0, max_frames * time_step, 0, max_frames * time_step, 1]

    ax1.set_xticks(np.arange(ax1_dim[0]-1, ax1_dim[1]+1, ax1_dim[4]))
    ax1.set_yticks(np.arange(ax1_dim[2]-1, ax1_dim[3]+1, ax1_dim[4]))
    ax1.grid(True)

    ax2.set_xticks(np.arange(ax2_dim[0]-1, ax2_dim[1]+1, ax2_dim[4]))
    ax2.set_yticks(np.arange(ax2_dim[2]-1, ax2_dim[3]+1, ax2_dim[4]))
    ax2.grid(True)

    # data output
    if writeToFile:
        file = open(dir + "hf_table" + time_code + ".csv", "w+")
        file.write("time,length,slope\n")

    print("TIME | LENGTH | SLOPE")

    # No clear
    # draw barriers
    for p in barrier_set:
        ax1.plot([p[0], p[0]], [0, p[1]], linestyle='solid', color='black')

    # placeholder
    coords = None

    # plot graph and animate
    ani = animation.FuncAnimation(fig, animate, interval=anim_interval, repeat=repeat)
    plt.show()
