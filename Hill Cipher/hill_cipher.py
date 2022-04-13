# TUGAS 2 Algoritma Hill Cipher
#   Naufal Firmansyah
#   A11.2019.12054
#   Kriptografi


def matriks(K1, K2, K3, K4):
    matriks = [[K1, K2], [K3, K4]]
    return matriks

def plaintext_proses(s):
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

#START kunci default dan setter
encrypted = True
K = matriks(5,6,2,3)
Praw = "Strike Now"
P = Praw.replace(" ","").lower()
C = ""
pisahP = plaintext_proses(Praw)

for i in pisahP:
    getIdx = []
    K_temp = []
    getIdx = [huruf.index(x)+1 for x in i]
    K_temp = [((K[0][0] * getIdx[0]) + (K[0][1] * getIdx[1])) % 26, ((K[1][0] * getIdx[0]) + (K[1][1] * getIdx[1])) % 26]
    for x in range(len(K_temp)):
        C += huruf[K_temp[x]-1]
# END kunci default dan setter

while True:
    print(f"""
{"="*40}
Hill Chiper

[1] Enkripsi
[2] Dekripsi
[3] Ganti PlainText
[4] Ganti Kunci
[0] Exit

PlainText saat ini: {Praw}
PlainText diproses: {P}
Kunci Saat ini:
{K[0][0], K[0][1]}
{K[1][0], K[1][1]}

Cipher Text:
{C}
{"="*40}
    """)
    uinp = input("Pilihan > ")
    if uinp == "0":
        print("Exit!")
        exit()
    elif uinp == "1":
        C = ""
        pisahP = plaintext_proses(Praw)

        for i in pisahP:
            getIdx = []
            K_temp = []
            getIdx = [huruf.index(x)+1 for x in i]
            K_temp = [((K[0][0] * getIdx[0]) + (K[0][1] * getIdx[1])) % 26, ((K[1][0] * getIdx[0]) + (K[1][1] * getIdx[1])) % 26]
            for x in range(len(K_temp)):
                C += huruf[K_temp[x]-1]
    elif uinp == "2":
        matriks_invers = [[K[1][1], K[0][1]*-1], [K[1][0]*-1, K[0][0]]]
        ad_min_bc = (matriks_invers[0][0] * matriks_invers[1][1]) - (matriks_invers[0][1] * matriks_invers[1][0])
        x_mod_mult_invers = ad_min_bc
        K_c = 1
        notfound = True
        while notfound:
            x_mod_mult_invers = ((1 + 26) * K_c)/ad_min_bc
            try:
                x_mod_mult_invers = int(x_mod_mult_invers)
            except:
                pass
            if type(x_mod_mult_invers) is int:
                notfound = False
            K_c += 1
            
        matriks_invers_next = [[matriks_invers[0][0]*x_mod_mult_invers, matriks_invers[0][1]*x_mod_mult_invers], [matriks_invers[1][0]*x_mod_mult_invers, matriks_invers[1][1]*x_mod_mult_invers]]
        pisahC = plaintext_proses(C)
        decryptC_Phasil = ""
        for i in pisahC:
                getIdx = []
                getIdx = [huruf.index(x)+1 for x in i]
                for x in getIdx:
                    decryptC_Phasil += huruf[x-1]
        print(decryptC_Phasil)
    elif uinp == "3":
        Praw = input("Masukkan PlainText>> ")
        P = Praw.replace(" ","").lower()
        print("Jangan Lupa Enkripsi Lagi !!")
    elif uinp == "4":
        print("""
Layout Matriks Kunci:
1a | 1b
2a | 2b     
        """)
        K = matriks(int(input("Angka 1a > ")), int(input("Angka 1b > ")), int(input("Angka 2a > ")), int(input("Angka 2b > ")))
    else:
        pass