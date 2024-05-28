btrungv1 = 0.6
btrungv2 = 0.3
btruot = 0.1
diem_v1 = 10
diem_v2 = 5
trout = 0
ex = 0
vx = 0
exb = 0
print("x\t\t\t\t p")
print("--------------------------------------")
for x in range(0,21):
    if x == trout :
        p = btruot * btruot
    elif x == diem_v2:
        p = 2*(btruot * btrungv2)
    elif x == diem_v1:
        p = (btrungv1*btruot) + (btrungv2*btrungv2) + (btruot*btrungv1)
    elif x == diem_v1 + diem_v2:
        p = 2*(btrungv1*btrungv2)
    elif x == 2*diem_v1:
        p = (btrungv1*btrungv1)
    else: 
        p = 0
    ex += x*p
    exb += (x**2)*p
    vx = exb - ex**2
    if p != 0:
        print(f"{x}\t\t\t\t {p:.2f}")
print(f"giá trị kỳ vọng của biến X là E(X) = {ex:0f}")
print(f"giá trị phương sai của biến X là V(X) = {vx:2f}")
