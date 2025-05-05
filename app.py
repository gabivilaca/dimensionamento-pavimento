from flask import Flask, render_template, request

app = Flask(__name__)

def calcular_espessuras(cbr, n):
    if cbr < 5:
        sub_base = 25
    elif cbr < 10:
        sub_base = 20
    else:
        sub_base = 15

    base = 20
    revestimento = 5 + (n / 1_000_000)
    return round(revestimento, 1), base, sub_base

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        cbr = float(request.form["cbr"])
        n = float(request.form["n"])
        vida_util = int(request.form["vida_util"])
        trafego = request.form["trafego"]

        revestimento, base, sub_base = calcular_espessuras(cbr, n)

        return render_template("resultado.html",
                               cbr=cbr, n=n, vida_util=vida_util, trafego=trafego,
                               revestimento=revestimento, base=base, sub_base=sub_base)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
