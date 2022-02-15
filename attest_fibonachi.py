
def nfib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

while True:
    try: 
        max_n = int(input("Введите максимальное количество чисел последовательности Фибонначи: "))
        break
    except ValueError:
        print("Введено не integer!")    
        
fib_list = nfib(max_n)
print(f"Запись последовательности чисел с помощью функции list:\n{list(fib_list)}")

fib_for_list = []
for i in nfib(max_n):
    fib_for_list.append(i)
print(f"Запись последовательности чисел с помощью цикла for:\n{fib_for_list}")

gen_fib_list = [x for x in nfib(max_n)]
print(f"Запись последовательности чисел с помощью генератора списка:\n{gen_fib_list}")

gen_plenty_fib = {x for x in nfib(max_n)}
print(f"Запись последовательности чисел с помощью генератора списка:\n{gen_plenty_fib}")

             
