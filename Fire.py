import copy


class Fire:

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

    def __init__(self):
        pass

    def increment(self, barrier_set):
        # center
        self.t += 1
        self.center[1] += 1

        # right
        # right boundary point intersects with a barrier
        if self.right[0] in [b[0] for b in barrier_set]:
            barrier = barrier_set[[b[0] for b in barrier_set].index(self.right[0])]

            # right boundary point is at the top of a barrier (the beginning of a 0-interval)
            if barrier[1] == self.right[1]:
                # reset r2
                self.r2 = copy.deepcopy(self.right)

                self.right[0] += 1

            else:
                # reset r1
                if not self.r1 and self.r_state == 0:
                    self.r1 = copy.deepcopy(self.right)

                self.right[1] += 1

                # increment cst counter
                self.cs += 1

            # change state to barrier
            self.r_state = 1

        else:
            self.right[0] += 1

            # change state to free
            self.r_state = 0

            if self.right[1] == 0:
                self.cs += 1

        # left
        # left boundary point intersects with a barrier
        if self.left[0] in [b[0] for b in barrier_set]:
            barrier = barrier_set[[b[0] for b in barrier_set].index(self.left[0])]

            # left boundary point is at the top of a barrier (the beginning of a 0-interval)
            if barrier[1] == self.left[1]:
                # reset l2
                self.l2 = copy.deepcopy(self.left)

                self.left[0] -= 1

            else:
                # reset l1
                if not self.l1 and self.l_state == 0:
                    self.l1 = copy.deepcopy(self.left)

                self.left[1] += 1

                # increment cst counter
                self.cs += 1

            # change state to barrier
            self.l_state = 1

        else:
            self.left[0] -= 1

            # change state to free
            self.l_state = 0

            if self.left[1] == 0:
                self.cs += 1

        # r2
        if self.r2:
            if self.r2[1] > 0:
                self.r2[1] -= 1
            else:
                self.r2[0] += 1

                # not sure if this always increments cst
                self.cs += 1

                # hit barrier
                self.r2 = None if self.r2[0] in [b[0] for b in barrier_set] else self.r2
        # l2
        if self.l2:
            if self.l2[1] > 0:
                self.l2[1] -= 1
            else:
                self.l2[0] -= 1

                # not sure if this always increments cst
                self.cs += 1

                # hit barrier
                self.l2 = None if self.l2[0] in [b[0] for b in barrier_set] else self.l2

        # r1
        if self.r1:
            if self.r1[1] > 0:
                self.r1[1] -= 1

                self.cs += 1
            else:
                self.r1 = None

        # l1
        if self.l1:
            if self.l1[1] > 0:
                self.l1[1] -= 1

                self.cs += 1
            else:
                self.l1 = None

        self.cst.append(self.cs)

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
