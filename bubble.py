from random import randint


def bub_sort(listing):
    for index_1 in range(len(listing) - 1):
        for index_2 in range(index_1 + 1, len(listing)):
            ## сравнение и перестановка
            if listing[index_1] > listing[index_2]:
                listing[index_1], listing[index_2] = listing[index_2], listing[index_1]
    return listing


## массив с рандомными цифрами
check_list = [randint(1, 1000) for i in range(15)]
print(*check_list)
bub_sort(check_list)
print(*check_list)
