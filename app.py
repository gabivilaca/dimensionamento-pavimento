
from flask import Flask, render_template, request, send_file
import pdfkit
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    try:
        # Entrada de dados
        trafego = float(request.form['trafego'])
        vida_util = float(request.form['vida_util'])
        fator_pit = float(request.form['fator_pit'])
        tipo_solo = request.form['tipo_solo']

        # Cálculo do Número de Repetições (N)
        N = trafego * 365 * vida_util * fator_pit

        # Escolha do tipo de solo (valores representativos fictícios)
        solos = {
            "CBRn": {"subleito": 2, "revestimento": 5, "base": 20, "recalc_toleravel": 2.5},
            "CBRSB": {"subleito": 5, "revestimento": 7, "base": 25, "recalc_toleravel": 2.0},
            "KR": {"subleito": 10, "revestimento": 10, "base": 30, "recalc_toleravel": 1.5},
        }

        solo = solos.get(tipo_solo, solos["CBRn"])

        # Dimensionamento das camadas (valores ilustrativos)
        espessura_revestimento = solo["revestimento"]
        espessura_base = solo["base"]
        espessura_subleito = solo["subleito"]
        recalque = solo["recalc_toleravel"]

        return render_template("resultado.html",
                               N=round(N, 2),
                               revestimento=espessura_revestimento,
                               base=espessura_base,
                               subleito=espessura_subleito,
                               recalque=recalque)
    except Exception as e:
        return f"Erro nos cálculos: {e}"

@app.route('/gerar_pdf', methods=['POST'])
def gerar_pdf():
    try:
        rendered = render_template('resultado.html',
                                   N=request.form['N'],
                                   revestimento=request.form['revestimento'],
                                   base=request.form['base'],
                                   subleito=request.form['subleito'],
                                   recalque=request.form['recalque'])
        pdfkit.from_string(rendered, 'relatorio.pdf')
        return send_file('relatorio.pdf', as_attachment=True)
    except Exception as e:
        return f"Erro ao gerar PDF: {e}"

if __name__ == "__main__":
    app.run(debug=True)
