def ffactorial (n):
    factorial = 1
    if n >= 0:
        while n > 1:
            factorial *= n
            n -= 1
        return(f'факториал числa равен {factorial}')
    else:
        return("вы ввели некорректное число")

