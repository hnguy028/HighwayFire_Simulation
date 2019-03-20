from BPoint import *
from decimal import *


class Fire:

    cs = Decimal(0.0)
    qs = 0.0

    cst = [Decimal(0)]
    cs_t = [0]
    qst = [0]

    cs_l = Decimal(0.0)
    cs_r = Decimal(0.0)

    cst_lhs = [Decimal(0)]
    cst_rhs = [Decimal(0)]

    t = Decimal(0.0)
    time_step = 1.0
    queue_pos = []
    queue_neg = []

    pref_step_size = Decimal(5)

    def __init__(self, time_step=1, pref_step=5):
        self.time_step = time_step
        self.pref_step_size = Decimal(pref_step)
        self.queue_neg = [BPoint("TYPE2", direction=-1, time_step=self.time_step)]
        self.queue_pos = [BPoint("CENTER", time_step=self.time_step),
                          BPoint("TYPE2", time_step=self.time_step)]

    # get distance to next event under preferred step size
    def d_event(self, barrier_set):

        d_ev = self.pref_step_size

        for p in self.queue_neg:
            d_ev = min(p.dist_to_event(barrier_set, self.pref_step_size), d_ev)

        for p in self.queue_pos:
            d_ev = min(p.dist_to_event(barrier_set, self.pref_step_size), d_ev)

        return d_ev

    def increment(self, barrier_set):
        d_ev = self.d_event(barrier_set)
        self.t += d_ev

        if d_ev == 0:
            self.print_bound_points()
            exit()

        csp_neg = Decimal(0.0)
        csp_pos = Decimal(0.0)

        i = 0
        prev_length = len(self.queue_neg)

        # move all boundary points to the left of the origin
        while i < len(self.queue_neg):
            csp_neg += self.queue_neg[i].move(barrier_set, self.queue_neg, d_ev)

            if prev_length - 1 == len(self.queue_neg):
                i -= 1

            i += 1
            prev_length = len(self.queue_neg)

        i = 0
        prev_length = len(self.queue_pos)

        # move all boundary points to the right of the origin
        while i < len(self.queue_pos):
            csp_pos += self.queue_pos[i].move(barrier_set, self.queue_pos, d_ev)

            if prev_length - 1 == len(self.queue_pos):
                i -= 1

            i += 1
            prev_length = len(self.queue_pos)

        # save lhs and rhs consumption
        self.cst_lhs.append(csp_neg)
        self.cst_rhs.append(csp_pos)

        # save total consumption and time
        csp = csp_neg + csp_pos
        self.cs += csp
        self.cs_l += csp_neg
        self.cs_r += csp_pos
        self.cst.append(self.cs)
        self.cs_t.append(self.t)

    def get_boundary(self):
        boundary = []

        rev_it = reversed(self.queue_neg)
        p = next(rev_it)

        for q in rev_it:
            a, b = get_xx_yy(p.get_coord(), q.get_coord())
            boundary.append((a, b))
            p = q

        it = iter(self.queue_pos)
        q = next(it)

        a, b = get_xx_yy(p.get_coord(), q.get_coord())
        boundary.append((a, b))
        p = q

        for q in it:
            a, b = get_xx_yy(p.get_coord(), q.get_coord())
            boundary.append((a, b))
            p = q

        return boundary

    def get_modded_cst(self):
        res = []
        res = self.cst
        # for t in self.cst:
        #     res.append(t - Decimal(1))

        return res

    def print_bound_points(self):
        print("\n###############")
        for point in self.queue_neg + self.queue_pos:
            a, b = point.get_coord()
            print(point.p_type + " : (" + str(a) + ", " + str(b) + ")")
        print("###############\n")

    def get_bound_str(self):
        string = ""
        for point in self.queue_neg + self.queue_pos:
            a, b = point.get_coord()
            string += point.p_type + " : (" + str(a) + ", " + str(b) + ")\n"
        return string


def get_xx_yy(coord1, coord2):
    return [coord1[0], coord2[0]], [coord1[1], coord2[1]]
