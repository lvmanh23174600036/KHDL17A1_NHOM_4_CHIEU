
def ham_mat_do(x, y, z):
    return x + y + z
so_lan_chia = 1000
dx = dy = dz = 1 / so_lan_chia
tong_tich_phan = 0
for i in range(so_lan_chia):
    for j in range(so_lan_chia):
        for k in range(so_lan_chia):
            x = i * dx
            y = j * dy
            z = k * dz
            tong_tich_phan += ham_mat_do(x, y, z) * dx * dy * dz
c = 1 / tong_tich_phan
print("Giá trị của tham số c là:", c)
#xác định giá trị hàm phâm phối xác suất F(x,y,z)
def ham_mat_do(x, y, z):
    return x + y + z
def phan_phoi_xac_suat(x, y, z, ham_mat_do):
    tong_phan_phoi = 0
    delta = 0.001 
    for u in range(int(x / delta)):
        for v in range(int(y / delta)):
            for w in range(int(z / delta)):
                tong_phan_phoi += ham_mat_do(u * delta, v * delta, w * delta) * delta * delta * delta

    return tong_phan_phoi
x = 0.5
y = 0.7
z = 0.8
F_xyz = phan_phoi_xac_suat(x, y, z, ham_mat_do)

print("Giá trị của hàm phân phối xác suất F(x, y, z) tại điểm ({}, {}, {}) là: {:.6f}".format(x, y, z, F_xyz))
