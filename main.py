import math

# Вспомогательные функции для создания полного бинарного дерева

def edit_bin_level(bin_level):
    list_of_void = []
    sort_bin_level = []
    for i in bin_level:
        if type(i) == type([]):
            list_of_void.append(i)
        else:
            sort_bin_level.append(i)
    for i in list_of_void:
        sort_bin_level.insert(i[1], i[0])
    return sort_bin_level

def check_bin_level(bin_level):
    for i in bin_level:
        if type(i) == type([]):
            return 1
    return 0

# Создаем отсутствующие пустые ветки

def full_bin_tree(digits):
    len_digits = len(digits)
    count_level = int(math.log(len_digits, 2)) + 1
    now_level = 0
    bin_tree = []
    bin_level = []
    for i in range(0, len_digits):
        if len(bin_level) == 2 ** now_level:
            if check_bin_level(bin_level):
                bin_level = edit_bin_level(bin_level)
            bin_tree.append(bin_level)
            if '' in bin_level:
                void_ind = []
                for i in range(len(bin_level)):
                    if bin_level[i] == '':
                        void_ind.append(i)
                bin_level = []
                for i in void_ind:
                    bin_level.append(['', 2 * i])
                    bin_level.append(['', 2 * i + 1])
            else:
                bin_level = []
            now_level += 1
        bin_level.append(digits[i])
    if check_bin_level(bin_level):
        bin_level = edit_bin_level(bin_level)
    bin_tree.append(bin_level)
    return bin_tree

# Создаем бинарное дерево префиксных сумм

def pref_sum(digits):
    pref_sum_tree = full_bin_tree(digits)

    for i in range(1, len(pref_sum_tree)):
        for j in range(len(pref_sum_tree[i])):
            if pref_sum_tree[i][j] != '':
                pref_sum_tree[i][j] += pref_sum_tree[i - 1][j // 2]

    return pref_sum_tree

# Находим все пути до введеного числа и выводим, если такие существуют

def find_paths(digits):
    pref_sum_tree = pref_sum(digits)
    last_level = len(pref_sum_tree) - 1
    find_ind = []
    for i in range(len(pref_sum_tree[last_level])):
        if pref_sum_tree[last_level][i] == n:
            find_ind.append(i)
    if find_ind != []:
        paths = []
        path = []
        for i in find_ind:
            for j in range(last_level, -1, -1):
                if j == last_level:
                    path.append([j, i])
                    ind_path = 0
                else:
                    path.append([j, path[ind_path][1] // 2])
                    ind_path += 1
            paths.append(path)
            path = []

        for i in paths:
            i.reverse()
        bin_tree = full_bin_tree(digits)
        for i in paths:
            for j in i:
                if j[0] == last_level:
                    print(bin_tree[j[0]][j[1]])
                else:
                    print(bin_tree[j[0]][j[1]], '-> ', end='')
    else:
        print('\nТакого пути не существует')

s = input('Введите значения через запятую: ')
digits = []
for i in s.split(','):
    if i != '':
        digits.append(int(i))
    else:
        digits.append('')
n = int(input('Введите число которое ищем: '))

find_paths(digits)
