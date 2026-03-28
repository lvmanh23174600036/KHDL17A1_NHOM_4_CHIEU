def tim_gia_tri_a(k):
    a = 1 / (1/3 + k)
    return a

def ky_vong_X(a, k):
    e_X = (1/3) * a + 2 * (1 - k) * a
    return e_X

def phuong_sai_X(a, k, e_X):
    var_X = (1/3) * a * (0 - e_X) ** 2 + 2 * (1 - k) * a * (2 - e_X) ** 2
    return var_X

def xac_xuat_giua(a, k):
    p = 2 * (1 - k) * a
    return p

def main():
    k = 0.1

    a = tim_gia_tri_a(k)
    print("a =", a)

    e_X = ky_vong_X(a, k)
    var_X = phuong_sai_X(a, k, e_X)
    std_dev_X = var_X ** 0.5
    print("E(X) =", e_X)
    print("Var(X) =", var_X)
    print("Std_dev(X) =", std_dev_X)

    p = xac_xuat_giua(a, k)
    print("P(0.5 < X < 2) =", p)

if __name__ == "__main__":
    main()