def fibonacci(n, m):
    
    fib_i, fib_n = 1, 1
    fib = []
    
    for x in range (1, m + 1):
        if x >= n:
            fib.append(fib_i)
        fib_i, fib_n = fib_n, fib_i + fib_n
    return fib

print(fibonacci(10, 20))
        
