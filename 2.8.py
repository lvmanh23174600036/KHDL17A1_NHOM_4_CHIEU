p = [0.05, 0.15, 0.4, 0.3]
x = [0, 1, 2, 3, 4]
gt  = 1 - sum(p)
p.append(gt)
loi_nhuan = 100

xs = sum(p[2:5])

ki_vong = 0
ex2 = 0
for i in range(len(x)):
    ki_vong +=  x[i] * p[i]
    ex2 += p[i] * (x[i]**2) 
phuong_sai =  ex2 - (ki_vong**2)

ki_vong_loi_nhuan = loi_nhuan * ki_vong
phuong_sai_loi_nhuan = loi_nhuan ** 2 * phuong_sai
print("kì vọng của lợi nhuận theo đơn vị triệu: ", ki_vong_loi_nhuan )
print("phương sai của lợi nhuận theo đơn vị triệu: ", phuong_sai_loi_nhuan)
print("kì vọng", ki_vong)
print("giá trị của p là: ", gt )
print("xác suất số hợp đồng là từ 2 trở lên: ", xs)
print("hàm khối lượng xác suất: ", p)
print("phương sai của số hợp đồng kí được: ", phuong_sai)