def diffLoop():
    end0 = [23, 68.75, 206, 617.75, 1853]
    end1 = [41.75, 125, 374.75, 1124, 3371.75]
    start3 = [53, 158.75, 476, 1427.75, 4283]
    end3 = [62, 185.75, 557, 1670.75, 5012]

    de10 = []

    for i in range(len(end0)):
        de10.append(end1[i] - end0[i])

    s3_e0 = []
    for i in range(len(end0)):
        s3_e0.append(start3[i] - end0[i])

    _1int = []
    for i in range(len(end0)):
        _1int.append(end3[i] - end1[i])

    for i in range(len(end0) - 1):
        print(end3[i + 1] - end3[i])

    di = []
    for i in range(len(end0)):
        di.append(end3[i] - start3[i])

    # print(di)

    t1_t2 = []
    for i in range(len(end0)):
        t1_t2.append(start3[i] - end1[i])

    # for i in range(len(end0)):
    # 	print(str(t1_t2[i]/s3_e0[i]))

    slope = []
    # for i in range(len(end0)):
    # 	slope.append(_1int[i]/di[i])

    print(slope)
    for i in range(len(end0) - 1):
        slope.append((end1[i] - end0[i]) / (start3[i] - end0[i]))

    print(slope)


if __name__ == "__main__":
    diffLoop()

    l = [7, 20.75, 62.00, 185.750, 557.0000, 1670.75000, 5012.000000, 15035.7500000, 45107.00000000, 135320.750000000,
         405962.0000000000, 1217885.75000000000, 3653657.000000000000, 10960970.7500000000000, 32882912.00000000000000]

# for i in range(len(l)-1):
# 	print(l[i+1]-l[i])

