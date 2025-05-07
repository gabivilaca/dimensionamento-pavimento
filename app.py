
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        try:
            N = float(request.form['N'])
            CBRn = float(request.form['CBRn'])
            CBRsb = float(request.form['CBRsb'])
            KR = float(request.form['KR'])
            KB = float(request.form['KB'])
            KSB = float(request.form['KSB'])

            Hn = KR * (77.67 * (N**0.0442) * (CBRn**-0.548))
            Hb = KB * (77.67 * (N**0.0442) * (CBRsb**-0.548))
            Hsb = KSB * (77.67 * (N**0.0442) * (CBRsb**-0.548))

            resultado = {'Hn': round(Hn, 2), 'Hb': round(Hb, 2), 'Hsb': round(Hsb, 2)}
        except Exception as e:
            resultado = {'erro': str(e)}
    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
