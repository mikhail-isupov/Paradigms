# Ленивые вычисления: Напишите функцию, которая будет генерировать бесконечную последовательность простых чисел. 
# Используйте ленивые вычисления, чтобы генерировать только те числа, которые действительно нужны.

def odd_numbers():
    primes = [2]
    while True:
        yield primes[-1]
        next_prime = primes[-1]
        is_prime_found = False
        while not is_prime_found:
            next_prime += 1
            is_prime_found = True
            for prime in primes:
                if next_prime % prime == 0:
                    is_prime_found = False
                    break
        primes.append(next_prime)

odds = odd_numbers()    

for i in range(100):
    print(next(odds))
