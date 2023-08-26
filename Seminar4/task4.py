# Фибоначчи через рекурсию: Напишите рекурсивную функцию для вычисления числа Фибоначчи с индексом n. 

def fibo(n):
    if n >= 2:
        return fibo(n - 2) + fibo(n - 1)
    else:
        return n
    
print(fibo(3))
    