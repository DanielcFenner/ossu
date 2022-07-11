def genPrimes():
    number = 2
    primes = []
    while True:

        prime = False
        while prime == False:
            prime = True
            for i in range(2, number - 1):
                if number % i == 0:
                    prime = False
            number += 1

        primes.append(number - 1)
        yield primes[-1]

gen = genPrimes()


for i in range(6):
    print(gen.__next__())