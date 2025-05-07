
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
            carga = float(request.form['carga'])
            fator = float(request.form['fator'])
            trafego = float(request.form['trafego'])

            # Cálculo de espessuras
            hn = round((carga * fator * trafego) / 100000, 1)
            hb = round(hn * 0.7, 1)
            hsb = round(hn * 1.5, 1)

            resultado = {
                'hn': hn,
                'hb': hb,
                'hsb': hsb,
                'explicacoes': {
                    'hn': 'Espessura da camada de rolamento (cm)',
                    'hb': 'Espessura da base (cm)',
                    'hsb': 'Espessura da sub-base (cm)'
                }
            }

            # Criar gráfico
            fig, ax = plt.subplots(figsize=(2.5, 6))
            cores = ['#666666', '#999999', '#CCCCCC']
            alturas = [hn, hb, hsb]
            labels = ['Hn', 'Hb', 'Hsb']

            bottom = 0
            for altura, cor, label in zip(alturas, cores, labels):
                ax.bar(0, altura, width=0.5, bottom=bottom, color=cor, label=label)
                bottom += altura

            ax.set_ylim(0, sum(alturas) + 10)
            ax.axis('off')
            ax.legend()

            grafico_path = os.path.join('static', 'grafico.png')
            plt.savefig(os.path.join('static', 'grafico.png'), bbox_inches='tight')
            plt.close()

        except Exception as e:
            resultado = f"Ocorreu um erro: {e}"

    return render_template('index.html', resultado=resultado, grafico_path=grafico_path)

if __name__ == '__main__':
    app.run(debug=True)
