def keliamieji(fn):
    def wrapper(metai):
        if type(metai) != int:
            raise ValueError('metai privalo buti skaicius')
        else:
            if metai % 4 == 0 and (metai % 100 != 0 or metai % 400 == 0):
                return fn(f'{metai} yra keliamieji')
            else:
                return fn(f'{metai} nera keliamieji')
    return wrapper

@keliamieji
def ar_keliamieji(metai):
    print(metai)

ar_keliamieji(2000)