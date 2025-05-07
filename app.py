
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        try:
            ce = float(request.form['ce'])
            tr = float(request.form['tr'])
            n = float(request.form['n'])
            fcn = float(request.form['fcn'])

            log_n = (log10(n) - log10(tr * ce)) / log10(fcn)
            resultado = round(log_n, 2)
        except Exception as e:
            resultado = f"Erro: {e}"
    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
