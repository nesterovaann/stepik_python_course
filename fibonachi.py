# Дано целое число 1=< n =< 40, необходимо вычислить n-е число Фибоначчи

def fib(n):
    fib_list = []
    fib_list.append(int(0))
    fib_list.append(int(1))
    for i in range(2, n+1):
        fib_list.append(int(fib_list[i - 2]) + int(fib_list[i - 1]))
    return fib_list[n]
    
    
#Найти последнюю цифру n-го числа Фибоначчи

def fib_digit(n):
    fib_list = []
    fib_list.append(int(0))
    fib_list.append(int(1))
    for i in range(2, n+1):
        fib_list.append((fib_list[i-2]+fib_list[i-1])%10)
    return fib_list[n]
    
 #Необходимо найти остаток от деления n-го числа Фибоначчи на m
 
 def fib_mod(n, m):
    #find Pisano period
    pisano = []
    fib = []
    if n == 1:
        return 0
    if n == 2:
        return 1
    pisano.append(0)
    pisano.append(1)
    f0 = 0
    f1 = 1
    for i in range(2,n+1):
        f0, f1 = f1, (f0+f1)%m
        pisano.append(f1 % m)
        if (i >= 3) and (pisano[i-2] == 0) and (pisano[i-1] == 1):
            l = len(pisano)-3
            return pisano[n%l]
            break
    print(pisano)
    l = len(pisano)
    return pisano[n%l]
