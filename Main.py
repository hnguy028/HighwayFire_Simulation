##
#
##
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from Fire import *
from matplotlib import style

fire = Fire()
barrier_set = [(-1, 2), (-3, 4), (3, 3)]


def animate(i):
    # l1 fire simulation
    ax1.clear()

    for (c1, c2) in fire.get_boundary():
        ax1.plot(c1, c2, linestyle='solid', color='r')

    # draw barriers
    for p in barrier_set:
        ax1.plot([p[0], p[0]], [0, p[1]], linestyle='dashed')

    # plot of cs(t)
    ax2.clear()
    ax2.plot(fire.cst)

    # increment logic
    fire.increment(barrier_set)

    # print table for time vs barrier consumed
    print("{0:4.0f} | {1:6.0f} | {2:10.5f}".format(fire.t, fire.cs, (fire.cs / fire.t)))

    # fix graph bounds
    ax1.set_xlim([-15, 15])
    ax1.set_ylim([-1, 20])
    ax2.set_xlim([-1, 20])
    ax2.set_ylim([-1, 20])

    if fire.t >= max_frames:
        ani.event_source.stop()
        print("Done")


if __name__ == '__main__':
    style.use('fivethirtyeight')

    fig = plt.figure(figsize=(10, 7))
    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2)

    xlim = [-15, 15]
    ylim = [-1, 20]
    max_frames = 15
    anim_interval = 1000
    repeat = False

    print("TIME | LENGTH | SLOPE")

    # plot graph and animate
    ani = animation.FuncAnimation(fig, animate, interval=anim_interval, repeat=repeat)
    plt.show()
