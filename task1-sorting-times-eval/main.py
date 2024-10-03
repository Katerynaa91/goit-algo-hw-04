import random
import timeit
import numpy as np
import matplotlib.pyplot as plt
import merge_insertion_modules

random.seed(42)

sorts = {'merge': [],
         'insertion': [],
         'sorted': [],
         'sort': []}
data_len = [100, 1000, 10000]

# Час виконання сортування злиттям
for i in data_len:
    arr_100 = [random.randint(1, 1000) for _ in range(1, i+1)]
    st = '''
import random
from merge_insertion_modules import merge_sort'''
    stm = f'''
merge_sort({arr_100})'''
    mrg_time = timeit.timeit(setup= st, stmt=stm, number=1)
    sorts['merge'].append(mrg_time)
    print(f'Merge sort took {mrg_time:.5f} seconds to sort {i} numbers')


# Час виконання сортування вставками
for i in data_len:
    arr_100 = [random.randint(1, 1000) for _ in range(1, i+1)]
    st = '''
import random
from merge_insertion_modules import insertion_sort'''
    stm = f'''
insertion_sort({arr_100})'''
    ins_time = timeit.timeit(setup= st, stmt=stm, number=1)
    sorts['insertion'].append(ins_time)
    print(f'Insertion sort took {ins_time:.5f} seconds to sort {i} numbers')

# Insertion Sort took 268.02570 seconds to sort 100000 numbers


# Час виконання сортування через вбудовану функцію SORTED()
for i in data_len:
    arr_100 = [random.randint(1, 1000) for _ in range(1, i+1)]
    st = '''
import random
'''
    stm = f'''
sorted({arr_100})'''
    srtd_time = timeit.timeit(setup= st, stmt=stm, number=1)
    sorts['sorted'].append(srtd_time)
    print(f'Sorted() sort took {srtd_time:.5f} seconds to sort {i} numbers')


# Час виконання сортування через вбудований метод SORT()
for i in data_len:
    arr_100 = [random.randint(1, 1000) for _ in range(1, i+1)]
    st = '''
import random
'''
    stm = f'''
{arr_100}.sort()'''
    srt_time = timeit.timeit(setup= st, stmt=stm, number=1)
    sorts['sort'].append(srt_time)
    print(f'Sort() sort took {srt_time:.5f} seconds to sort {i} numbers')



fig, ax = plt.subplots()
tms = ax.bar(sorts.keys(), [np.average(i)*1000 for i in sorts.values()], color='orange')
ax.bar_label(tms, fmt='%.2f')
ax.set_ylabel('Time (milliseconds)')
ax.spines[['top', 'right']].set_visible(False)
plt.grid(True, alpha=0.3)
plt.show()


"""Висновки:
              |  Merge     |  Insertion   |    Sorted() |   Sort()
10000 numbers |  0.02803 s |  2.50954 s   |   0.00175 s | 0.00123 s

Як бачимо, сортування через вбудовані методи sorted() та .sort() займають значно менше часу, ніж
сортування злиттям або вставками.
Сортування злиттям приблизно в 89 разів швидше за сортування вставками, однак в 16 разів
повільніше за вбудовані методи сортування.

Сортування sorted() та .sort() приблизно в 1400 разів швидші за сортування вставками.

Порівняння проводилось на основі сортування масивів рандомних чисел у діапазоні від 1 до 1000 
різної довжини (100, 1000, 10000, 100000 елементів у масиві).
Оскільки сортувавання вставками займає багато часу (4.3 хвилини) при сортуванні 100_000 елементів, 
у вище наведеному коді підрахунок часу для 10_000 елементів не представлений задля економії часу 
та пам'яті.

"""
