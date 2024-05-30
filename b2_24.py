# Tìm giá trị của a
def tim_gia_tri_a(k):
    # Đảm bảo tổng của PDF trên toàn bộ miền giá trị của X bằng 1
    a = 1 / (1/3 + k)
    return a

# Tính kỳ vọng của X
def ky_vong_X(a, k):
    # Tính phần diện tích dưới đường cong PDF và giá trị tương ứng với mỗi điểm
    e_X = (1/3) * a + 2 * (1 - k) * a
    return e_X

# Tính phương sai của X
def phuong_sai_X(a, k, e_X):
    # Tính phần diện tích dưới đường cong PDF và giá trị (X - E(X))^2 tương ứng với mỗi điểm
    var_X = (1/3) * a * (0 - e_X) ** 2 + 2 * (1 - k) * a * (2 - e_X) ** 2
    return var_X

# Tính P(0.5 < X < 2)
def xac_xuat_giua(a, k):
    # Tính diện tích dưới đường cong PDF trong khoảng từ 0.5 đến 2
    p = 2 * (1 - k) * a
    return p

def main():
    # Giả định giá trị của k
    k = 0.1

    # Bước 1: Tìm giá trị của a
    a = tim_gia_tri_a(k)
    print("a =", a)

    # Bước 2: Tính kỳ vọng, phương sai và độ lệch chuẩn của X
    e_X = ky_vong_X(a, k)
    var_X = phuong_sai_X(a, k, e_X)
    std_dev_X = var_X ** 0.5
    print("E(X) =", e_X)
    print("Var(X) =", var_X)
    print("Std_dev(X) =", std_dev_X)

    # Bước 3: Tính P(0.5 < X < 2)
    p = xac_xuat_giua(a, k)
    print("P(0.5 < X < 2) =", p)

if __name__ == "__main__":
    main()
