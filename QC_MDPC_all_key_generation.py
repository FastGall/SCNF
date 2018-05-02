import random
import numpy as np
from binmatrix import BinMatrix
from functools import reduce
print("""
n = 9602, r = 4801, w = 90, t = 84, n0 = 2, Level security - 80""")

# Generate a parity check matrix H (private key)
r = 4801
w = 90

once_range = [i for i in range(r+1)]   # For make random '1' sequence

while(1):
    weight_sequence = random.sample(once_range, w)   # Random index for '1'

    H_first_row = []

    for i in range(r):
        if(i in weight_sequence):    # w = 90, make 90 '1'
            H_first_row.append(1)
        else:
            H_first_row.append(0)

    H0_matrix = [[] for i in range(r)]

    for i in range(r):
        H0_matrix[i] = H_first_row[i:] + H_first_row[:i]
    H0_matrix_m = H0_matrix
    H0_matrix = BinMatrix(H0_matrix)
    if(H0_matrix.det()):
        break


while(1):
    weight_sequence = random.sample(once_range, w)   # Random index for '1'

    H_first_row = []

    for i in range(r):
        if(i in weight_sequence):
            H_first_row.append(1)
        else:
            H_first_row.append(0)

    H1_matrix = [[] for i in range(r)]

    for i in range(r):
        H1_matrix[i] = H_first_row[i:] + H_first_row[:i]
    H1_matrix_m = H1_matrix
    H1_matrix = BinMatrix(H1_matrix)
    print(H1_matrix.det())
    if(H1_matrix.det()):
        break

H = np.hstack((H0_matrix_m,H1_matrix_m))    # private key



# Generate a generator matrix


H1_inverse_on_map = H1_matrix.inv()

H1_inverse = [[] for i in range(r)]

for i in range(len(H1_inverse_on_map)):
    for j in H1_inverse_on_map[i]:
        H1_inverse[i].append(j)

H1_inverse = np.array(H1_inverse)

H1_matrix_m = np.array(H1_matrix_m)

H0_matrix_m = np.array(H1_matrix_m)

Q_matrix = H1_inverse*H0_matrix_m

Q_matrix = Q_matrix.transpose()

# Make a diag matrix

pointer = 0
row_I = []
I = []

for i in range(r):     # Diag matrix
    for j in range(r):
        if j == pointer:
            row_I.append(1)
        else:
            row_I.append(0)
    I.append(row_I)
    pointer += 1
    row_I = []

I = np.matrix(I)

G = np.hstack((I,Q_matrix))   # Public key

print("""#*****\nPublic key (G,t), where t = 84, G = \n""")

print(G)

print("""\n*****\nPrivate key H\n""")

print(H,"\n*****")


# SLAU

H = H.transpose()


SLAU = G*H


# print(SLAU[0])


