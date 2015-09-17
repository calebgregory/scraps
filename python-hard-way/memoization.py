def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)

def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper


fib = memoize(fib)

print(fib(40))

class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}
    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]

# there is also a decoration syntax @ . . .

def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper

@memoize
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# fib = memoize(fib)

def argument_test_natural_number(f):
    def helper(x):
        if type(x) == int and x > 0:
            return f(x)
        else:
            raise Exception("Argument is not an integer > 0")
    return helper

@argument_test_natural_number
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

for i in range(1,10):
    print(i, factorial(i))

# print(factorial(-1)) raises an exception

# on a two-sided scale, weigh quantities from 1 to 40 lbs
# what is the least number of weights that can be used on a balance scale to weigh any of these quantities?
# a first idea might be to use weights of 1,2,4,8,16,32 lb
#   this is a minimal number if we restrict ourselves to put weights on one side
# but it is possible to put weights on both sides of the scale
#   now, we need only four weights: 1,3,9,27
# TODO: write a function weigh(), which calculates the weights needed and their distribution on the pans to weigh any amount from 1 to 40.

# weight  left    right
# 1       1               0001 - 0000
# 2       3       1       0010 - 0001
# 3       3               0010 - 0000
# 4       3,1             0011 - 0000
# 5       9       3,1     0100 - 0011
# 6       9       3       0100 - 0010
# 7       9,1     3       0101 - 0010
# 8       9       1       0100 - 0001
# 9       9               0100 - 0000
# 10      9,1             0101 - 0000
# 11      9,3     1       0110 - 0001
# 12      9,3             0110 - 0000
# 13      9,3,1           0111 - 0000
# 14      27      9,3,1   1000 - 0111
# 15      27      9,3     1000 - 0110
# 16      27,1    9,3     1001 - 0110
# 17      27      9,1     1000 - 0101
# 18      27      9       1000 - 0100
# 19      27,1    9       1001 - 0100
# 20      27,3    9,1     1010 - 0101
# 21      27,3    9       1010 - 0100
# 22      27,3,1  9       1011 - 0100
# 23      27      3,1     1000 - 0011
# 24      27      3       1000 - 0010
# 25      27,1    3       1001 - 0010
# 26      27      1       1000 - 0001
# 27      27              1000 - 0000
# 28      27,1            1001 - 0000
# 29      27,3    1       1010 - 0001
# 30      27,3            1010 - 0000
# 31      27,3,1          1011 - 0000
# 32      27,9    3,1     1100 - 0011
# 33      27,9    3       1100 - 0010
# 34      27,9,1  3       1101 - 0010
# 35      27,9    1       1100 - 0001
# 36      27,9            1100 - 0000
# 37      27,9,1          1101 - 0000
# 38      27,9,3  1       1110 - 0001
# 39      27,9,3          1110 - 0000
# 40      27,9,3,1        1111 - 0000

def factors_set():
    factors_set = ( (i,j,k,l) for i in [-1,0,1]
            for j in [-1,0,1]
            for k in [-1,0,1]
            for l in [-1,0,1])
    for factor in factors_set:
        yield factor

def memoize(f):
    results = {}
    def helper(n):
        if n not in results:
            results[n] = f(n)
        return results[n]
    return helper

@memoize
def linear_combination(n):
    """ returns the tuple (i,j,k,l) satisfying
        n = i*1 + j*3 + k*9 + l*27 """
    weights = (1,3,9,27)

    for factors in factors_set():
        sum = 0
        for i in range(len(factors)):
            sum += factors[i] * weights[i]
        if sum == n:
            return factors

def weigh(pounds):
    weights = (1,3,9,27)
    scalars = linear_combination(pounds)
    left = ""
    right = ""
    for i in range(len(scalars)):
        if scalars[i] == -1:
            left += str(weights[i]) + " "
        elif scalars[i] == 1:
            right += str(weights[i]) + " "
    return (left,right)

for i in [2,3,4,5,7,8,9,20,40]:
    pans = weigh(i)
    print("Left pan: " + str(i) + " plus " + pans[0])
    print("Right pan: " + pans[1] + "\n")
