
# "all natural numbers below 1000", so not including 10. this is range's default behavior. 
numbers = range(1, 1000)

total = 0

for i in numbers:
    if (
            (i % 3 == 0) or
            (i % 5 == 0)):
        total += i

print total

# This is correct. 
# The PDF you get after finding the answer notes that it's more efficient to:
#   Find the sum of numbers divisible by 3.
#   Find the sum of numbers divisible by 5.
#   Subtract the sum of numbers divisible by 15. 
# This way, we don't have to look at every number - we can just look at every third
# number, every 5th number, and every 15th number. 

# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 # look at 20 numbers
#     3     6     9       12       15       18       # look at 6 numbers
#         5         10             15             20 # look at 4 numbers
#                                  15                # look at 1 number

# So, you're looking at like half as many numbers. 

# We do need to adjust the starting number for the range function, otherwise we'll
# get like "1, 4, 7, 10" for numbers divisible by three. 
nums_three   = range(3, 1000, 3)
nums_five    = range(5, 1000, 5)
nums_fifteen = range(15, 1000, 15)

print( (sum(nums_three)) + (sum(nums_five)) - (sum(nums_fifteen)) )

# So, that's definitely faster. The PDF also notes a generic solution like this:
# 3 + 6 + 9 + 12 + ... + 999
# 3 * (1 + 2 + 3 + 4 + ... + 333)

# 5 + 10 + 15 + 20 + ... + 995
# 5 * (1 + 2 + 3 + 4 + ... + 199)

# 1 + 2 + 3 + 4 + ... + p
# 1/2(p * (p + 1))

# n * (1 + 2 + 3 + 4 + ... + p)
# n * 1/2(p * (p + 1))

# We can implement this and skip range() entirely, just linear time calculations. 
def get_sum(target, iterate_by):
    # When we're counting by ones, what's the biggest number?
    small_target = target / iterate_by

    return ((iterate_by * (small_target * (small_target + 1))) / 2)

# We need to use 999 rather than 1000 here, because we're no longer using the range
# function - we're dividing by the iterator to determine how high we need to go. So,
# for 5 and 15, using "1000" will get us the wrong answer. 
print( (get_sum(999, 3)) + (get_sum(999, 5)) - (get_sum(999, 15)) )
