n_A, n_B, n_C = 8, 5, 3
n_total = n_A + n_B + n_C
n_pick = 3

def giai_thua(n):
    if n == 0:
        return 1
    else:
        return n * giai_thua(n-1)

def to_hop(n, r):
    return giai_thua(n) / (giai_thua(r) * giai_thua(n - r))
bang = [[0 for _ in range(n_pick+1)] for _ in range(n_pick+1)]

for X in range(n_pick+1):
    for Y in range(n_pick+1):
        if X + Y <= n_pick:
            Z = n_pick - X - Y
            bang[X][Y] = (to_hop(n_A, X) * to_hop(n_B, Y) * to_hop(n_C, Z)) / to_hop(n_total, n_pick)

print("Bảng phân phối xác suất đồng thời (X, Y):")
for row in bang:
    print(row)