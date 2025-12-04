from inspect import signature

## исходная функция
def f(x, y, z):
    return x + y + z

## каррирование
def curry(f, arity):

    ## функция, которая вызывает саму себя и накапливает аргументы
    def g(*args):

        ##возвращает длину списка переменных из сигнатуры функции и сравнивает с арностью
        if arity != len(signature(f).parameters):
            raise Exception("Некорректная арность")

        ## если количество аргументов и арность совпадают, то каррирование завершенно
        if len(args) == arity:
            return f(*args)
        ## иначе запоминаем аргумент, и вызваем функцию еще раз
        return lambda *x: g(*(args + x))

    return g()

## антикаррировоние
def uncurry(g):

    ## применяет к каждому элементу кортежа каррированую функцию
    def f(*args):
        curry_f = g
        for element in args:
            curry_f = curry_f(element)
        return curry_f

    return f()

curry_f = curry(f, 3)
uncurry_f = uncurry(curry_f)
print("Исходная функция:", f(1, 2, 3))
print("Каррированная функция:", curry_f(1)(2)(3))
print("Антикаррированная функция:", uncurry_f(1, 2, 3))

