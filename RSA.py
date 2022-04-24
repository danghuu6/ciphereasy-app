class rsa():
    def __init__(self, text, e, p, q):
        self.text = text
        self.e = e
        self.p = p
        self.q = q
    def setText(self,text):
        self.text=text
    def setE(self,e):
        self.e=e
    def setP(self,p):
        self.p=p
    def setQ(self,q):
        self.q=q
    def isPrime(self, x):
        if x == 1:
            return True
        for i in range(2, x):
            if x % i == 0:
                return False
        return True;

    def rsa_mahoa(self):  # e vs N la khoa cong khai
        N = self.p * self.q
        plaintext = self.text.replace(" ", "")  # xoa khoang trang
        ciphertext = []
        for i in range(len(plaintext)):
            char = plaintext[i]
            if (char.isupper()):  # kiem tra chua hoa chu thuong
                cipe = ord(char)  # chuyen chu ve dang so
                cipe = pow(cipe, self.e) % N
                ciphertext.append(cipe)
            else:
                cipe = ord(char)
                cipe = pow(cipe, self.e) % N
                ciphertext.append(cipe)
        return ciphertext

    def tinh(self):
        n = self.p * self.q
        d = 0
        phin = (self.p - 1) * (self.q - 1)
        for i in range(phin):
            du = (self.e * i) % phin
            if (du == 1):
                d = i
        return d
    def rsa_giaima(self):  # q va q la khoa bi mat va la 2 so nguyen to
        ciphertext = ''
        d = self.tinh()
        N = self.p * self.q
        for i in range(len(self.text)):
            char = self.text[i]
            cipe = pow(char, d) % N
            ciphertext += chr(cipe)
        return ciphertext
# gg =rsa('nguyennguyen',3,11,47)
# en= gg.rsa_mahoa()
# print(en)
# gg =rsa(en,3,11,47)
# print(gg.rsa_giaima())
