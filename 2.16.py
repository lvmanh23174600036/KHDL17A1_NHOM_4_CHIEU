def f(x,a,theta):
    e = 2.71828
    if x > 0:
        return a*e**(-x/theta)
    else:
        return 0
def tich_phan(f,m,n,p,a,theta):
    h = (n - m) / p
    integral = 0
    for i in range(p):
        x_left = m + i * h
        x_right = m + (i+1) * h
        integral += f((x_left + x_right) / 2,a,theta) * h
    return integral
#1.
theta = 1 #có thể thay đổi giá trị theta
a = 1  #tính toán giá trị của a sao cho tích phân = 1 
nguyen_ham = tich_phan(f,0,10,100,a,theta)
a = 1 / nguyen_ham
print(f"Giá trị của hệ số a: {a}")
#2.
x = int(input("Nhập giá trị x: "))
function = f(x,1/theta,theta)
print(f"Hàm phân phối xác suất X: F(x) = {function}")
#P(0 < X < θ) = F(θ)−F(0)
F_theta = f(theta,1/theta,theta)
F_0 = f(0,1/theta,theta)
P_0_X_theta = F_theta - F_0
print(f"P(0 < X < θ) = {P_0_X_theta}")

