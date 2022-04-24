from Hill import hill
from Vigenere import vigenere
from Caesar import caesar
from RSA import rsa
from Des import des
from Affine import affine
from flask import Flask, render_template, request

app = Flask(__name__)

hill_code = hill(None, None)
vigenere_code = vigenere(None, None)
caesar_code = caesar(None, None)
rsa_code = rsa(None, None, None, None)
rsa_de = rsa(None, None, None, None)
des_code = des()
affine_code = affine(None, None, None, None)


# route
@app.route("/", methods=['GET', 'POST'])
def main():
    return render_template("index1.html")


@app.route("/hill_page", methods=['GET', 'POST'])
def hill_page():
    return render_template("hill.html")


@app.route("/affine_page", methods=['GET', 'POST'])
def affine_page():
    return render_template("affine.html")


@app.route("/caesar_page", methods=['GET', 'POST'])
def caesar_page():
    return render_template("caesar.html")


@app.route("/rsa_page", methods=['GET', 'POST'])
def rsa_page():
    return render_template("rsa.html")


@app.route("/vigenere_page", methods=['GET', 'POST'])
def vigenere_page():
    return render_template("vigenere.html")


@app.route("/des_page", methods=['GET', 'POST'])
def des_page():
    return render_template("des.html")


@app.route("/hill", methods=['GET', 'POST'])
def hill():
    if request.method == 'POST':
        txt = request.form.get('my_text')
        k = request.form.get('my_key')
        action = request.form.get('actioncode')
        hill_code.setText(txt)
        hill_code.setStringkey(k)
        if action=='en':
            res = hill_code.hill_encrypt()
        if action=='de':
            res = hill_code.hill_decrypt()
        return render_template("hill.html", en=res)


@app.route("/vigenere", methods=['GET', 'POST'])
def vigenere():
    if request.method == 'POST':
        action = request.form.get('actioncode')
        txt = request.form.get('plantext')
        k = request.form.get('key')

        vigenere_code.setText(txt)
        vigenere_code.setkey(k)
        if action=='en':
            res = vigenere_code.encrypt()
        if action=='de':
            res = vigenere_code.decrypt()
        return render_template('vigenere.html', en=res)


@app.route("/caesar", methods=['GET', 'POST'])
def caesar():
    if request.method == 'POST':
        action = request.form.get('actioncode')
        txt = request.form.get('plantext')
        k = request.form.get('key')
        k = int(k)
        caesar_code.setText(txt)
        caesar_code.setkey(k)
        if action=='en':
            res = caesar_code.ca_encrypt()
        if action=='de':
            res= caesar_code.ca_decrypt()
        return render_template('caesar.html', en=res)


@app.route("/rsa", methods=['GET', 'POST'])
def rsa():
    if request.method == 'POST':
        action =request.form.get('actioncode')
        txt = request.form.get('plantext')
        p = request.form.get('p')
        q = request.form.get('q')
        e = request.form.get('e')
        e = int(e)
        q = int(q)
        p = int(p)
        if action == 'en':
            rsa_code.setText(txt)
            rsa_code.setE(e)
            rsa_code.setP(p)
            rsa_code.setQ(q)
            res = rsa_code.rsa_mahoa()
        if action == 'de':
            rsa_code.setE(e)
            rsa_code.setP(p)
            rsa_code.setQ(q)
            txt = txt.replace(" ", "")
            txt = txt[1:-1]
            arr=[]
            for e in txt.split(','):
                arr.append(int(e))
            rsa_code.setText(arr)
            res = rsa_code.rsa_giaima()
        return render_template('rsa.html', en=res)


@app.route("/des", methods=['GET', 'POST'])
def des():
    if request.method == 'POST':
        action = request.form.get('actioncode')
        txt = request.form.get('plantext')
        k = request.form.get('key')

        des_code.setAttr(txt, k)
        en = des_code.encrypt()
        if action=='en':
            res = des_code.encrypt()
        if action=='de':
            res = des_code.decrypt()
        return render_template('des.html', en=res)


@app.route("/affine", methods=['GET', 'POST'])
def affine():
    if request.method == 'POST':
        action = request.form.get('actioncode')
        txt = request.form.get('plantext')
        a = request.form.get('a')
        b = request.form.get('b')
        n = request.form.get('n')
        a = int(a)
        b = int(b)
        n = int(n)
        affine_code.setText(txt)
        affine_code.setA(a)
        affine_code.setB(b)
        affine_code.setN(n)
        if action=='en':
            res = affine_code.encrypt()
        if action=='de':
            res = affine_code.decrypt()
        return render_template('affine.html', en=res)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port='6868')
