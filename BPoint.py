##
#
##


class BPoint:

    speed = 1
    time_step = 1

    x = 0
    y = 0

    p_type = None
    p_direction = 1

    def __init__(self, p_type, time_step=1, speed=1, direction=1):
        self.p_type = p_type
        self.speed = speed
        self.time_step = time_step
        self.p_direction = direction

    def move(self, barrier_set):
        t_dist = self.get_step_size()
        if self.p_type == "CENTER":
            self.y += t_dist
        elif self.p_type == "TYPE2":

            # loop until distance required to travel is 0
            while t_dist > 0:
                # if at a barrier move up as much as possible
                if self.x in [b[0] for b in barrier_set]:
                    barrier = barrier_set[[b[0] for b in barrier_set].index(self.x)]

                    d = min(t_dist, self.y - barrier[1])
                    self.y += (d * self.p_direction)

                    t_dist -= d

                if t_dist > 0:
                    # barrier = barrier_set[[b[0] for b in barrier_set].index(self.x)]
                    # barrier_set.sort(key=lambda t: t[0])

                    # find right most barrier to self.x
                    next_barrier_x = min(xc for xc in [b[0] for b in barrier_set] if xc > self.x)
                    barrier = barrier_set[[b[0] for b in barrier_set].index(next_barrier_x)]

                    # move right as much as possible
                    d = min(t_dist, self.x - barrier[0])
                    self.x += (d * self.p_direction)

                    t_dist -= d

            # find if point is at a barrier
            # for barrier in barrier_set:
            #     pass

    def get_coord(self):
        return [self.x, self.y]

    def get_step_size(self):
        return self.speed * self.time_step
