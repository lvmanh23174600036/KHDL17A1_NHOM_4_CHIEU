import numpy as np
from scipy.integrate import quad

# Hàm mật độ xác suất
def f(x):
    if x <= 0 or x > 2:
        return 0
    elif 0 < x < 1:
        return a * x**2
    else:
        return a * (2 - x)**2

# Ràng buộc tổng xác suất bằng 1
def constraint(a):
    integral, _ = quad(f, -np.inf, np.inf)
    return 1 - integral

# Tìm giá trị của a
a = 1 / (quad(lambda x: x**2, 0, 1)[0] + quad(lambda x: (2 - x)**2, 1, 2)[0])

# Kỳ vọng
mean, _ = quad(lambda x: x * f(x), -np.inf, np.inf)

# Phương sai
variance, _ = quad(lambda x: (x - mean)**2 * f(x), -np.inf, np.inf)

# Độ lệch chuẩn
std_deviation = np.sqrt(variance)

# Xác suất P(0.5 < X < 2)
probability, _ = quad(f, 0.5, 2)

print("Giá trị của a:", a)
print("Kỳ vọng của X:", mean)
print("Phương sai của X:", variance)
print("Độ lệch chuẩn của X:", std_deviation)
print("Xác suất P(0.5 < X < 2):", probability)

