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
        cbr = float(request.form['cbr'])
        n = float(request.form['n'])
        k = float(request.form['k'])

        ht = 77.67 * (n**0.0442) * (cbr**-0.2654)
        h = round(ht, 2)

        h1 = round(h * k / 10, 2)
        h2 = round((h - h1) / 2, 2)
        h3 = round(h - h1 - h2, 2)

        return render_template('resultado.html', h=h, h1=h1, h2=h2, h3=h3, cbr=cbr, n=n, k=k)
    except Exception as e:
        return f"Erro nos cálculos: {e}"

@app.route('/gerar_pdf', methods=['POST'])
def gerar_pdf():
    rendered = render_template('resultado.html',
        h=request.form['h'],
        h1=request.form['h1'],
        h2=request.form['h2'],
        h3=request.form['h3'],
        cbr=request.form['cbr'],
        n=request.form['n'],
        k=request.form['k']
    )
    path_wkhtmltopdf = '/usr/bin/wkhtmltopdf' if os.name != 'nt' else r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    pdfkit.from_string(rendered, 'relatorio.pdf', configuration=config)
    return send_file('relatorio.pdf', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)