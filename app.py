from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/v1.0/predict', methods=['GET'])
def predict():
    def parse_float(value):
        try:
            return float(value)
        except (TypeError, ValueError):
            return 0.0

    a = parse_float(request.args.get('a'))
    b = parse_float(request.args.get('b'))
    total = a + b
    prediction = 1 if total > 5.8 else 0

    return jsonify({
        "prediction": prediction,
        "features": {
            "a": a,
            "b": b,
            "sum": total
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

