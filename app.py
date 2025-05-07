
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        try:
            # Cálculo simplificado apenas para exemplo
            trafego = float(request.form['trafego'])
            cbr = float(request.form['cbr'])
            modulo = float(request.form['modulo'])
            coeficiente = float(request.form['coeficiente'])
            camada = float(request.form['camada'])
            fatork = float(request.form['fatork'])
            espessura = round(trafego * coeficiente / (cbr * fatork + modulo + camada), 2)
            resultado = f"Espessura calculada: {espessura} cm"
        except Exception as e:
            resultado = f"Erro nos cálculos: {str(e)}"
    return render_template('index.html', resultado=resultado)
