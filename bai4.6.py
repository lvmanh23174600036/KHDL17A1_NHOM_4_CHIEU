# Bảng phân phối xác suất đồng thời
bpp = {
    (6, 1): 0.1, (6, 2): 0.05, (6, 3): 0.15,
    (7, 1): 0.05, (7, 2): 0.15, (7, 3): 0.1,
    (8, 1): 0.1, (8, 2): 0.2, (8, 3): 0.1
}

# In bảng phân phối xác suất đồng thời
print("Bảng phân phối xác suất đồng thời của (X, Y):")
print("X\\Y\t1\t2\t3")
for x in range(6, 9):
    row = [f"{bpp[(x, y)]:.2f}" for y in range(1, 4)]
    print(f"{x}\t" + "\t".join(row))

# Xác suất biên của X
bxsbx = {6: 0, 7: 0, 8: 0}
for (x, y), p in bpp.items():
    bxsbx[x] += p

# Xác suất biên của Y
bxsby = {1: 0, 2: 0, 3: 0}
for (x, y), p in bpp.items():
    bxsby[y] += p

# Tính E(X)
E_X = sum(x * p for x, p in bxsbx.items())

# Tính E(Y)
E_Y = sum(y * p for y, p in bxsby.items())

# Tính Var(X)
E_X2 = sum(x**2 * p for x, p in bxsbx.items())
Var_X = E_X2 - E_X**2

# Tính Var(Y)
E_Y2 = sum(y**2 * p for y, p in bxsby.items())
Var_Y = E_Y2 - E_Y**2

# Phân phối xác suất của Y với điều kiện X = 7
ppxsxy_7 = {1: bpp[(7, 1)] / bxsbx[7],
                         2: bpp[(7, 2)] / bxsbx[7],
                         3: bpp[(7, 3)] / bxsbx[7]}

# Tính P(X = 6)
P_X_6 = bxsbx[6]

# Tính P(X >= 7, Y >= 2)
P_X_ge_7_Y_ge_2 = sum(p for (x, y), p in bpp.items() if x >= 7 and y >= 2)

# In kết quả
print("\nBảng phân phối xác suất biên của X:")
for x, p in bxsbx.items():
    print(f"P(X = {x}) = {p}")

print("\nBảng phân phối xác suất biên của Y:")
for y, p in bxsby.items():
    print(f"P(Y = {y}) = {p}")

print(f"\nE(X) = {E_X}")
print(f"E(Y) = {E_Y}")
print(f"Var(X) = {Var_X}")
print(f"Var(Y) = {Var_Y}")

print("\nBảng phân phối xác suất của Y với điều kiện X = 7:")
for y, p in ppxsxy_7.items():
    print(f"P(Y = {y} | X = 7) = {p}")

print(f"\nP(X = 6) = {P_X_6}")
print(f"P(X >= 7, Y >= 2) = {P_X_ge_7_Y_ge_2}")
