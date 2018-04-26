print("""*****
Input please vector (n,k,t)
public key  = (G^,t), where G^ = SGP
S - det!=0 k*k matrix
G - k*n matrix
P - swap n*n marix
***""")


n,k,t = eval(input())   # input vector values



if( type(n) != int and type(k) != int and type(t) != int ):   # Check incorrect input
    print("vector elements not int")
    exit(1)


import numpy
import random

# Make random matrix S

while(1):
    row_S = []
    S = []
    for j in range(k):
        for i in range(k):
            row_S.append(random.randint(0,1))
        S.append(row_S)
        row_S = []
    if(numpy.linalg.det(S) != 0):
        break

print("""\n*****Matrix S*****\n""")

for i in range(k):
    print(*(S[i]))

print("\ndet(S) = ",numpy.linalg.det(S))
print("\n\n\n")

# Done Matrix S

# Make Matrix G and P TODO
