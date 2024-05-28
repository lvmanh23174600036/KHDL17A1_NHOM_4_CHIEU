import math
#Ham f(x)
def f(x):
    if 1 <= x <= 4:
        return (x - 1) / 3
    else:
        return 0
#Tinh tich phan
def tich_phan(f, a, b, num = 1000):
    buoc = (b - a) / num
    tphan = 0.5 * (f(a) + f(b))
    for i in range (1, num):
        tphan += f(a + i * buoc)
    tphan *= buoc
    return tphan
#Tinh ky vong E(X)
def ky_vong(f, a, b, num = 1000):
    ham = lambda x: x * f(x)
    return tich_phan(ham, a, b, num)
#Tinh ky vong E(X**2)
def ki_vong(f, a, b, num = 1000):
    ham = lambda x: x**2 * f(x)
    return tich_phan(ham, a, b, num)
#Tinh phuong sai V(X)
def phuong_sai(f, a, b, num = 1000):
    E_X = ky_vong (f, a, b, num)
    E_X2 = ki_vong(f, a, b, num)
    return E_X2 - (E_X)**2
#Tinh Mot cua X
def mot(f, a, b):
    gia_tri = a
    max = f(a)
    for i in range(1,1001):
        x = a + i * (b - a) / 1000
        matdo = f(x)
        if matdo > max:
            max = matdo
            gia_tri = x
    return gia_tri
#In ra ket qua
a, b = 1, 4
E_X = ky_vong(f, a, b)
V_X = phuong_sai(f, a, b)
mot_x = mot(f, a, b)
print("Ky vong E(X):",E_X)
print("Phuong sai V(X):",V_X)
print("Mot cua X:",mot_x)