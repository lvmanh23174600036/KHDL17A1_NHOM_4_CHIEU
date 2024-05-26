p1, p2 = 0.7, 0.8
A = [0] * 5 
B = [i for i in range(5)]
for i in range(3):
    for j in range(3):
        A[i+j] += (p1**i*(1-p1)**(2-i))*(p2**j*(1-p2)**(2-j))

print("Bảng phân phối xác suất")
print(B)
print(A)

c  = sum(A[i] for i in [0, 2, 4])

print("xác suất để số viên đạn trúng thú của hai người bằng nhau là: ", c)