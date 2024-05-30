import sympy as sp

# Định nghĩa các biến
x, y, A = sp.symbols('x y A')

# Định nghĩa hàm mật độ xác suất chung
f_xy = A / sp.sqrt(x * y)

# Tích phân để tìm A
tich_phan = sp.integrate(sp.integrate(f_xy, (x, 0, y)), (y, 0, 1))
A_value = sp.solve(tich_phan - 1, A)[0]

print(f"Hằng số chuẩn hóa A: {A_value}")

# Tính hàm mật độ xác suất biên của X
f_X = sp.integrate(f_xy.subs(A, A_value), (y, x, 1))
print(f"Hàm mật độ xác suất biên của X: f_X(x) = {sp.simplify(f_X)}")

# Tính hàm mật độ xác suất biên của Y
f_Y = sp.integrate(f_xy.subs(A, A_value), (x, 0, y))
print(f"Hàm mật độ xác suất biên của Y: f_Y(y) = {sp.simplify(f_Y)}")

# Kiểm tra tính độc lập của X và Y
doc_lap = sp.simplify(f_xy.subs(A, A_value) - f_X * f_Y)
if doc_lap == 0:
    print("X và Y là các biến ngẫu nhiên độc lập.")
else:
    print("X và Y không độc lập.")