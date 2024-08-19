# Author: Khrystian Clark
# Date: 11/18/2020
# Description:

def count_seq():
    first = "12"
    print("2, 12" + ", ") # Print the first two numbers
    while True:
        show = ""
        count = 1
        prev = first
        for i in range(3, len(first)+1):
            if i == (len(show) - 1):
                if first[2] == first[0]:
                    show += "11" + prev
                else:
                    show += str(count) + first[i]
            if first[i+1] == first[i]:
                count += 1
            else:
                show += str(count) + prev
                count = 1
                prev = first[i+1]
        first = show
        print(first + ", ")

count_seq()
