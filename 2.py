
def generate_fibonacci_sequence(n):
    retval = [1, 2]
    for i in (range(1, n - 1)):
        retval.append(retval[i - 1] + retval[i])

    return retval

# 32 is a magic number, it's how many numbers there are in the fibonacci
# sequence before we exceed 4,000,000. 
fibs = (generate_fibonacci_sequence(32))
fibs_sum = 0

for f in fibs:
    if (f % 2 == 0):
        fibs_sum += f

print(fibs_sum)

# This is correct.  I think my fib sequence function needs some love. I think
# there's a way to do a list comprehension to get the same sum effect in a very
# concise, pythonic, way, but I don't really care about that right now. 
