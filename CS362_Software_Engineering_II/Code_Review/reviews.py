# Pull request 1
def my_func(x, y):


    return x**y 


# Pull request 2
def create_odds(num):
    """Creates a list of len(num) of random odd numbers between 1 and 1000"""
    num_list = []
    for i in range(0, num):
        new_num = 2
        while new_num % 2 == 0:
            new_num = random.randint(1, 1000)
        num_list.append(new_num)
    return num_list


def create_evens(num):
    """Creates a list of len(num) of random even numbers between 1 and 1000"""
    num_list = []
    for i in range(0, num):
        new_num = 1
        while new_num % 2 != 0:
            new_num = random.randint(1, 1000)
        num_list.append(new_num)
    return num_list


# Pull request 3
def check_for_val(self, val):
    """This member function checks to see if val exists in the class member
    values and returns True if found"""
    found = False
    for i in range(len(self.values)):
        if self.values[i] == val:
            found = True
    return found


# Pull request 4
def get_val_index(arr, val):
    """Searches arr for val and returns the index if found, otherwise -1"""
    index = -1
    for i in range(len(arr)):
        if arr[i] == val:
            index = i
            break
    return index


# Pull request 5
def double_array(arr):
    """sort the list (ascending) and double the value of each element of
       the list and return without changing the state of the original list"""
    arr.sort()
    for i in range(len(arr)):
        arr[i] = arr[i] * 2
    return arr
        