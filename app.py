from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    if request.method == "POST":
        try:
            N = float(request.form["N"])
            CBRn = float(request.form["CBRn"])
            CBRsb = float(request.form["CBRsb"])
            KR = float(request.form["KR"])
            KB = float(request.form["KB"])
            KSB = float(request.form["KSB"])

            # Cálculo das espessuras
            Hn = KR * (77.67 * (N**0.0442) * (CBRn**-0.548))
            Hb = KB * (77.67 * (N**0.0442) * (CBRsb**-0.548))
            Hsb = KSB * (77.67 * (N**0.0442) * (CBRsb**-0.548))

            # Geração do gráfico das camadas
            fig, ax = plt.subplots(figsize=(5, 2))
            layers = [Hsb, Hb, Hn]
            labels = ['Subleito (Hsb)', 'Base (Hb)', 'Reforço (Hn)']
            y_offset = 0
            for i in range(3):
                ax.barh(0, width=layers[i], left=y_offset, label=f"{labels[i]}: {layers[i]:.2f} cm")
                y_offset += layers[i]
            ax.set_xlim(0, y_offset + 10)
            ax.set_ylim(-1, 1)
            ax.axis('off')
            ax.legend(loc='center', bbox_to_anchor=(0.5, -0.2), ncol=1)
            output_path = os.path.join("static", "grafico_espessura.png")
            plt.savefig(output_path, bbox_inches="tight")
            plt.close()

            resultado = {
                "Hn": round(Hn, 2),
                "Hb": round(Hb, 2),
                "Hsb": round(Hsb, 2),
                "grafico": output_path
            }
        except Exception as e:
            resultado = {"erro": str(e)}
    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)