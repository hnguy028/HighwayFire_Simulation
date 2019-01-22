from BPoint import *


class Fire:

    cs = 0.0
    qs = 0.0

    cst = [0]
    qst = [0]

    t = 0.0
    time_step = 1.0
    queue_pos = []
    queue_neg = []

    def __init__(self, time_step=1):
        self.time_step = time_step
        self.queue_neg = [BPoint("TYPE2", direction=-1, time_step=self.time_step)]
        self.queue_pos = [BPoint("CENTER", time_step=self.time_step),
                          BPoint("TYPE2", time_step=self.time_step)]

    def increment(self, barrier_set):
        self.t += self.time_step

        csp = 0.0

        i = 0
        prev_length = len(self.queue_neg)

        while i < len(self.queue_neg):
            csp += self.queue_neg[i].move(barrier_set, self.queue_neg)

            if prev_length - 1 == len(self.queue_neg):
                i -= 1

            i += 1
            prev_length = len(self.queue_neg)

        i = 0
        prev_length = len(self.queue_pos)

        while i < len(self.queue_pos):
            csp += self.queue_pos[i].move(barrier_set, self.queue_pos)

            if prev_length - 1 == len(self.queue_pos):
                i -= 1

            i += 1
            prev_length = len(self.queue_pos)

        self.cs += csp
        self.cst.append(self.cs)

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


def get_xx_yy(coord1, coord2):
    return [coord1[0], coord2[0]],[coord1[1], coord2[1]]
