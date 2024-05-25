
#1) XÁC ĐỊNH HÀM MẬT ĐỘ BIÊN
def f(x, y):
    if 0 <= x <= 1 and 0 <= y <= 1:
        return 6/5 * (x + y**2)
    else:
        return 0

def mat_do_xac_suat_X(x):
    buoc = 0.001
    tong_tich_phan = 0
    y = 0
    while y < 1:
        tong_tich_phan += f(x, y) * buoc
        y += buoc
    return tong_tich_phan

def mat_do_xac_suat_Y(y):

    buoc = 0.001
    tong_tich_phan = 0
    x = 0
    while x < 1:
        tong_tich_phan += f(x, y) * buoc
        x += buoc
    return tong_tich_phan

print("Hàm mật độ xác suất biên của X:")
print("f_X(x) =", mat_do_xac_suat_X(0.5))  
print()
print("Hàm mật độ xác suất biên của Y:")
print("f_Y(y) =", mat_do_xac_suat_Y(0.5))
#2) XÁC ĐỊNH CÁC HÀM MẬT ĐỘ CÓ ĐIỀU KIỆN

def f(x, y):
    if 0 <= x <= 1 and 0 <= y <= 1:
        return 6/5 * (x + y**2)
    else:
        return 0


def mat_do_xac_suat_X(x):
    buoc = 0.001
    integral_sum = 0
    y = 0
    while y < 1:
        integral_sum += f(x, y) * buoc
        y += buoc
    return integral_sum


def mat_do_xac_suat_Y(y):
    buoc = 0.001
    integral_sum = 0
    x = 0
    while x < 1:
        integral_sum += f(x, y) * buoc
        x += buoc
    return integral_sum

def mat_do_xac_suat_X_khi_biet_Y(x, y):
    return f(x, y) / mat_do_xac_suat_Y(y)

def mat_do_xac_suat_Y_khi_biet_X(y, x):
    return f(x, y) / mat_do_xac_suat_X(x)

print("Hàm mật độ xác suất có điều kiện của X khi biết Y:")
print("f_X|Y(x|y) =", mat_do_xac_suat_X_khi_biet_Y(0.5, 0.6))  
print()

print("Hàm mật độ xác suất có điều kiện của Y khi biết X:")
print("f_Y|X(y|x) =", mat_do_xac_suat_Y_khi_biet_X(0.6, 0.5))  
#3)TÍNH KÌ VỌNG VÀ PHƯƠNG SAI CỦA X VÀ Y

# Hàm mật độ xác suất đa biến f(x, y)
def mat_do_xac_suat(x, y):
    if 0 <= x <= 1 and 0 <= y <= 1:
        return 6/5 * (x + y**2)
    else:
        return 0

# Hàm mật độ xác suất biên của X
def mat_do_xac_suat_X(x):
    tong_tich_phan = 0
    buoc = 0.001
    y = 0
    while y < 1:
        tong_tich_phan += mat_do_xac_suat(x, y) * buoc
        y += buoc
    return tong_tich_phan

# Hàm mật độ xác suất biên của Y
def mat_do_xac_suat_Y(y):
    tong_tich_phan = 0
    buoc = 0.001
    x = 0
    while x < 1:
        tong_tich_phan += mat_do_xac_suat(x, y) * buoc
        x += buoc
    return tong_tich_phan

# Kỳ vọng của X
def ky_vong_X():
    tong_tich_phan = 0
    buoc = 0.001
    x = 0
    while x < 1:
        tong_tich_phan += x * mat_do_xac_suat_X(x) * buoc
        x += buoc
    return tong_tich_phan

# Kỳ vọng của Y
def ky_vong_Y():
    tong_tich_phan = 0
    buoc = 0.001
    y = 0
    while y < 1:
        tong_tich_phan += y * mat_do_xac_suat_Y(y) * buoc
        y += buoc
    return tong_tich_phan

# Kỳ vọng của X^2
def ky_vong_X_binh_phuong():
    tong_tich_phan = 0
    buoc = 0.001
    x = 0
    while x < 1:
        tong_tich_phan += (x**2) * mat_do_xac_suat_X(x) * buoc
        x += buoc
    return tong_tich_phan

# Kỳ vọng của Y^2
def ky_vong_Y_binh_phuong():
    tong_tich_phan = 0
    buoc = 0.001
    y = 0
    while y < 1:
        tong_tich_phan += (y**2) * mat_do_xac_suat_Y(y) * buoc
        y += buoc
    return tong_tich_phan

# Phương sai của X
def phuong_sai_X():
    return ky_vong_X_binh_phuong() - (ky_vong_X())**2

# Phương sai của Y
def phuong_sai_Y():
    return ky_vong_Y_binh_phuong() - (ky_vong_Y())**2

print("Kỳ vọng của X (E(X)):", ky_vong_X())
print("Kỳ vọng của Y (E(Y)):", ky_vong_Y())
print("Phương sai của X (V(X)):", phuong_sai_X())
print("Phương sai của Y (V(Y)):", phuong_sai_Y())

#4) tính hiệp phương sai và hệ số tương quan 
# Hiệp phương sai giữa X và Y
def hiep_phuong_sai():
    tong_tich_phan = 0
    buoc = 0.001
    x = 0
    while x < 1:
        y = 0
        while y < 1:
            tong_tich_phan += (x - ky_vong_X()) * (y - ky_vong_Y()) * mat_do_xac_suat(x, y) * buoc**2
            y += buoc
        x += buoc
    return tong_tich_phan

# Hệ số tương quan giữa X và Y
def he_so_tuong_quan():
    return hiep_phuong_sai() / (phuong_sai_X() * phuong_sai_Y())**0.5

print("Hiệp phương sai giữa X và Y (Cov(X,Y)):", hiep_phuong_sai())
print("Hệ số tương quan giữa X và Y (ρ(X,Y)):", he_so_tuong_quan())
