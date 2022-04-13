# TUGAS 1 Algoritma Hill Cipher
#   Naufal Firmansyah
#   A11.2019.12054
#   Kriptografi


def matriks(K1, K2, K3, K4):
    matriks = [[K1, K2], [K3, K4]]
    return matriks

def plaintext_proses():
    pisahP = []
    for i in range(0,len(P),2):
        try:
            pisahP.append(P[i]+P[i+1])
        except IndexError:
            pisahP.append(P[i]+P[i])
            break
    return pisahP

hrf = "abcdefghijklmnopqrstuvwxyz"
huruf = [i for i in hrf]

#kunci default
K = matriks(5,6,2,3)
C = ""
P = input("Masukkan PlainText>> ").replace(" ","")
pisahP = plaintext_proses()
print(P)

for i in pisahP:
    getIdx = []
    K_temp = []
    getIdx = [huruf.index(x)+1 for x in i]
    K_temp = [((K[0][0] * getIdx[0]) + (K[0][1] * getIdx[1])) % 26, ((K[1][0] * getIdx[0]) + (K[1][1] * getIdx[1])) % 26]
    for x in range(len(K_temp)):
        C += huruf[K_temp[x]+1]
print(C)
    
print(K[0][1])