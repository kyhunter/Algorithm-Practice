# introduction to algorithms chapter 4.1

import math


A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]


def find_maximum_subarray(A, p, r):
    if p == r:
        return p,r, A[p]
    else:
        q = math.floor((p + r) / 2)
        left_left, left_right, left_sum = find_maximum_subarray(A, p, q)
        right_left, right_right, right_sum = find_maximum_subarray(A, q+1, r)
        c_left, c_right, c_sum = find_max_crossing_subarray(A, p, q, r)
        if (left_sum > right_sum) and (left_sum > c_sum):
            return left_left, left_right, left_sum
        elif (right_sum > left_sum) and (right_sum > c_sum):
            return right_left, right_right, right_sum
        else:
            return c_left, c_right, c_sum


def find_max_crossing_subarray(A, p, q, r):
    left_sum = -math.inf
    sum = 0
    left_ind = q
    for i in range(q, p-1, -1):
        sum += A[i]
        if sum > left_sum:
            left_sum = sum
            left_ind = i

    right_sum = -math.inf
    sum = 0
    right_ind = q+1
    for j in range(q+1, r+1):
        sum += A[j]
        if sum > right_sum:
            right_sum = sum
            right_ind = j

    sum_all = left_sum + right_sum
    return left_ind, right_ind, sum_all

ind_left, ind_right, sum_array = find_maximum_subarray(A, 0, len(A)-1)
print('maximum subarray starts from', ind_left, 'to', ind_right, 'with sum', sum_array)

