import random
import numpy

print("""*****\nn = 9601, k = 4801, w = 90, t = 84
Make a PUBLIC QC-MDPC McEliece key, where n = 2p, k = p, w = row weight, t = dec error\n\n*****\n""")

# Part 1. Make two random vectors, h0 and h1, len(h0) = len(h1) = k, weight = w

k = 4801
w = 90

rrange = [i for i in range(k+1)]   # For make random '1' sequence
weight_sequence = random.sample(rrange, w)   # Random index for '1'

h1 = []

for i in range(k):
    if i in weight_sequence:
        h1.append(1)
    else:
        h1.append(0)      # Make h1 vector

weight_sequence = random.sample(rrange, w)   # Random index for '1'

h0 = []

for i in range(k):
    if(i in weight_sequence):
        h0.append(1)
    else:
        h0.append(0)     # Make h0 vector

# Part 2. mul (h0)*T and h1

h0 = numpy.matrix(h0)

h0 = h0.transpose()      # Make and transpose vector(matrix(h0))

h1 = numpy.matrix(h1)

Q = h0*h1   # 1/2 of G matrix

# Part 3. Make diag matrix I

pointer = 0
row_I = []
I = []

for i in range(k):     # Diag matrix
    for j in range(k):
        if j == pointer:
            row_I.append(1)
        else:
            row_I.append(0)
    I.append(row_I)
    pointer += 1
    row_I = []

I = numpy.matrix(I)

G = numpy.hstack((I,Q))

print("""Matrix G\n\n""")

print(G,"\n\n")

print("""Public key is (G,t), where t = 84\n\n*****\n\n""")


