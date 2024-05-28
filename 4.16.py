import random
def mo_phong_cuoc_gap(so_lan_mo_phong):
    xac_suat_gap_nhau = 0
    for i in range(so_lan_mo_phong):
        nguoi_thu_nhat = random.uniform(0,60)
        nguoi_thu_2 = random.uniform(0,60)
        if abs(nguoi_thu_nhat - nguoi_thu_2) <= 15:
            xac_suat_gap_nhau = 1
    p = xac_suat_gap_nhau / so_lan_mo_phong
    return p
so_lan_mo_phong = 6
xac_suat_cung_nhau_di_choi = mo_phong_cuoc_gap(so_lan_mo_phong)
print(f"Xác suất để hai người cùng nhau đi chơi là: {xac_suat_cung_nhau_di_choi:.4f}")