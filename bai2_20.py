import math
#Ham f(x)
def f_x(x):
    if 0 <= x <= 1:
        return 3 * (x**2)
    else:
        return 0
#Tinh tich phan
def tich_phan(f, a, b, n=10000):
    buoc = (b - a) / n
    tphan = 0.5 * (f(a) + f(b))
    for i in range(n):
        tphan += f(a + i * buoc)
    tphan *= buoc
    return tphan
#Tinh trung vi
def trung_vi(a, b, t = 1e-5):
    trung_binh = (a + b) / 2
    if abs(tich_phan(f_x, 0, trung_binh) - 0.5) < t:
        return trung_binh
    elif tich_phan(f_x, 0, trung_binh) < 0.5:
        return trung_vi(trung_binh, b, t)
    else:
        return trung_vi(a,trung_binh, t)

def tinh_toan():
    # Kỳ vọng E[X]
    E_X = tich_phan(lambda x: x * f_x(x), 0, 1)

    # Phương sai V(X)
    E_X2 = tich_phan(lambda x: x**2 * f_x(x), 0, 1)
    V_X = E_X2 - E_X**2

    # Trung vị 
    trung_vi_X = trung_vi(0, 1)

    # Hệ số bất đối xứng 
    E_X3 = tich_phan(lambda x: x**3 * f_x(x), 0, 1)
    hso_bat_dx_X = (E_X3 - 3 * E_X * V_X - E_X**3) / V_X**(3/2)

    # Hệ số nhọn 
    E_X4 = tich_phan(lambda x: x**4 * f_x(x), 0, 1)
    hso_nhon_X = (E_X4 - 4 * E_X * E_X3 + 6 * E_X**2 * E_X2 - 3 * E_X**4) / V_X**2

    return E_X, V_X, trung_vi_X, hso_bat_dx_X, hso_nhon_X

# Gọi hàm và lấy kết quả
results = tinh_toan()
print("Kỳ vọng (E[X]):", results[0])
print("Phương sai (V(X)): ", results[1])
print("Trung vị: ", results[2])
print("Hệ số bất đối xứng: ", results[3])
print("Hệ số nhọn: ", results[4])
