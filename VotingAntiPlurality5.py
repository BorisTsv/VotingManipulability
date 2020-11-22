import random

InitArrangement = 4 * [0]

for i in range(0, 4):
    InitArrangement[i] = []
    for j in range(0, 120):
        InitArrangement[i].append(0)
# generating array of profiles
preferences = []
for i in range(1, 121):
    preferences.append(i)
counter = 0
for i in range(0, 5):
    for j in range(0, 5):
        for k in range(0, 5):
            for l in range(0, 5):
                for m in range(0, 5):
                    if i != j and i != k and i != l and i != m and j != k and j != l and j != m and k != l and k != m and l != m:
                        preferences[counter] = []
                        preferences[counter].append(i)
                        preferences[counter].append(j)
                        preferences[counter].append(k)
                        preferences[counter].append(l)
                        preferences[counter].append(m)
                        counter += 1
# generating array of points distribution according to profiles
PointDistArr = []
for i in range(0, 5):
    PointDistArr.append(i)
for i in range(0, 5):
    PointDistArr[i] = []
    for j in range(0, 120):
        PointDistArr[i].append(0)
for i in range(0, 120):
    for j in range(0, 5):
        s = preferences[i][j]
        PointDistArr[s][i] = 4 - j


trials = 800000 # number of points in the sample
TrialPts = trials * [0]
S = 120 * [0]

# creating random sample of points in the simplex
for i in range(0, trials):
    TrialPts[i] = []
    for j in range(0, 119):
        S[j] = random.uniform(0, 1)
    S[119]=1
    TrialPts[i] = sorted(S)
    for k in range(1, 120):
        TrialPts[i][120 - k] -= TrialPts[i][119 - k]
# initiating coalition members arrays (1 if the preference
# belongs to the coalition and 0 otherwise)
CoalB = 120 * [0]
CoalC = 120 * [0]
CoalD = 120 * [0]
CoalE = 120 * [0]
for j in range(0, 120):
    if PointDistArr[0][j] < PointDistArr[1][j]:
        CoalB[j] = 1
    if PointDistArr[0][j] < PointDistArr[2][j]:
        CoalC[j] = 1
    if PointDistArr[0][j] < PointDistArr[3][j]:
        CoalD[j] = 1
    if PointDistArr[0][j] < PointDistArr[4][j]:
        CoalE[j] = 1
dBA = 120 * [0]
dBC = 120 * [0]
dBD = 120 * [0]
dBE = 120 * [0]
dCA = 120 * [0]
dCB = 120 * [0]
dCD = 120 * [0]
dCE = 120 * [0]
dDA = 120 * [0]
dDB = 120 * [0]
dDC = 120 * [0]
dDE = 120 * [0]
dEA = 120 * [0]
dEB = 120 * [0]
dEC = 120 * [0]
dED = 120 * [0]
# computing d(B,A), d(B,C), d(B,D) and d(B,E)
for i in range(0, 120):
    for j in range(0, 5):
        s = preferences[i][j]
        if j == 4:
            PointDistArr[s][i] = 0
        else:
            PointDistArr[s][i] = 1
for j in range(0, 120):  # Initial arrangement is A>B>C>D
    InitArrangement[0][j] = PointDistArr[0][j] - PointDistArr[1][j]
    InitArrangement[1][j] = PointDistArr[1][j] - PointDistArr[2][j]
    InitArrangement[2][j] = PointDistArr[2][j] - PointDistArr[3][j]
    InitArrangement[3][j] = PointDistArr[3][j] - PointDistArr[4][j]
for j in range(0, 120):
    if CoalB[j] == 1:
        dBA[j] = 1
        dBC[j] = 1
        dBD[j] = 1
        dBE[j] = 1
    else:
        dBA[j] = PointDistArr[1][j] - PointDistArr[0][j]
        dBC[j] = PointDistArr[1][j] - PointDistArr[2][j]
        dBD[j] = PointDistArr[1][j] - PointDistArr[3][j]
        dBE[j] = PointDistArr[1][j] - PointDistArr[4][j]
# computing d(C,A), d(C,B), d(C,D) and d(C,E)
for j in range(0, 120):
    if CoalC[j] == 1:
        dCA[j] = 1
        dCB[j] = 1
        dCD[j] = 1
        dCE[j] = 1
    else:
        dCA[j] = PointDistArr[2][j] - PointDistArr[0][j]
        dCB[j] = PointDistArr[2][j] - PointDistArr[1][j]
        dCD[j] = PointDistArr[2][j] - PointDistArr[3][j]
        dCE[j] = PointDistArr[2][j] - PointDistArr[4][j]
# computing d(D,A), d(D,B), d(D,C) and d(D,E)
for j in range(0, 120):
    if CoalD[j] == 1:
        dDA[j] = 1
        dDB[j] = 1
        dDC[j] = 1
        dDE[j] = 1
    else:
        dDA[j] = PointDistArr[3][j] - PointDistArr[0][j]
        dDB[j] = PointDistArr[3][j] - PointDistArr[1][j]
        dDC[j] = PointDistArr[3][j] - PointDistArr[2][j]
        dDE[j] = PointDistArr[3][j] - PointDistArr[4][j]
# computing d(E,A), d(E,B), d(E,C) and d(E.D)
for j in range(0, 120):
    if CoalE[j] == 1:
        dEA[j] = 1
        dEB[j] = 1
        dEC[j] = 1
        dED[j] = 1
    else:
        dEA[j] = PointDistArr[4][j] - PointDistArr[0][j]
        dEB[j] = PointDistArr[4][j] - PointDistArr[1][j]
        dEC[j] = PointDistArr[4][j] - PointDistArr[2][j]
        dED[j] = PointDistArr[4][j] - PointDistArr[3][j]

counter = 0
B = 4*[0]
C = 4*[0]
D = 4*[0]
E = 4*[0]
Sb = []
Sc = []
Sd = []
Se = []
BmanipCheck = False
CmanipCheck = False
DmanipCheck = False
EmanipCheck = False
CoalBsize = 0
CoalCsize = 0
CoalDsize = 0
CoalEsize = 0
for i in range(0, trials):
    BmanipCheck = False
    CmanipCheck = False
    DmanipCheck = False
    EmanipCheck = False
    CoalBsize = 0
    CoalCsize = 0
    CoalDsize = 0
    CoalEsize = 0
    Sb = []
    Sc = []
    Sd = []
    Se = []
    check = False
    for j in range(0, 4):
        s = 0
        check = True
        for k in range(0, 120):
            s += TrialPts[i][k] * InitArrangement[j][k]
        if s < 0:
            check = False
            break
    if check is True:
        BmanipCheck = False
        CmanipCheck = False
        DmanipCheck = False
        EmanipCheck = False
        for j in range(0, 4):
            B[j] = 0
            C[j] = 0
            D[j] = 0
            E[j] = 0
        for k in range(0, 120):
            CoalBsize += TrialPts[i][k] * CoalB[k]
            CoalCsize += TrialPts[i][k] * CoalC[k]
            CoalDsize += TrialPts[i][k] * CoalD[k]
            CoalEsize += TrialPts[i][k] * CoalE[k]
            B[0] += TrialPts[i][k] * dBA[k]
            B[1] += TrialPts[i][k] * dBC[k]
            B[2] += TrialPts[i][k] * dBD[k]
            B[3] += TrialPts[i][k] * dBE[k]
            C[0] += TrialPts[i][k] * dCA[k]
            C[1] += TrialPts[i][k] * dCB[k]
            C[2] += TrialPts[i][k] * dCD[k]
            C[3] += TrialPts[i][k] * dCE[k]
            D[0] += TrialPts[i][k] * dDA[k]
            D[1] += TrialPts[i][k] * dDB[k]
            D[2] += TrialPts[i][k] * dDC[k]
            D[3] += TrialPts[i][k] * dDE[k]
            E[0] += TrialPts[i][k] * dEA[k]
            E[1] += TrialPts[i][k] * dEB[k]
            E[2] += TrialPts[i][k] * dEC[k]
            E[3] += TrialPts[i][k] * dED[k]
        Sb = sorted(B)
        Sc = sorted(C)
        Sd = sorted(D)
        Se = sorted(E)
        if (Sb[0]>0) and (Sb[0]+Sb[1]>CoalBsize) and (Sb[0]+Sb[1]+Sb[2]>2*CoalBsize) and (Sb[0]+Sb[1]+Sb[2]+Sb[3]>3*CoalBsize):
            BmanipCheck = True
        if (Sc[0]>0) and (Sc[0]+Sc[1]>CoalCsize) and (Sc[0]+Sc[1]+Sc[2]>2*CoalCsize) and (Sc[0]+Sc[1]+Sc[2]+Sc[3]>3*CoalCsize):
            CmanipCheck = True
        if (Sd[0]>0) and (Sd[0]+Sd[1]>CoalDsize) and (Sd[0]+Sd[1]+Sd[2]>2*CoalDsize) and (Sd[0]+Sd[1]+Sd[2]+Sd[3]>3*CoalDsize):
            DmanipCheck = True
        if (Se[0]>0) and (Se[0]+Se[1]>CoalEsize) and (Se[0]+Se[1]+Se[2]>2*CoalEsize) and (Se[0]+Se[1]+Se[2]+Se[3]>3*CoalEsize):
            EmanipCheck = True
    if check is True and ((BmanipCheck is True) or (CmanipCheck is True) or (DmanipCheck is True) or (EmanipCheck is True)):
        counter += 1
ans = 0.0
ans = float(120 * counter / 8000)
print(str(ans) + '%')