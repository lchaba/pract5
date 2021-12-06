def fib(a):
    x = 1
    if a > 2:
        x = fib(a-1) + fib(a-2)
    return x
try:     
    el = int(input("введите номер нужного значения: "))
except ValueError:   
    print("вы должны ввести число")  
v = fib(el)
print('число фибоначчи равно ' + str(v))