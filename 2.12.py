import math
n = 20
p = 0.4
#1.
trung_binh = n * p 
do_lech_chuan = math.sqrt(n * p * (1 - p)) 
mot = math.floor((n + 1) * p)
#2.
k = 10
pX_10 = (math.comb(n,k)) * (p**k) * ((1-p)**(n-k))  
print(f"Giá trị trung bình: {trung_binh}")
print(f"Độ lệch chuẩn: {do_lech_chuan:.2f}")
print(f"Mốt: {mot}")
print(f"Xác suất P(X=10): {pX_10:.4f}")