##
#
##
from decimal import *


class BPoint:

    speed = 1.0
    time_step = 1.0

    x = Decimal(0)
    y = Decimal(0)

    p_type = None
    p_direction = 1

    def __init__(self, p_type, x=0, y=0, time_step=1.0, speed=1.0, direction=1, init_dist=-1.0):
        self.p_type = p_type
        self.x = Decimal(x)
        self.y = Decimal(y)
        self.speed = speed
        self.time_step = time_step
        self.p_direction = direction
        self.init_dist = init_dist

    # move current point t_dist time units
    def move(self, barrier_set, bpoint_set, t_dist=1):
        t_dist = Decimal(t_dist) if self.init_dist == -1 else Decimal(self.init_dist)
        cs = 0

        if self.p_type == "CENTER":
            self.y += t_dist

        elif self.p_type == "TYPE2":

            # loop until distance required to travel is 0
            while t_dist > 0:
                # if currently at a barrier, move up along it
                if self.x in [b[0] for b in barrier_set]:
                    barrier = barrier_set[[b[0] for b in barrier_set].index(self.x)]

                    # either we traveled all of defined dist or we reached the top of the barrier
                    d = min(t_dist, abs(self.y - barrier[1]))
                    self.y += d

                    t_dist -= d
                    cs += abs(d)

                    # reached the top of a barrier
                    if self.y == barrier[1] and d > 0:
                        print("\/ end 1 int")
                        # create a new bpoint
                        ind = bpoint_set.index(self)
                        bpoint_set.insert(ind+1,
                                          BPoint("TYPE4", self.x, self.y, self.time_step, self.speed, self.p_direction,
                                                 init_dist=t_dist))

                if t_dist > 0:
                    # find the next barrier in our respective direction
                    r_barriers = [xc for xc in [b[0] for b in barrier_set] if xc > self.x] if self.p_direction > 0 else [xc for xc in [b[0] for b in barrier_set] if xc < self.x]

                    # if there are any barriers left
                    if len(r_barriers) > 0:
                        next_barrier_x = min(r_barriers) if self.p_direction > 0 else max(r_barriers)
                        barrier = barrier_set[[b[0] for b in barrier_set].index(next_barrier_x)]

                        # move in that direction until we hit the barrier or traveled all of t_dist
                        d = min(t_dist, abs(self.x - barrier[0]))
                        self.x += (d * self.p_direction)

                        t_dist -= d

                        if self.y == 0:
                            cs += abs(d)

                        # reached the the next barrier
                        if self.x == next_barrier_x and d > 0 and self.y > 0:
                            print("\/ start 3 int")
                            # create a new bpoint
                            ind = bpoint_set.index(self)
                            bpoint_set.insert(ind + 1,
                                              BPoint("TYPE3", self.x, self.y, self.time_step, self.speed,
                                                     self.p_direction,
                                                     init_dist=t_dist))

                    else:
                        # No more barriers beyond this point, move all of defined distance in respective direction
                        d = t_dist * self.p_direction
                        self.x += d

                        if self.y == 0:
                            cs += abs(d)
                        t_dist = 0

        elif self.p_type == "TYPE3":
            if t_dist > 0 and self.y > 0:
                if self.x in [b[0] for b in barrier_set]:
                    barrier = barrier_set[[b[0] for b in barrier_set].index(self.x)]

                    # either we traveled all of defined dist or we reached the horizontal axis y=0
                    d = min(t_dist, abs(self.y))
                    self.y -= d

                    t_dist -= d

                    cs += abs(d)

                    if self.y <= 0:
                        print("^ end 3 int")
                        del bpoint_set[bpoint_set.index(self)]

                    # if t_dist > 0: we've already hit y=0 and cannot travel anymore
                else:
                    print("Error - TYPE3 point must be at a barrier")

            self.init_dist = -1
        
        elif self.p_type == "TYPE4":
            # loop until distance required to travel is 0
            # while t_dist > 0:
            if t_dist > 0:
                # if currently at a barrier, move down along it
                if self.x in [b[0] for b in barrier_set] and self.y > 0:
                    # barrier = barrier_set[[b[0] for b in barrier_set].index(self.x)]

                    # either we traveled all of defined dist or we reached the horizontal axis y=0
                    d = min(t_dist, abs(self.y))
                    self.y -= d

                    t_dist -= d

                    if self.y <= 0:
                        print("^ end 0 int")

                if t_dist > 0 and self.y == 0:
                    # find the next barrier in our respective direction

                    # need to check within current location and (0,0)
                    if self.p_direction > 0:
                        r_barriers = [xc for xc in [b[0] for b in barrier_set] if xc > self.x]
                    else:
                        r_barriers = [xc for xc in [b[0] for b in barrier_set] if xc < self.x]

                    # if there are any barriers left
                    if len(r_barriers) > 0:
                        next_barrier_x = min(r_barriers) if self.p_direction > 0 else max(r_barriers)
                        barrier = barrier_set[[b[0] for b in barrier_set].index(next_barrier_x)]

                        # move in that direction until we hit the barrier or traveled all of t_dist
                        d = min(t_dist, abs(self.x - barrier[0]))
                        self.x += (d * self.p_direction)

                        t_dist -= d

                        cs += abs(d)

                        if next_barrier_x == self.x:
                            # remove self from bpoint_list
                            del bpoint_set[bpoint_set.index(self)]

                    else:
                        # No more barriers beyond this point, move all of defined distance in respective direction
                        d = t_dist * self.p_direction
                        self.x += d

                        if self.y == 0:
                            cs += abs(d)

                        t_dist = 0

            # only if a bpoint is created during an "iteration"
            self.init_dist = -1

        return cs

    # returns the next min time between next k event and input dist
    def dist_to_event(self, barrier_set, dist):
        if dist <= 0:
            print("Error dist is 0")
            exit()

        if self.p_type == "CENTER":
            return dist
        elif self.p_type == "TYPE2":
            # if currently at a barrier, move up along it
            if self.x in [b[0] for b in barrier_set]:
                barrier = barrier_set[[b[0] for b in barrier_set].index(self.x)]

                # either we traveled all of defined dist or we reached the top of the barrier
                if abs(self.y - barrier[1]) > 0:
                    return min(dist, abs(self.y - barrier[1]))

            # find the next barrier in our respective direction
            r_barriers = [xc for xc in [b[0] for b in barrier_set] if xc > self.x] if self.p_direction > 0 else \
                [xc for xc in [b[0] for b in barrier_set] if xc < self.x]

            # if there are any barriers left
            if len(r_barriers) > 0:
                next_barrier_x = min(r_barriers) if self.p_direction > 0 else max(r_barriers)
                barrier = barrier_set[[b[0] for b in barrier_set].index(next_barrier_x)]

                # move in that direction until we hit the barrier or traveled all of t_dist
                return min(dist, abs(self.x - barrier[0]))
            else:
                return dist

        elif self.p_type == "TYPE3":
            if self.y > 0 and self.x in [b[0] for b in barrier_set]:
                # either we traveled all of defined dist or we reached the horizontal axis y=0
                return min(dist, abs(self.y))
            else:
                print("Error - TYPE3 not at a barrier or below horizon")
                exit()
        elif self.p_type == "TYPE4":
            if self.x in [b[0] for b in barrier_set] and self.y > 0:
                # either we traveled all of defined dist or we reached the horizontal axis y=0
                return min(dist, abs(self.y))

            if self.y == 0:
                # find the next barrier in our respective direction
                # need to check within current location and (0,0)
                if self.p_direction > 0:
                    r_barriers = [xc for xc in [b[0] for b in barrier_set] if xc > self.x]
                else:
                    r_barriers = [xc for xc in [b[0] for b in barrier_set] if xc < self.x]

                # if there are any barriers left
                if len(r_barriers) > 0:
                    next_barrier_x = min(r_barriers) if self.p_direction > 0 else max(r_barriers)
                    barrier = barrier_set[[b[0] for b in barrier_set].index(next_barrier_x)]

                    # move in that direction until we hit the barrier or traveled all of t_dist
                    return min(dist, abs(self.x - barrier[0]))

                else:
                    # No more barriers beyond this point, move all of defined distance in respective direction
                    return dist

    def get_coord(self):
        return [self.x, self.y]

    def get_step_size(self):
        return self.speed * self.time_step
