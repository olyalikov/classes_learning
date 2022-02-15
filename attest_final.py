import random as r
import time

def nask(amin = 20, amax = 1000):
    while True:
        try:
            user_input = int(input(f"Задайте количество точек для сортировки в интервале от {amin} до {amax}: "))
            if user_input < amin:
                print(f"Значение должно быть больше минимального значения по умолчанию {amin}! Повторите ввод.")
                continue
            if user_input > amax:
                print(f"Значение должно быть меньше максимального значения по умолчанию {amax}! Повторите ввод.")
                continue 
        except:
            print("Значение не является числом! Повторите ввод.")
        else:
            return user_input
        
def bub_sort(a):
    i = 0
    start_time = time.process_time()
    while i < len(a) - 1:
        j = 0
        while j < len(a) - 1 - i:
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
            j += 1
        i += 1
    list_left = a[:10]
    list_right = a[-10:]     
    pt = (time.process_time() - start_time)    
    print(f"Отсортированный список:\n{a}")
    print(f"Время сортировки:\n{pt:0.3f} секунд")    
    print(f"10 минимальных чисел:\n{list_left}")
    print(f"10 максимальных чисел:\n{list_right}")
    
nums = nask(50,70)
rand_list = list(r.randint(10000,99999) for n in range(nums))
print(f"Исходный список:\n{rand_list}")
print(f"Количество чисел в списке:\n{nums}")
bub_sort(rand_list)
