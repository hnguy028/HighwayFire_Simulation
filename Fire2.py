import copy
from BPoint import *

class Fire2:

    left = [0, 0]
    center = [0, 0]
    right = [0, 0]

    l1 = None
    l2 = None

    r1 = None
    r2 = None

    r_state = -1
    l_state = -1

    cs = 0
    qs = 0

    cst = [0]
    qst = [0]

    t = 0
    queue = []

    def __init__(self):
        self.queue = [BPoint()]

    def increment(self, barrier_set):
        # for each BPoint -> BPoint.move(barrier_set)
        pass

    def get_boundary(self):
        boundary = []

        p, q = get_xx_yy(self.center, self.right)
        boundary.append((p, q))

        p, q = get_xx_yy(self.center, self.left)
        boundary.append((p, q))

        if self.r2:
            if self.r1:
                p, q = get_xx_yy(self.right, self.r1)
                boundary.append((p, q))

                p, q = get_xx_yy(self.r1, self.r2)
                boundary.append((p, q))

            else:
                p, q = get_xx_yy(self.right, self.r2)
                boundary.append((p, q))

        if self.l2:
            if self.l1:
                p, q = get_xx_yy(self.left, self.l1)
                boundary.append((p, q))

                p, q = get_xx_yy(self.l1, self.l2)
                boundary.append((p, q))

            else:
                p, q = get_xx_yy(self.left, self.l2)
                boundary.append((p, q))
        #
        # boundary.append((self.l1, self.l2))
        # boundary.append((self.left, self.l1))

        #
        # boundary.append((self.r1, self.r2))
        # boundary.append((self.right, self.r1))

        return boundary


def get_xx_yy(coord1, coord2):
    return [coord1[0], coord2[0]],[coord1[1], coord2[1]]
