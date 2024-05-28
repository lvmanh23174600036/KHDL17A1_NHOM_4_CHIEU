def f(x):
    if 10 < x < 20:
        return 1/20
    else:
        return 0
def tich_phan(f,a,b,n):
    '''
    Tính tích phân của hàm f từ a đến b bằng phương pháp hình chữ nhật
    f -- hàm cần tính tích phân
    a -- giới hạn dưới của tích phân
    b -- giới hạn trên của tích phân
    n -- số lượng hình chữ nhật
    '''
    h = (b - a) / n  #kích thước mỗi HCN
    integral = 0     #chiều cao HCN
    for i in range(n):
        x_left = a + i * h    #giá trị biên HCN
        x_right = a + (i+1) * h
        integral += f((x_left + x_right) / 2) * h
    return integral
nguyen_ham = tich_phan(f,10,20,100)
if nguyen_ham == 1:
    print("f(x) là hàm mật độ xác suất.")
else:
    print("f(x) không phải là hàm mật độ xác suất.")
print("Kết quả tích phân:", nguyen_ham)