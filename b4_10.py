def phan_phoi_xac_suat():
    bang_du_lieu = {
        4: {90: 0.04, 110: 0.07, 130: 0.02, 150: 0, 180: 0},
        7: {90: 0.02, 110: 0.14, 130: 0.06, 150: 0.07, 180: 0},
        12: {90: 0, 110: 0.17, 130: 0.12, 150: 0.08, 180: 0.06},
        17: {90: 0, 110: 0, 130: 0.09, 150: 0.04, 180: 0.02}
    }
    return bang_du_lieu

def phan_phoi_xac_suat_carbonne_x_doi_voi_do_ben_130():
    bang_du_lieu = phan_phoi_xac_suat()
    return bang_du_lieu[130]

def phan_phoi_xac_suat_do_ben_y_doi_voi_carbonne_12():
    bang_du_lieu = phan_phoi_xac_suat()
    phan_phoi_y = {}
    for carbonne, do_ben in bang_du_lieu.items():
        if 12 in do_ben:
            phan_phoi_y[carbonne] = do_ben[12]
    return phan_phoi_y

def kiem_tra_doc_lap_X_va_Y():
    bang_du_lieu = phan_phoi_xac_suat()
    for carbonne, do_ben in bang_du_lieu.items():
        for do_ben_value in do_ben.values():
            if carbonne * do_ben_value != sum(do_ben.values()) * sum(bang_du_lieu[carbonne].values()):
                return False
    return True

def main():
    print("1) Phân phối xác suất của tỉ lệ carbonne X và của độ bền Y:")
    print(phan_phoi_xac_suat())
    
    print("\n2) Phân phối xác suất của tỉ lệ carbonne X đối với thép có độ bền 130 kg/cm²:")
    print(phan_phoi_xac_suat_carbonne_x_doi_voi_do_ben_130())
    
    print("\n3) Phân phối xác suất của độ bền Y đối với thép có tỉ lệ carbonne là 12%:")
    print(phan_phoi_xac_suat_do_ben_y_doi_voi_carbonne_12())
    
    print("\n4) Xét tính độc lập của X và Y:", "Có" if kiem_tra_doc_lap_X_va_Y() else "Không")

if __name__ == "__main__":
    main()
