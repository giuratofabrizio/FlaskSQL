from flask import Flask, render_template, request
app = Flask(__name__)



@app.route('/', methods=['GET'])
def home():
    return render_template('search.html')


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






if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)