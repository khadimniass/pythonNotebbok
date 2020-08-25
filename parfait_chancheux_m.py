import math

def SomDiv(n:int()):
    return sum([i for i in range(n) if n%i==0])

def estParfait(entier:int()):
    teste=False
    if SomDiv(entier)==entier:
        teste=True
    return teste

def estPremier(nombre:int()):
    test=True
    for i in range(2,int(math.sqrt(nombre))):
             if nombre%i==0:
                test=False
    return test

def estChancheux(a:int()):
    teste=False
    for n in range(-1,a):
        if estPremier(a+n+n**2):
            teste=True
    return teste