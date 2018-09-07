# merge sort algorithm

import math

A_ori = [1, 3, 5, 4, 2, 8, 6, 11]
print('original array is', A_ori)


def merge(A, p, q, r):
    L = A[p:q+1]
    R = A[q+1:r+1]
    L.append(math.inf)
    R.append(math.inf)
    i = 0
    j = 0
    for k in range(p, r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
    return A


def merge_sort(A, p, r):
    if p < r:
        q = math.floor((p+r)/2)
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)
    return A


A_new = merge_sort(A_ori, 0, 7)
print('sequenced array is', A_new)

# exercise 2.3.7
# find if exists a,b in S, so that a given integer x = a + b
# algorithm time should be within Theta(nlogn)

# solution 1


def check_sum1(A, x):
    n = len(A)
    i = 0
    j = n - 1
    while i < j:
        if A[i] + A[j] == x:
            # return i, j
            return True
        if A[i] + A[j] > x:
            j -= 1
        else:
            i += 1

    return False


# solution 2


def check_sum2(A, S, x):
    for i in range(len(S)):
        ans = bin_search(A, 0, len(S)-1, x - S[i])
        if ans is True:
            return True
    return False


def bin_search(A, p, q, x):
    ans = False
    if p<q:
        if x == A[math.floor((p+q)/2)]:
            return True
        elif x < A[math.floor((p+q)/2)]:
            temp_ans1 = bin_search(A, p, math.floor((p+q)/2), x)
            if temp_ans1 is True:
                return True
        elif x > A[math.floor((p+q)/2)]:
            temp_ans2 = bin_search(A, math.floor((p+q)/2)+1, q, x)
            if temp_ans2 is True:
                return True
        # ans = (temp_ans1 or temp_ans2)
    return ans


sol2 = check_sum2(A_new, A_ori, 4)
print('solution 2 is', sol2)


