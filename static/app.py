
from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import os
import math

app = Flask(__name__)

def calcular_espessuras(N, CBRn, CBRsb, KR, KB, KSB):
    # Determina espessura do revestimento (R)
    if N <= 5e6:
        R = 5
    elif N <= 1e7:
        R = 7.5
    elif N <= 5e7:
        R = 10
    else:
        R = 12.5

    # Altura total até a base
    H20 = 77.67 * (N ** 0.0482) * (CBRsb ** -0.598)

    # Altura até a sub-base
    Hn = 77.67 * (N ** 0.0482) * (CBRn ** -0.598)

    # Espessura da base
    B = max(15, (H20 - R * KR) / KB)

    # Espessura da sub-base
    h20 = max(15, (Hn - R * KR - B * KB) / KSB)

    return round(R, 2), round(B, 2), round(h20, 2)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    grafico_path = None

    if request.method == "POST":
        try:
            N = float(request.form["N"])
            CBRn = float(request.form["CBRn"])
            CBRsb = float(request.form["CBRsb"])
            KR = float(request.form["KR"])
            KB = float(request.form["KB"])
            KSB = float(request.form["KSB"])

            R, B, h20 = calcular_espessuras(N, CBRn, CBRsb, KR, KB, KSB)

            resultado = {
                "R": R,
                "B": B,
                "Hsb": h20
            }

            # Criar gráfico
            fig, ax = plt.subplots(figsize=(3, 6))
            alturas = [R, B, h20]
            labels = ['Revestimento (R)', 'Base (B)', 'Sub-base (Hsb)']
            cores = ['#666666', '#999999', '#CCCCCC']

            bottom = 0
            for altura, cor, label in zip(alturas, cores, labels):
                ax.bar(0, altura, width=0.5, bottom=bottom, color=cor, label=f"{label}: {altura:.2f} cm")
                bottom += altura

            ax.set_ylim(0, sum(alturas) + 20)
            ax.axis('off')
            ax.legend()

            grafico_path = os.path.join("static", "grafico.png")
            fig.savefig(grafico_path, bbox_inches="tight")
            plt.close()

        except Exception as e:
            resultado = {"erro": str(e)}

    return render_template("index.html", resultado=resultado, grafico_path=grafico_path)

if __name__ == "__main__":
    from os import environ
    port = int(environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
