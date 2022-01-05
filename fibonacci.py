def fib(n):
    res = [0]
    fib1 = fib2 = 1
    if n >= 0:
        res.append(fib1, fib2)
        for  i in range (2, n):
            fib1, fib2 = fib2, fib1 +fib2
            print(fib2, end=' ')
    else:
        print("вы ввели некорректное число")
    return fib1, fib2