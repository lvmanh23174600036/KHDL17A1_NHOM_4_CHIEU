#A tính c và E(x)
c = 1 - (1/3)
c = c / 1
c = round(c, 2) 
print(f"c = {c}")
E_X = (2/3) * ((1/3) / (1 - (1/3))) 
E_X = round(E_X, 2) 
print(f"E(X) = {E_X}")
#B tính P(X>=3)
c = 2/3
p_3 = 0 
for x in range(3, 21):
    p_x = c * (1/3)**x
    p_3 += p_x
print(f"P(X >= 3) = {p_3:.4f}")
#C tính P(X=2k+1)
c = 2/3
p_odd = 0 
for x in range(1, 21, 2):
    p_x = c * (1/3)**x
    p_odd += p_x
print(f"P(X = 2k + 1) = {p_odd:.4f}")