def amount(A, S):
    result = []
    count = len(A)+1
    s_holder = 0
    A.sort()
    return(amount_helper(A, S, result, count, s_holder))

def amount_helper(A, S, result, count, s_holder):
    stored = []
    if (S == s_holder) and (result.sort() not in stored): # of the target sum is reached
        print(result)
        stored.append(result.sort())
        return
    for i in range(0, len(A), 1):
        if (s_holder + A[i] > S): # if the tracking sum is greater than the target, reset.
            continue
        if (i > count) and (A[i] == A[i-1]):
            continue

        result.append(A[i]) # add the value to the result
        amount_helper(A, S, result, i-1, s_holder+A[i]) #iterate
        result.remove(result[len(result) - 1]) # pop the end of the result

A = [11,1,3,2,6,1,5]
S = 8
amount(A, S)