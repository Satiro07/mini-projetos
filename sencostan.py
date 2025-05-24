from math import cos
def seno(angulo):
    seno = angulo * (3.14159/180)
    return seno

print(seno(30))


def cosseno(angulo):
    x = angulo * (3.14159/180)
    cosseno = 1 - ((x**2/2) + (x**4/24))
    return cosseno

print(cosseno(30))

print(cos(0.523598))