import random 

def sena():
    from random import shuffle
    x = [[i] for i in range(1,60)]
    shuffle(x)
    print (x[0:6])


print(sena())