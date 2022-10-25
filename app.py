from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)



@app.route('/', methods=['GET'])
def home():
    return render_template('radio.html')


@app.route("/select", methods=["GET"])
def elenco():
    scelta= request.args["scelta"]

    if scelta == "es1":
        return redirect(url_for("es1"))
    elif scelta == "es2":
        return render_template("es2.html")
    elif scelta == "es3":
        return render_template("es3.html")
    elif scelta == "es4":
        return render_template("search.html")




@app.route('/result', methods=['GET'])
def result():
    # collegamento database
    import pandas as pd
    import pymssql
    conn = pymssql.connect(server='213.140.22.237\SQLEXPRESS', user= 'giurato.fabrizio', password='xxx123##', database='giurato.fabrizio')

    # invio query al database e ricezione informazioni
    NomeProdotto = request.args['nomeProdotto']
    query = f"select * from production.products where product_name like '{NomeProdotto}%'"
    dfProdotti = pd.read_sql(query,conn)

    # far visualizare le informazioni all'utente
 
    return render_template('result.html', nomiColonne = dfProdotti.columns.values, dati = list(dfProdotti.values.tolist()))



@app.route("/es1", methods=["GET"])
def es1():
    query = f'SELECT category_name, count(*) as numero_prodotti FROM production.products inner join production.categories on categories.category_id = products.category_id group by category_name'
    dfCategorie = pd.read_sql(query,conn)
    return render_template('es1.html', nomiColonne = dfCategorie.columns.values, dati = list(dfCategorie.values.tolist()))


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)