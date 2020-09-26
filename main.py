# Author:  David Mena

# imports
import decimal  # to handle very big numbers

# initial values
n = 1056048717
m = 0
# limit num of calculations, gives the precision
limit = 200000

# find m from the equation:  n-1 = 2^k*m
k = 0
# run until result of division is not an integer
result = 0
while result == 0:
    result = (n-1) % (2**k)
    if result == 0:
        m = (n-1)//(2**k)
        k += 1

# pick an a in the range of: 1 < a < n-1
a = 2

# Calculate the cases of primarity
# for b0: b0 = a^m mod n
b = (a**m) % n
count = 1
if(abs(b) == 1):  # probably prime if b is -1 or +1
    print("The number is PROBABLY prime!")
else:
    # for b1 to bn, stops when b == 1 or b == n-1 or limit encountered
    # b==-1 in mod is the same as b == n-1
    while b != 1 and b != (n-1) and count != limit:
        b = (b**2) % n
        count += 1
    # get final results of primarity testing for b to bn
    print(count)
    if(b == n-1):
        print("The number is PROBABLY prime!")
    if(b == 1 or count == limit):
        print("The number is composite")
