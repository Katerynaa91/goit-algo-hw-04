"""Завдання 2. Реалізуйте функцію, яка приймає на вхід список відсортованих списків 
та повертає відсортований список."""

def merge_lists(lst: list) -> list:
    """Базова функція для об'єднання 2-х відсортованих списків в один відсортований список"""
    l1=lst[0]
    l2=lst[1]
    i = 0 # index counter for l1
    j = 0 # index counter for l2
    merged = []

    while i < len(l1) and j < len(l2):
        if l1[i]<=l2[j]:
            merged.append(l1[i])
            i+=1
        else: 
            merged.append(l2[j])
            j+=1

    if i < len(l1):
        for k in range(i, len(l1)):
            merged.append(l1[k])
    elif j < len(l2):
        for n in range(j, len(l2)):
            merged.append(l2[n])
    return merged


def merge_k_lists(lst: list) -> list:
    """Функція, оптимізована для об'єднання необмеженої кількості відсортованих списків, 
    що є елементами списка вищого рівня"""
    l1=lst[0]
    l2=lst[1]
    index = 1
    m = merge_lists(l1, l2)
    while index <len(lst)-1:
        index+=1
        m= merge_lists(m, lst[index])    
    return m


lists = [[1, 11, 12], [1, 3, 4], [2, 6], [1, 3, 7], [2, 6, 8]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
