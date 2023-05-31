import http.client
import json
from flask import Flask, render_template


app = Flask(__name__)


def get_coin_prices():
    coins = ["bitcoin", "ethereum", "bitcoin-cash", "ripple", "monero", "dogecoin"]
    conn = http.client.HTTPSConnection("api.coingecko.com")
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) /'
                             'Chrome/58.0.3029.110 Safari/537.3'}
    conn.request("GET", f"/api/v3/simple/price?ids={','.join(coins)}&vs_currencies=usd", headers=headers)
    response = conn.getresponse()
    data = json.loads(response.read().decode())
    conn.close()
    return {coin: data[coin]['usd'] for coin in coins}


@app.route('/')
def index():
    coin_prices = get_coin_prices()
    return render_template('index.html', coin_prices=coin_prices)


if __name__ == '__main__':
    app.run(port=8007)
