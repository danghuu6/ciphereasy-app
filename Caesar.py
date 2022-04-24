class caesar:
  def __init__(self, text, k):
    self.text = text
    self.k = k
  def setText(self, text):
    self.text = text
  def setkey(self, k):
    self.k = k
  def ca_encrypt(self):
    text = self.text.replace(" ","")
    result = ""
    for i in range(len(text)):
      char = text[i]
      # Ma hoa bang cach chuyen doi ki tu o vi tri i den vi tri i+k
      # Neu ki tu dau vao la chu in hoa thi gia tri tinh toan se la 65 (Vi gia tri cua A trong Ascii la 65)
      if (char.isupper()):
        result += chr((ord(char) + self.k - 65) % 26 + 65)
      else:
      # Neu ki tu dau vao la chu in hoa thi gia tri tinh toan se la 97 (Vi gia tri cua a trong Ascii la 97)
        result += chr((ord(char) + self.k - 97) % 26 + 97)
      #print(result)
    return result
  def ca_decrypt(self):
    text = self.text.replace(" ","")
    result = ""
    for i in range(len(text)):
      char = text[i]
      if (char.isupper()):
      # Giai ma bang cach chuyen doi ki tu o vi tri i den vi tri i+k
      # Nguoc lai voi cach ma hoa thay vi cong voi k se tien hanh tien len gia tri con giai ma se tru k di tra ve gia tri ban dau
        result += chr((ord(char) - self.k - 65) % 26 + 65)
      else:
        result += chr((ord(char) - self.k - 97) % 26 + 97)
    return result