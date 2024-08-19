def KthElement(Arr1, Arr2, k):
    newArr = []
    a = 0 #place in arr1
    b = 0 #place in arr2
    c = 0 #place in newArr
    m = len(Arr1)
    n = len(Arr2)
    
    # parse throught the sorted arrays and add each item in sorted order into the new array.
    while a < m and b < n:
        if Arr1[a] < Arr2[b]:
            newArr[c] = Arr1[a]
            c += 1
            a += 1
        if a == m-1 and b != n-1:
            newArr[c] = Arr1[b]
            c += 1
        if a != m-1 and b == n-1:
            newArr[c] = Arr1[a]
            c += 1
        if len(newArr) == m+n:
            return print(newArr[k])        
        else:
            newArr[c] = Arr2[b]
            c += 1
            b += 1
    # Return the printed value located at the kth place in the new array.
    return print(newArr[k])

Arr1 = [1,2,3,5,6];
Arr2 = [3,4,5,6,7];
k =  5;
KthElement(Arr1, Arr2, k);