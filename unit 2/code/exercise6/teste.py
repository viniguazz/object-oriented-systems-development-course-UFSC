class Teste():

    def __init__(self, a, b, c):
        if isinstance(a, int):
            self.__a = a
        if isinstance(b, str):
            self.__b = b
        if isinstance(c, bool):
            self.__c = c
        if self.__a == False or self.__b == False or self.__c == False:
            print('shit')

x = Teste(1, 'abc', True)
for _ in vars(x):
    print(f'x {_}')

y = Teste(1, 2, False)
for _ in vars(y):
    print(f'y {_}')

