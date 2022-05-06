def maximum(interval):
    si = sorted(interval)
    # print(si)
    cnt = 0
    a = []
    for i in si:
        # print(i)
        s = 0
        e = len(i) - 1
        if a:
            if a[0] <= i[s]:
                a.pop(0)
        a.append(i[e])
    cnt = max(len(a), cnt)
    return (cnt)


# l=[[30, 75], [0, 50], [60, 150]]
# l=[(2, 7)]
l = [[10, 30], [5, 10], [5, 6], [15, 20]]
print(maximum(l))
