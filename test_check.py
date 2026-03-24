def emeraldbuy(n, x):
    max_consec = 0
    current_consec = 0
    for i in range(n):
        if (x[i]%2) == 0:
            current_consec += x[i]
            if current_consec > max_consec:
                max_consec = current_consec
        else:
            current_consec = 0
    print(max_consec)
emeraldbuy(13,[2,3,4,4,5,6,1,2,2,2,1,8,2])