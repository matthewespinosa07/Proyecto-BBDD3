from flask import Flask, jsonify
import pandas as pd

app = Flask(_name_)

# Ruta para leer el CSV y devolver datos JSON
@app.route('/partidos')
def partidos():
    try:
        # Leer archivo CSV (asegúrate que la ruta sea correcta)
        df = pd.read_csv('partidos.csv')

        # Reemplazar NaN por None para evitar errores en JSON
        df = df.where(pd.notnull(df), None)

        # Convertir DataFrame a lista de diccionarios para jsonify
        datos = df.to_dict(orient='records')

        return jsonify(datos)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)