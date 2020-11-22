import random

InitArrangement = 3 * [0]

for i in range(0, 3):
    InitArrangement[i] = []
    for j in range(0, 24):
        InitArrangement[i].append(0)
# generating array of profiles
preferences = []
for i in range(1, 25):
    preferences.append(i)
counter = 0
for i in range(0, 4):
    for j in range(0, 4):
        for k in range(0, 4):
            for l in range(0, 4):
                if i != j and i != k and i != l and j != k and j != l and k != l:
                    preferences[counter] = []
                    preferences[counter].append(i)
                    preferences[counter].append(j)
                    preferences[counter].append(k)
                    preferences[counter].append(l)
                    counter += 1
# generating array of points distribution according to profiles
PointDistArr = []
for i in range(0, 4):
    PointDistArr.append(i)
for i in range(0, 4):
    PointDistArr[i] = []
    for j in range(0, 24):
        PointDistArr[i].append(0)
for i in range(0, 24):
    for j in range(0, 4):
        s = preferences[i][j]
        PointDistArr[s][i] = 3 - j


trials = 3000000 # number of points in the sample
TrialPts = trials * [0]
S = 24 * [0]

# creating random sample of points in the simplex
for i in range(0, trials):
    TrialPts[i] = []
    for j in range(0, 23):
        S[j] = random.uniform(0, 1)
    S[23]=1
    TrialPts[i] = sorted(S)
    for k in range(1, 24):
        TrialPts[i][24 - k] -= TrialPts[i][23 - k]
# initiating coalition members arrays (1 if the preference
# belongs to the coalition and 0 otherwise)
CoalB = 24 * [0]
CoalC = 24 * [0]
CoalD = 24 * [0]
for j in range(0, 24):
    if PointDistArr[0][j] < PointDistArr[1][j]:
        CoalB[j] = 1
    if PointDistArr[0][j] < PointDistArr[2][j]:
        CoalC[j] = 1
    if PointDistArr[0][j] < PointDistArr[3][j]:
        CoalD[j] = 1
dBA = 24 * [0]
dBC = 24 * [0]
dBD = 24 * [0]
dCA = 24 * [0]
dCB = 24 * [0]
dCD = 24 * [0]
dDA = 24 * [0]
dDB = 24 * [0]
dDC = 24 * [0]
# computing d(B,A), d(B,C) and d(B,D)
for i in range(0, 24):
    for j in range(0, 4):
        s = preferences[i][j]
        if j == 3:
            PointDistArr[s][i] = 0
        else:
            PointDistArr[s][i] = 1
for j in range(0, 24):  # Initial arrangement is A>B>C>D
    InitArrangement[0][j] = PointDistArr[0][j] - PointDistArr[1][j]
    InitArrangement[1][j] = PointDistArr[1][j] - PointDistArr[2][j]
    InitArrangement[2][j] = PointDistArr[2][j] - PointDistArr[3][j]
for j in range(0, 24):
    if CoalB[j] == 1:
        dBA[j] = 1
        dBC[j] = 1
        dBD[j] = 1
    else:
        dBA[j] = PointDistArr[1][j] - PointDistArr[0][j]
        dBC[j] = PointDistArr[1][j] - PointDistArr[2][j]
        dBD[j] = PointDistArr[1][j] - PointDistArr[3][j]
# computing d(C,A), d(C,B) and d(C,D)
for j in range(0, 24):
    if CoalC[j] == 1:
        dCA[j] = 1
        dCB[j] = 1
        dCD[j] = 1
    else:
        dCA[j] = PointDistArr[2][j] - PointDistArr[0][j]
        dCB[j] = PointDistArr[2][j] - PointDistArr[1][j]
        dCD[j] = PointDistArr[2][j] - PointDistArr[3][j]
# computing d(D,A), d(D,B) and d(D,C)
for j in range(0, 24):
    if CoalD[j] == 1:
        dDA[j] = 1
        dDB[j] = 1
        dDC[j] = 1
    else:
        dDA[j] = PointDistArr[3][j] - PointDistArr[0][j]
        dDB[j] = PointDistArr[3][j] - PointDistArr[1][j]
        dDC[j] = PointDistArr[3][j] - PointDistArr[2][j]
counter = 0
B = 3*[0]
C = 3*[0]
D = 3*[0]
Sb = []
Sc = []
Sd = []
BmanipCheck = False
CmanipCheck = False
DmanipCheck = False
CoalBsize = 0
CoalCsize = 0
CoalDsize = 0
for i in range(0, trials):
    BmanipCheck = False
    CmanipCheck = False
    DmanipCheck = False
    CoalBsize = 0
    CoalCsize = 0
    CoalDsize = 0
    Sb = []
    Sc = []
    Sd = []
    check = False
    for j in range(0, 3):
        s = 0
        check = True
        for k in range(0, 24):
            s += TrialPts[i][k] * InitArrangement[j][k]
        if s < 0:
            check = False
            break
    if check is True:
        BmanipCheck = False
        CmanipCheck = False
        DmanipCheck = False
        for j in range(0, 3):
            B[j] = 0
            C[j] = 0
            D[j] = 0
        for k in range(0, 24):
            CoalBsize += TrialPts[i][k] * CoalB[k]
            CoalCsize += TrialPts[i][k] * CoalC[k]
            CoalDsize += TrialPts[i][k] * CoalD[k]
            B[0] += TrialPts[i][k] * dBA[k]
            B[1] += TrialPts[i][k] * dBC[k]
            B[2] += TrialPts[i][k] * dBD[k]
            C[0] += TrialPts[i][k] * dCA[k]
            C[1] += TrialPts[i][k] * dCB[k]
            C[2] += TrialPts[i][k] * dCD[k]
            D[0] += TrialPts[i][k] * dDA[k]
            D[1] += TrialPts[i][k] * dDB[k]
            D[2] += TrialPts[i][k] * dDC[k]
        Sb = sorted(B)
        Sc = sorted(C)
        Sd = sorted(D)
        if (Sb[0] > 0) and (Sb[0]+Sb[1] > CoalBsize) and (Sb[0]+Sb[1]+Sb[2] > 2*CoalBsize):
            BmanipCheck = True
        if (Sc[0] > 0) and (Sc[0]+Sc[1] > CoalCsize) and (Sc[0]+Sc[1]+Sc[2] > 2*CoalCsize):
            CmanipCheck = True
        if (Sd[0] > 0) and (Sd[0]+Sd[1] > CoalDsize) and (Sd[0]+Sd[1]+Sd[2] > 2*CoalDsize):
            DmanipCheck = True

    if check is True and ((BmanipCheck is True) or (CmanipCheck is True) or (DmanipCheck is True)):

        counter += 1
ans = 0.0
ans = float(24 * counter / 30000)
print(str(ans) + '%')