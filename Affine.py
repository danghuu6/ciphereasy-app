class affine():
    def __init__(self, text, a, b, n):
        self.text = text
        self.n = n
        self.a = a
        self.b = b
    def setText(self,text):
        self.text= text
    def setA(self,a):
        self.a= a
    def setB(self,b):
        self.b= b
    def setN(self,n):
        self.n= n
    def encrypt(self):
        k_a, k_b, k_i = self.a, self.b, self.n
        # xoa khoang trang
        text = self.text.replace(" ", "")
        result = ""
        # ma hoa tung ki tu
        for i in range(len(self.text)):
            char = self.text[i]
            result += chr((k_a * (ord(char) - 65) + k_b) % self.n + 65)

        return result

    def a_inverse(self, a):
        for i in range(self.n):
            if (a * i) % self.n == 1:
                return i
        return -1

    def decrypt(self):
        k_a, k_b, k_i = self.a, self.b, self.n
        # xoa khoang trang
        self.text = self.text.replace(" ", "")
        result = ""
        # giai ma tung ki tu
        for i in range(len(self.text)):
            char = self.text[i]
            result += chr(self.a_inverse(self.a)*((ord(char) - 65)-self.b) % self.n +65)
        return result
