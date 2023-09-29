def threesum(nums):
    lnum = len(nums)
    trips = []
    indk = 0
    for i in range(lnum):
        for j in range(i + 1, lnum):
            s = nums[i] + nums[j]
            for k in range(j + 1, lnum):
                if s + nums[k] == 0:
                    trips.append([nums[i], nums[j], nums[k]])
                    indk = k
                    continue
            if s + nums[indk] == 0:
                indk = 0
                continue
    lent = len(trips)
    tripd = []
    for i in range(lent):
        for j in range(i + 1, lent):
            if trips[i] == trips[j]:
                if j not in tripd:
                    tripd.insert(0, j)
            elif trips[i][0] == trips[j][1] and trips[i][1] == trips[j][2] and trips[i][2] == trips[j][0]:
                if j not in tripd:
                    tripd.insert(0, j)
            elif trips[i][0] == trips[j][2] and trips[i][1] == trips[j][0] and trips[i][2] == trips[j][1]:
                if j not in tripd:
                    tripd.insert(0, j)
            elif trips[i][0] == trips[j][0] and trips[i][1] == trips[j][2] and trips[i][2] == trips[j][1]:
                if j not in tripd:
                    tripd.insert(0, j)
            print(tripd, i, j, trips)
    for i in tripd:
        trips.pop(int(i))
    return trips


print(threesum([-1, 0, 1, 2, -1, -4]))
