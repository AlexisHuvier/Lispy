def fib(nb):
    if nb == 0:
        return 0
    if nb == 1:
        return 1
    if nb == 2:
        return 1
    nb1 = 1
    nb2 = 1
    suivant = 0
    for i in range(2, nb):
        suivant = nb1 + nb2
        nb1 = nb2
        nb2 = suivant
    return suivant
