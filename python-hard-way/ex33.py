def print_multiples(start, finish, inc):
    i = start
    numbers = []

    while i < finish:
        numbers.append(i)

        i = i + inc
        print "Numbers now: ", numbers

print_multiples(6,100,9)

