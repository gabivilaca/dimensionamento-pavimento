
from flask import Flask, render_template, request, send_file
import pdfkit
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    try:
        N = float(request.form['N'])
        CBRn = float(request.form['CBRn'])
        CBRSB = float(request.form['CBRSB'])
        KR = float(request.form['KR'])
        KB = float(request.form['KB'])
        KSB = float(request.form['KSB'])

        # Cálculo de cada camada
        hR = ((N / (CBRn * KR)) ** 0.25) * 10
        hB = ((N / (CBRSB * KB)) ** 0.25) * 10
        hSB = ((N / (CBRSB * KSB)) ** 0.25) * 10

        # Gera relatório PDF
        rendered = render_template('resultado.html', N=N, CBRn=CBRn, CBRSB=CBRSB, KR=KR, KB=KB, KSB=KSB, hR=hR, hB=hB, hSB=hSB, data=datetime.now())
        path_wkhtmltopdf = '/usr/bin/wkhtmltopdf'
        config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf) if os.path.exists(path_wkhtmltopdf) else None
        pdfkit.from_string(rendered, 'relatorio.pdf', configuration=config)

        return send_file('relatorio.pdf', as_attachment=True)

    except Exception as e:
        return f"Ocorreu um erro: {e}"

if __name__ == '__main__':
    app.run(debug=True)
