from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/welcome', methods=['GET'])
def welcome():
    nome = request.args.get('nome')
    if not nome:
        return jsonify({"message": "Por favor, forneça um nome." }), 400
    return jsonify({"message": f"Bem-vindo, {nome}!" })


@app.route('/carbon_footprint', methods=['POST'])
def carbon_footprint():
    data = request.json


    try:
        eletricidade_kwh = float(data.get('eletricidade_kwh', 0))
        km_carro = float(data.get('km_carro', 0))
        carne_kg = float(data.get('carne_kg', 0))
    except ValueError:
        return jsonify({"message": "Os valores devem ser numéricos."}), 400
    
    pegada_eletricidade = eletricidade_kwh * 0.233
    pegada_carro = km_carro * 0.21
    pegada_carne = carne_kg * 27

    pegada_total = pegada_eletricidade + pegada_carro + pegada_carne

    return jsonify({
        "pegada_eletricidade": pegada_eletricidade,
        "pegada_carro": pegada_carro,
        "pegada_carne": pegada_carne,
        "pegada_total": pegada_total,
        "equivalente_arvores": pegada_total / 21


    })

if __name__ =='__main__':
    app.run(debug=True)