from check_if_prime import check_if_prime

for x in range(0, 80):
    # n = (x**2 + x + 41)
    n = (x**2 - (79 * x) + 1601)
    if (check_if_prime(n)):
        print (str(x) + " :: " + str(n))

print(str(-79) + " * " + str(1601) + " = " + str(-79*1601))

highest_consecutive_primes = 0

for a in range(-999, 1000):
    for b in range(-1000, 1001):
        # maximum number of primes for consecutive values of n
        consecutive_primes = 0
        while True:
            n = consecutive_primes
            if not (check_if_prime(n**2 + (a * n) + b)):
                break
            else:
                consecutive_primes = consecutive_primes + 1
            if (consecutive_primes > highest_consecutive_primes):
                highest_consecutive_primes = consecutive_primes
                print("New record! :: a = " + str(a) + ", b = " + str(b) + ", consec = " + str(consecutive_primes))
                print("a * b = " + str(a*b))
        

