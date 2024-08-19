def dna_match_bottomup(DNA1, DNA2):
    m = len(DNA1)
    n = len(DNA2)

    cache = [[0 for x in range(n+1)] for x in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                cache[i][j] = 0
            elif DNA1[i-1] == DNA2[j-1]:
                cache[i][j] = cache[i-1][j-1] + 1
            else:
                cache[i][j]= max(cache[i-1][j] , cache[i][j-1])

    return cache[m][n]

DNA1 = "ATAGTTCCGTCAAA"
DNA2 = "GTGTTCCCGTCAAA"
print(dna_match_bottomup(DNA1, DNA2))