def feedDog(hunger_level, biscuit_size):
    count = 0
    hunger_level.sort()
    biscuit_size.sort()
    for i in biscuit_size:
        if i in hunger_level:
            count += 1
            biscuit_size.remove(i)
            hunger_level.remove(i)
        for j in hunger_level:
            if (i >= j):
                count += 1
                i = i-j
                hunger_level.remove(j)
            if len(hunger_level) == 0:
                print (count)
    print (count)

feedDog([1,2,3], [1,1])
feedDog([2,1], [1,3,2])