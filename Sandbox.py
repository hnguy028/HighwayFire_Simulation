##
#
##


if __name__ == '__main__':

    li = [0,1,2,3,4,5,6,7,8,9]

    # li.insert(4, 7)

    i = 0

    pr = len(li)

    while i < len(li):
        print(str(i) + " - " + str(len(li)) + " - " + str(li[i]))
        if i == 3:
            del li[i]
        if pr == len(li):
            i += 1
