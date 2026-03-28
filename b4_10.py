def phan_phoi_xac_suat():
    bang_du_lieu = {
        4: {90: 0.04, 110: 0.07, 130: 0.02, 150: 0, 180: 0},
        7: {90: 0.02, 110: 0.14, 130: 0.06, 150: 0.07, 180: 0},
        12: {90: 0, 110: 0.17, 130: 0.12, 150: 0.08, 180: 0.06},
        17: {90: 0, 110: 0, 130: 0.09, 150: 0.04, 180: 0.02}
    }
    return bang_du_lieu

def phan_phoi_xac_suat_carbonne_x_doi_voi_do_ben_Y(bang_du_lieu, do_ben):
    phan_phoi_x = {}
    for carbonne, do_ben_dict in bang_du_lieu.items():
        if do_ben in do_ben_dict:
            phan_phoi_x[carbonne] = do_ben_dict[do_ben]
    return phan_phoi_x

def phan_phoi_xac_suat_do_ben_Y_doi_voi_carbonne_X(bang_du_lieu, carbonne):
    return bang_du_lieu.get(carbonne, {})

def kiem_tra_doc_lap_X_va_Y(bang_du_lieu):
    for carbonne, do_ben_dict in bang_du_lieu.items():
        for do_ben, phan_phoi in do_ben_dict.items():
            if carbonne * phan_phoi != sum(do_ben_dict.values()) * sum(bang_du_lieu[carbonne].values()):
                return False
    return True

def main():
    bang_du_lieu = phan_phoi_xac_suat()
    
    print("1) Phân phối xác suất của tỉ lệ carbonne X và của độ bền Y:")
    print(bang_du_lieu)
    
    do_ben = 130
    print("\n2) Phân phối xác suất của tỉ lệ carbonne X đối với thép có độ bền Y =", do_ben, "kg/cm²:")
    print(phan_phoi_xac_suat_carbonne_x_doi_voi_do_ben_Y(bang_du_lieu, do_ben))
    
    carbonne = 12
    print("\n3) Phân phối xác suất của độ bền Y đối với thép có tỉ lệ carbonne X =", carbonne, "%:")
    print(phan_phoi_xac_suat_do_ben_Y_doi_voi_carbonne_X(bang_du_lieu, carbonne))
    
    print("\n4) Xét tính độc lập của X và Y:", "Có" if kiem_tra_doc_lap_X_va_Y(bang_du_lieu) else "Không")

if __name__ == "__main__":
    main()
