import math
#Ham f(x)
def f(x):
    if -6 < x < 6:
        return (36 - x**2) / 288
    else:
        return 0
#Tinh tich phan
def tich_phan(a, b, n):
    if n == 0:
        return f(a) * (b - a)
    else:
        h = (b - a) / n
        x = a + h
        sum_fx = 0
        for i in range(1,n):
            sum_fx += f(x)
            x += h
        return (h / 2) * (f(a) + 2 * sum_fx + f(b) + tich_phan(a ,b ,n//2))
som_it_nhat_2p = tich_phan(-6 ,-2, 1000)
muon_it_nhat_1p = tich_phan(1, 6, 1000)
som_trong_khoang_1_3p = tich_phan(1, 3, 1000)
muon_dung_5p = f(5)
print(f"Xác suất để một chuyến bay sớm ít nhất 2 phút là: {som_it_nhat_2p}")
print(f"Xác suất để một chuyến bay muộn ít nhất 1 phút là: {muon_it_nhat_1p}")
print(f"Xác suất để một chuyến bay sớm trong khoảng 1 đến 3 phút là: {som_trong_khoang_1_3p}")
print(f"Xác suất để một chuyến bay muộn đúng 5 phút là: {muon_dung_5p}")