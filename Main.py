##
#
##
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from Fire import *
from matplotlib import style
from decimal import *
from BarrierFactory import *
import math

dir = "data/"
time_step = Decimal(1)

fire = Fire(time_step, 1000)

# Test Data
in_barrier_set = [(-1, 2), (-3, 4), (3, 3)]
# in_barrier_set = [(-3, 4), (-2, 2), (1, 3), (2, 5)]
# in_barrier_set = [(1, 4), (2, 5), (3, 9)]
# in_barrier_set = [(-2.5, 3.6), (0.8, 4.3), (3.1, 7.6)]


# in_barrier_set = [(-1.5, 3.6), (0.8, 4.3), (3.1, 7.6)]
# in_barrier_set = [(-150, 360), (80, 430), (310, 760)]
# in_barrier_set = [('-1.5', '3.6'), ('0.8', '4.3'), ('3.1', '7.6')]
# in_barrier_set = [(-1.5, 3.6), (0.8, 4.3), (3.1, 7.6)]

barrier_set = []


def define_barriers(ind):
    if ind == 0:
        return barrier_set0()
    elif ind == 1:
        return barrier_set1()
    elif ind == 2:
        return barrier_set2()
    elif ind == 3:
        return barrier_set3()
    elif ind == 4:
        return barrier_set4()
    elif ind == 5:
        return barrier_set5()
    else:
        return eval('barrier_set' + str(ind))()
    # by default return
    # return in_barrier_set


def d_barrier_set(_barrier_set):
    new_set = []
    for (_x, _y) in _barrier_set:
        new_set.append((Decimal(str(_x)), Decimal(str(_y))))
    return new_set


def boundary2flist(_list):
    new_list = []
    for ([_x1, _y1], [_x2, _y2]) in _list:
        new_list.append(([float(_x1), float(_y1)], [float(_x2), float(_y2)]))
    return new_list


def animate(i):
    # l1 fire simulation
    # ax1.clear()
    coords = boundary2flist(fire.get_boundary())
    bound_string = fire.get_bound_str()

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
    ax2.plot([0, s2_line], [0, _threshold * s2_line], linestyle='dashed', linewidth=2, color='grey')
    ax2.plot(fire.cs_t, fire.get_modded_cst(), linewidth=1, color='r')

    # print table for time vs barrier consumed
    if fire.t > 0:
        res_str = "{:3.0f} | {:6.2f} | {:8.2f} | {:8.2f} | {:7.5f} | {:8.2f} | {:7.5f}".format(i+1, fire.t, 2*fire.t, fire.cs, (fire.cs / fire.t), fire.cs_r, (fire.cs_r/fire.t))
        print(res_str)
        if writeToFile:
            file.write("{:4.2f},{:6.2f},{:7.5f}\n".format(fire.t, fire.cs, (fire.cs / fire.t)))

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

        # fire.print_bound_points()
        print(bound_string)

        ani.event_source.stop()

        if writeToFile:
            fig.savefig(dir + "hf_sim" + time_code + ".png")
            file.write(str(fire.cst))
            file.close()

        print("Program Terminated")


def threshold_check(i, cs, t, occ, flag):
    if flag:
        return True, 0

    slope = cs/t

    if slope >= threshold:
        occ += 1
        if occ >= 1:
            inp = input("Threshold Passed, Continue? [y/n/s]\n")
            if inp == "n":
                exit()
            elif inp == "s":
                return True, occ
            else:
                return False, occ

    return False, occ


# given the barrier set, a time t, and the zero index, determine the right most barrier at time t
def function_test(bset, t, z_index):
    print("Function Test")
    print("z_index: " + str(z_index) + " num_bar: " + str(len(bset)))
    print(f_p(Decimal(t), z_index, bset, z_index))
    print("Function Test")


# gets index of right most barrier given time t
def f_p(t, i, bset, z_index):
    print(t)
    # there is no barrier to the right
    if i >= len(bset):
        return i

    c_prev = (0, 0) if i == z_index else bset[i-1]
    c = bset[i]

    dist_to_next_bar = (abs(c[0] - c_prev[0]) + abs(c[1] - c_prev[1]))
    if t > dist_to_next_bar:
        return f_p(t-dist_to_next_bar, i+1, bset, z_index)
    else:
        return i


if __name__ == '__main__':
    style.use('fivethirtyeight')

    time_code = time.strftime("%Y%m%d-%H%M%S")
    end_time = 50
    anim_interval = 1000
    repeat = True

    # instructions
    writeToFile = False
    visual = False
    runFunction = False

    nv_max_it = 10000 # pref_step_size * loops

    barrier_set_id = '7_v2'
    # barrier_set_id = '_sol'

    S = 1
    # '1.894427190999915835106747838'
    _threshold = (Decimal(2) + Decimal(math.sqrt(Decimal(5)))) / Decimal(math.sqrt(Decimal(5)))
    threshold = 1.90

    # functionally generate barriers
    in_barrier_set = define_barriers(barrier_set_id)

    # convert barrier set to decimal object for precision
    barrier_set = d_barrier_set(in_barrier_set)

    # data output
    if writeToFile:
        file = open(dir + "hf_table" + time_code + ".csv", "w+")
        file.write("time,length,slope\n")

    # i, t, 2t, cst, qst
    print("  i |   TIME | 2 x TIME |   LENGTH |   SLOPE")

    # placeholder - to draw final boundary in red
    coords = None

    # if runFunction:
    #     z_ind = barrier_set.index((1, 2))
    #     print(z_ind)
    #     function_test(barrier_set, 25.5, z_ind)

    if visual:
        fig = plt.figure(figsize=(10, 7))
        ax1 = fig.add_subplot(2, 1, 1)
        ax2 = fig.add_subplot(2, 1, 2)

        # [lower_x, upper_x, lower_y, upper_y, grid_step]

        # ax1_dim = [-10, 10, 0, 10, 1]
        ax1_dim = [-end_time, end_time, 0, end_time, 1]
        ax2_dim = [0, 100, 0, 100, 1]
        s2_line = 25
        # ax2_dim = [0, max_frames * time_step, 0, max_frames * time_step, 1]

        ax1.set_xticks(np.arange(ax1_dim[0] - 1, ax1_dim[1] + 1, ax1_dim[4]))
        ax1.set_yticks(np.arange(ax1_dim[2] - 1, ax1_dim[3] + 1, ax1_dim[4]))
        ax1.grid(True)

        # ax2.set_xticks(np.arange(ax2_dim[0]-1, ax2_dim[1]+1, ax2_dim[4]))
        # ax2.set_yticks(np.arange(ax2_dim[2]-1, ax2_dim[3]+1, ax2_dim[4]))
        # ax2.grid(True)

        # draw barriers
        ax1.axhline(y=0, linestyle='solid', color='black')
        for (x, y) in barrier_set:
            ax1.plot([float(x), float(x)], [0, float(y)], linestyle='solid', color='black')

        # plot graph and animate
        ani = animation.FuncAnimation(fig, animate, interval=anim_interval, repeat=repeat)
        plt.show()

    else:
        # print info at each iteration
        print_flag = True
        ignore_ind = 2 # number of iteration to ignore threshold and max cs count

        # variables
        tCount = 0      # number of times threshold is passed
        sFlag = False   # flag to suppress threshold warnings
        max_cs = 0      # max consumption reached

        # temp variables
        max_csr = 0
        max_csl = 0

        for i in range(0, nv_max_it):
            fire.increment(barrier_set)
            if print_flag:
                res_str = "{:3.0f} | {:6.2f} | {:8.2f} | {:8.2f} | {:7.5f}".format(i + 1, fire.t, 2 * fire.t, fire.cs,
                                                                                   (fire.cs / fire.t))

                res_str2 = " | {:8.2f} | {:7.5f} | {:8.2f} | {:7.5f}".format(fire.cs_l, (fire.cs_l / fire.t), fire.cs_r,
                                                                             (fire.cs_r / fire.t))
                res_str += res_str2
                print(res_str)

            if i > ignore_ind:
                sFlag, tCount = threshold_check(i, fire.cs, fire.t, tCount, sFlag)
                max_cs = max(max_cs, fire.cs/fire.t)
                max_csr = max(max_csr, fire.cs_r / fire.t)
                max_csl = max(max_csr, fire.cs_l / fire.t)

            if fire.t in [7,20.750,62.000,185.750,557.0000,1670.75000,5012.000000,15035.7500000,45107.00000000,135320.750000000,405962.0000000000,1217885.75000000000,3653657.000000000000,10960970.7500000000000,32882912.00000000000000,98648735.750000000000000,295946207.0000000000000000,887838620.75000000000000000,2663515862.000000000000000000,7990547585.750000000000000000,23971642757.00000000000000000]:
                print(str(fire.t) + ": " + str(fire.cs))
                pass

        res_str = "{:3.0f} | {:6.2f} | {:8.2f} | {:8.2f} | {:7.5f}".format(i + 1, fire.t, 2 * fire.t, fire.cs,
                                                                           (fire.cs / fire.t))

        res_str2 = " | {:8.2f} | {:7.5f} | {:8.2f} | {:7.5f}".format(fire.cs_l, (fire.cs_l / fire.t), fire.cs_r,
                                                                     (fire.cs_r / fire.t))
        res_str += res_str2

        print(res_str)
        fire.print_bound_points()
        print("Max slope in simulation: " + str(max_cs) + ", " + str(max_csr) + ", " + str(max_csl))
        # if max_cs < _threshold:
        #     for i in range(0, 6):
        #         print("EEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRROOOOOOOOOOOOOOORRRRRRRRRRRROOOOOOOOOOOORRRRRRRRRRRR")



