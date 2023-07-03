def findSmallOrBig(a):
    a.sort()
    print("biggest: ", a[-1])
    print("smallest: ", a[0])

a = [1,2,4,32,12,6,8]
findSmallOrBig(a)