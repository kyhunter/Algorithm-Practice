# insertion sort practice
# exercises from introductions to algorithms 3rd edition

import numpy as np
import math

A = np.array([15, 26, 34, 31, 57, 93, 27])


# ascending order, 2.1
for j in range(1, np.size(A)):
    key = A[j]
    i = j - 1
    while (i > -1) and (A[i] > key):
        A[i+1] = A[i]
        i = i-1
    A[i+1] = key

print('Ascending order A is', A)


# descending order, exercise 2.1-2
for j in range(1, np.size(A)):
    key = A[j]
    i = j - 1
    while (i > -1) and (A[i] < key):
        A[i+1] = A[i]
        i = i-1
    A[i+1] = key

print('Descending order A is', A)


# find the index of a number v from A, exercise 2.1-3
v = 32
quitflag = 0
for j in range(np.size(A)):
    key = v
    if A[j] == key:
        quitflag = 1
        break

if quitflag == 0:
    print('v is not in A')
else:
    print('index is', j+1)
# or if def as a function, use return instead of quitflag


# sum of two n-bit binary integers, 2.1-4

A = [1, 0, 1, 0, 1, 0, 1]
B = [1, 1, 1, 0, 0, 1, 0]
C = []

n = len(A)
carry = 0
for i in range(n-1, -1, -1):
    C.append((A[i] + B[i] + carry) % 2)
    carry = math.floor((A[i] + B[i] + carry) / 2)

C.append(carry)
C.reverse()
print('C is', C)



