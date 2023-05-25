from flask import Flask, jsonify


app = Flask(__name__)

coin_prices = {
    "bitcoin": 43000,
    "ethereum": 2800,
    "bitcoin-cash": 600,
    "ripple": 1.05,
    "monero": 250,
    "dogecoin": 0.35
}


@app.route('/api/coin_prices', methods=['GET'])
def get_coin_prices():
    return jsonify(coin_prices)


if __name__ == '__main__':
    app.run(port=8010)
