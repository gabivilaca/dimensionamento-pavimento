
from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    grafico_path = None
    if request.method == 'POST':
        try:
            R = float(request.form['R'])
            CBRsb = float(request.form['CBRsb'])
            CBRn = float(request.form['CBRn'])
            KR = float(request.form['KR'])
            KB = float(request.form['KB'])
            KSB = float(request.form['KSB'])

            H20 = round(77.67 * (10**4)**0.0482 * (CBRsb**-0.598), 4)
            Hn = round(77.67 * (10**4)**0.0482 * (CBRn**-0.598), 4)

            B = round((H20 - R * KR) / KB, 2)
            B = B if B > 15 else 15

            Hsb = round((Hn - R * KR - B * KB) / KSB, 2)
            Hsb = Hsb if Hsb > 15 else 15

            resultado = {
                'R': R,
                'B': B,
                'Hsb': Hsb
            }

            # Gráfico
            fig, ax = plt.subplots(figsize=(3, 6))
            alturas = [R, B, Hsb]
            labels = ['Revestimento (R)', 'Base (B)', 'Sub-base (Hsb)']
            cores = ['#555555', '#888888', '#CCCCCC']

            bottom = 0
            for altura, cor, label in zip(alturas, cores, labels):
                ax.bar(0, altura, width=1.0, bottom=bottom, color=cor, label=f"{label}: {altura:.2f} cm")
                bottom += altura

            ax.set_ylim(0, sum(alturas) + 10)
            ax.axis('off')
            ax.legend(loc='upper center')
            grafico_path = os.path.join('static', 'grafico.png')
            plt.savefig(grafico_path, bbox_inches='tight')
            plt.close()

        except Exception as e:
            resultado = f"Erro: {e}"

    return render_template('index.html', resultado=resultado, grafico_path=grafico_path)

if __name__ == "__main__":
    from os import environ
    port = int(environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
