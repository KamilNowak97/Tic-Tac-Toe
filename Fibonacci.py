#! /usr/bin/python3

def fibonacci():
    count = int(input("Write amount of numbers to generate: "))
    i = 1
    if count == 0:
        fib_tab = []
    elif count == 1:
        fib_tab = [1]
    elif count == 2:
        fib_tab = [1,1]
    elif count > 2:
        fib_tab = [1,1]
        while i < (count-1):
            fib_tab.append(fib_tab[i]+fib_tab[i-1])
            i += 1
    return fib_tab

print("----------------------")
print("---Fibonacci number---")
print("----------------------\n")
print(fibonacci())

