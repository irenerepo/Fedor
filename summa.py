def ssummaa(n):
    #удалила инпут н
    i = 1
    s = 0
    if n >= 0:
        while i <= n:
            s = i + s
            i = i + 1
    else:
        while i >= n:
            s = s + i
            i = i + (-1)
    return f'Сумма всех чисел от 0 до {n}: {s}'
