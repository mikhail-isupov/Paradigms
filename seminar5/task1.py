# Напишите программу, которая находит все простые числа в заданном диапазоне.
def odd_numbers(max, min = 2):
    primes = [2] # начальное простое число
    for number in range(2, max + 1): # проверяем числа все до max на простоту
        is_number_prime = True
        for prime in primes:
            if not number % prime:
                is_number_prime = False
                break
            if prime > number ** 0.5:
                break 
        if is_number_prime:
            primes.append(number)
    return(list(filter(lambda n: n >= min, primes)))

print(odd_numbers(100, 10))

