class vigenere:
    def __init__(self, text, k):
        self.text=text
        self.k=k
    def setText(self,text):
        self.text= text
    def setkey(self,k):
        self.k= k
    #Mã hoá
    def encrypt(self):
        # Xoá khoảng trắng
        txt = self.text.replace(" ","")
        # Chia bản rõ theo dộ dài của khoá k. Ví du: k = "KEY" thì độ dài khoá là 3
        # Ví dụ bản rõ là: CANTHOUNIVERSITY thì sẽ chia théo độ dài của khoá (k= 3) là: CAN |THO |UNI |VER |SIT |Y
        key_length = len(self.k)
        key_as_int = [ord(i) for i in self.k]
        plaintext_int = [ord(i) for i in txt]
        ciphertext = ''

        # Chuyển đổi plantext thành số thứ tự của chúng tương ứng trong bảng chữ cái và cộng với khoá k (mod 26)
        for i in range(len(plaintext_int)):
            value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
            ciphertext += chr(value + 65)
        return ciphertext

    #Giải mã
    def decrypt(self):
        # Xoá khoảng trắng
        txt = self.text.replace(" ", "")
        # Chia mật mã theo độ dài của khoá. Ví du: k = "KEY" thì độ dài khoá là 3
        # Ví dụ mật mã là: MELDLMERGFIPCMRI thì sẽ được chia theo độ dài của khoá (k = 3) là MEL |DLM |ERG |FIP |CMR |I
        key_length = len(self.k)
        key_as_int = [ord(i) for i in self.k]
        ciphertext_int = [ord(i) for i in txt]
        plaintext = ''

        # Chuyển đổi mật mã thành số thứ tự của chúng tương ứng trong bảng chữ cái và trừ với khoá k (mod 26)
        for i in range(len(ciphertext_int)):
            value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
            plaintext += chr(value + 65)
        return plaintext