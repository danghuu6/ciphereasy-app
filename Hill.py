import numpy as np


class hill:
    def __init__(self, text, stringkey):
        self.text = text
        self.stringkey = stringkey
    def setText(self,text):
        self.text= text
    def setStringkey(self,stringkey):
        self.stringkey= stringkey
    # Đổi ký tự sang ma trận số
    def char_to_int(self, chr):  # ký tự
        chr = chr.upper()  # In hoa ký tự
        integer = ord(chr) - 65  # ord('A') = 65
        return integer

    # Tạo ma trận từ chuổi plantext hoặc chuổi khóa
    def create_matrix_to_integer_from_string(self, str, M):  # String str, Int M
        integers_list = []

        # Tạo list số nguyên của từng ký tự trong chuỗi
        for c in str:
            integers_list.append(self.char_to_int(c))

        length = len(integers_list)
        MT = np.zeros((int(length / M), M), dtype=np.int32)  # Ma trận 0 cấp M x M

        i = 0
        # Đưa các phần tử trong list số nguyên thành ma trận M x M
        for column in range(int(length / M)):
            for row in range(M):
                MT[column][row] = integers_list[i]
                i += 1

        return MT

    # Tìm định thức ma trận khóa và nghịc đảo cua nó
    def find_det_inverse(self, MT_key):  # MT là ma trận
        # Tính định thức ma trận, làm tròn định thức và chia chia phần dư 26
        det = round(np.linalg.det(MT_key)) % 26

        # Nếu không tìm thấy phần tử nghịch đảo trả về -1
        det_inverse = -1
        for i in range(26):
            inverse = det * i
            if inverse % 26 == 1:
                det_inverse = i
                break
        return det_inverse

    # Tìm M từ khóa
    def find_M_in_key(self):  # string_key là đoạn chuỗi khóa
        M = 2
        while True:
            if M * M == len(self.stringkey):
                break
            else:
                M = M + 1
        return M

    # Kiểm tra khóa có hợp lệ
    def check_key(self):
        str_key = self.stringkey.replace(" ", "")

        M = self.find_M_in_key()
        Key = self.create_matrix_to_integer_from_string(str_key, M)

        Key_matrix = np.matrix(Key)
        det = round(np.linalg.det(Key_matrix))
        det_inv = self.find_det_inverse(Key_matrix)
        # Nếu định thức ma trận khóa = 0 thì khóa không có ma trận nghịch đảo
        if det == 0:
            return False
        # Nếu tìm nghịch đảo định thức = -1 thì định thức không có phần tử nghịch đảo
        if det_inv == -1:
            return False
        return True

    # Mã hóa
    def hill_encrypt(self):
        # Xóa khảng trắng trong các đoạn text
        msg = self.text.replace(" ", "")
        string_key = self.stringkey.replace(" ", "")

        M = self.find_M_in_key()
        # print(M)
        # len_check = len(msg) % M == 0
        # if not len_check:
        #     msg += "z"

        # Cộng thêm số lượng z vào text
        while len(msg)%M != 0:
            msg+='0'

        # Khởi tạo ma trận Plaintext và khóa
        P = self.create_matrix_to_integer_from_string(msg, M)  # Plaintext
        Key = self.create_matrix_to_integer_from_string(string_key, M)  # Ma trận khóa

        # Đưa về ma trận để tính toán
        P_matrix = np.matrix(P)
        Key_matrix = np.matrix(Key)

        msg_len = int(len(msg) / M)


        encrypt_msg = ""
        for i in range(msg_len):
            C = P_matrix[i] * Key_matrix
            for j in range(M):
                integer = int(C[0, j] % 26 + 65)
                encrypt_msg += chr(integer)

        return encrypt_msg

    # Tìm nghịch đảo của khóa
    def key_inverse(self, MT_key):
        det = np.linalg.det(MT_key)  # Tính định thức
        adjunct_matrix = np.linalg.inv(MT_key) / (1 / det)  # Đưa về ma trận phụ hợp

        det_inverse = self.find_det_inverse(MT_key)  # tìm nghịch đảo của định thức 1/det(k)

        matrix_inverse = det_inverse * adjunct_matrix

        # Xét từng phần tử, nếu < 0 thì + 26
        for i in range(len(matrix_inverse)):
            for j in range(len(matrix_inverse)):
                matrix_inverse[i, j] %= 26
                # Làm tròn các phần tử để tránh sai số
                matrix_inverse[i,j] = round(matrix_inverse[i,j])

        return matrix_inverse


    def hill_decrypt(self):
        M = self.find_M_in_key()

        C = self.create_matrix_to_integer_from_string(self.text, M)
        Key = self.create_matrix_to_integer_from_string(self.stringkey, M)  # Ma trận khóa

        C_matrix = np.matrix(C)
        Key_matrix = np.matrix(Key)

        # K nghịch đảo
        Key_inverse = self.key_inverse(Key_matrix)

        msg_len = int(len(self.text) / M)

        decrypt_msg = ""

        for i in range(msg_len):
            P = C_matrix[i] * Key_inverse
            for j in range(M):
                integer = int(P[0, j] % 26 + 65)
                decrypt_msg += chr(integer)

        # Loại bỏ ký tự được thêm vào khi thực hiện giải mã
        # Kí tự '0' đươc thêm vào luôn luôn giải mã ra kí tự 'J'
        while decrypt_msg[-1] == 'J':
            decrypt_msg = decrypt_msg[:-1]

        return decrypt_msg
#
# k = 'lshduanlk'
# en_code = hill('nguyen huu dang super hero', k)
# en = en_code.hill_encrypt()
# de_code = hill(en, k)
# de = de_code.hill_decrypt()
#
# print(en)
# print(de)