def phan_phoi_xac_suat_dong_thoi():
    return [
        [4/15, 1/5, 4/15],
        [1/15, 2/15, 1/5],
        [0, 2/15, 0]
    ]

def gia_tri_x():
    return [-1, 15, 20]

def gia_tri_y():
    return [-1, 0, 1]

def phan_phoi_bien_x(bang_phan_phoi):
    phan_phoi_x = []
    for hang in bang_phan_phoi:
        phan_phoi_x.append(sum(hang))
    return phan_phoi_x

def phan_phoi_bien_y(bang_phan_phoi):
    phan_phoi_y = []
    so_cot = len(bang_phan_phoi[0])
    for j in range(so_cot):
        tong_cot = sum(bang_phan_phoi[i][j] for i in range(len(bang_phan_phoi)))
        phan_phoi_y.append(tong_cot)
    return phan_phoi_y

def ky_vong(gia_tri, phan_phoi_bien):
    return sum(gia_tri[i] * phan_phoi_bien[i] for i in range(len(gia_tri)))

def ky_vong_xy(gia_tri_x, gia_tri_y, bang_phan_phoi):
    E_XY = 0
    for i in range(len(gia_tri_x)):
        for j in range(len(gia_tri_y)):
            E_XY += gia_tri_x[i] * gia_tri_y[j] * bang_phan_phoi[i][j]
    return E_XY

def phuong_sai(gia_tri, phan_phoi_bien, ky_vong_value):
    return sum(((gia_tri[i] - ky_vong_value) ** 2) * phan_phoi_bien[i] for i in range(len(gia_tri)))

def hiep_phuong_sai(ky_vong_xy, ky_vong_x, ky_vong_y):
    return ky_vong_xy - ky_vong_x * ky_vong_y

def kiem_tra_doc_lap(bang_phan_phoi, phan_phoi_bien_x, phan_phoi_bien_y):
    doc_lap = True
    for i in range(len(phan_phoi_bien_x)):
        for j in range(len(phan_phoi_bien_y)):
            if not round(bang_phan_phoi[i][j], 10) == round(phan_phoi_bien_x[i] * phan_phoi_bien_y[j], 10):
                doc_lap = False
                break
    return doc_lap

def main():
    bang_phan_phoi = phan_phoi_xac_suat_dong_thoi()
    gia_tri_X = gia_tri_x()
    gia_tri_Y = gia_tri_y()

    phan_phoi_bien_X = phan_phoi_bien_x(bang_phan_phoi)
    phan_phoi_bien_Y = phan_phoi_bien_y(bang_phan_phoi)
    print("Phân phối xác suất biên của X:", phan_phoi_bien_X)
    print("Phân phối xác suất biên của Y:", phan_phoi_bien_Y)

    E_X = ky_vong(gia_tri_X, phan_phoi_bien_X)
    E_Y = ky_vong(gia_tri_Y, phan_phoi_bien_Y)
    E_XY = ky_vong_xy(gia_tri_X, gia_tri_Y, bang_phan_phoi)
    Cov_XY = hiep_phuong_sai(E_XY, E_X, E_Y)
    print("E(X):", E_X)
    print("E(Y):", E_Y)
    print("E(XY):", E_XY)
    print("Cov(X, Y):", Cov_XY)

    doc_lap = kiem_tra_doc_lap(bang_phan_phoi, phan_phoi_bien_X, phan_phoi_bien_Y)
    print("X và Y có độc lập không?", doc_lap)

if __name__ == "__main__":
    main()
