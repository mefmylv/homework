def selection_sort(arg):
    n = len(arg)
    for i in range(n):
        min_num = i
        for a in range(i+1,n):
            if arg[a] < arg[min_num]:
                min_num = a
        arg[i], arg[min_num] = arg[min_num], arg[i]

    return arg

unsorted_list = [2,0,89,23,1,98,25,45,67,12]
sorted_list = selection_sort(unsorted_list)
print(sorted_list)

def binary_search():
    num = int(input('Введите число из списка выше 🠕🠕🠕'))

    mid_list = len(sorted_list) // 2
    low_list = 0
    high_list = len(sorted_list) - 1
    while sorted_list[mid_list] != num and low_list <= high_list:
        if num > sorted_list[mid_list]:
            low_list = mid_list + 1
        else:
            high_list = mid_list - 1
        mid_list = (low_list + high_list) // 2
        if low_list > high_list:
            print('ВЫ ВВЕЛИ ЧИСЛО НЕ ИЗ СПИСКА')
        elif low_list > high_list:
            print(f' INDEX = {mid_list}')


binary_search()






