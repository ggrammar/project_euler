
# "all natural numbers below 10", so not including 10. this is range's default behavior. 
numbers = range(1, 1000000000)

total = 0

for i in numbers:
    if (
            (i % 3 == 0) or
            (i % 5 == 0)):
        total += i

print total

# This is correct. 
