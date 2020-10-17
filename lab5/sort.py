import time

def time_decorator(func):
    def inner(*args, **kwargs):
        t = time.time()
        output = func(*args, **kwargs)
        print("Elapsed Time : ", time.time() - t, "sec")
        return output
    return inner


@time_decorator
def insertion_sort(L):
    n = len(L)
    for i in range(n):
        current_value = L.pop(i) # current value that we want to sort

        last = True # if current_value belongs to last position of the ordered list
        for j in range(i):
            if L[j] >= current_value:
                last = False
                L.insert(j, current_value) # put in ordered position
                break
        
        if last == True:
            L.insert(i, current_value) # if bigger than every ordered number, put in last position
        
        assert n == len(L)

    return L


@time_decorator
def merge_sort(L):
    return __merge_sort(L) 
    # decorator makes recursive calls decorative, so we make another non-decorative function to avoid getting time information in recursive calls

def __merge_sort(L):
    n = len(L)

    if n == 1: # base case
        return L

    # divide L into half: sublist A, B
    A = L[: n // 2]
    B = L[n // 2 :]

    # merge sort A and B individually
    A = __merge_sort(A)
    B = __merge_sort(B)

    # merge A and B
    i = 0 # index of A
    j = 0 # index of B
    for k in range(n): # index of L
        # if we spent all of either A or B, just add the remaining elements of the other list to L
        if i >= len(A):
            L[k:] = B[j:]
            return L
        if j >= len(B):
            L[k:] = A[i:]
            return L

        # add each element of L using the comparison of smallest unused value of A and B
        if A[i] <= B[j]:
            L[k] = A[i]
            i += 1
        else:
            L[k] = B[j]
            j += 1
    
    return L


