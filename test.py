i = 3
if i == 1:
    l = [-3, -2, -1, 0, 1, 2, 3]
    formulas = [lambda x: (x - 2) ** 2, lambda x: 0.5 * x ** 2 + 5, lambda x: 2 * x ** 2 + 5 * x]

    for f in formulas:
        for x in l:
            print(' f(' + str(x) + ') =', f(x))
        if not f == formulas[-1]:
            print('#################')

elif i == 2:
    def generator(lst, ln, is_prim=True):
        for i in lst:
            if is_prim:
                for j in generator(lst, ln - 1, False):
                    print(i + j)
            else:
                ol = []
                if ln == 1:
                    return lst
                else:
                    for j in generator(lst, ln - 1, False):
                        ol.append(i + j)
                    return ol


    l = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    generator(l, 5)

elif i == 3:
    l = [3, 4, 5, 5]
    print(type(l) == list)
