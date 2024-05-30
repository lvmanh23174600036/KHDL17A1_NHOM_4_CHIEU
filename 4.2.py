import pandas as pd
data = pd.DataFrame({1: [1, 2, 3],2: [2, 3, 1]}, index=[1, 2, 3])
pX = data.sum(axis=1)
pY = data.sum(axis=0)
doc_lap = True
for i in data.index:
    for j in data.columns:
        if (data.loc[i, j] !=  pX[i] * pY[j]) :
            doc_lap = False
            break
if doc_lap:
    print("X và Y độc lập.")
else:
    print("X và Y không độc lập.")