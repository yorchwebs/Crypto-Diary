from flask import Flask, render_template

import cryptocompare

app = Flask(__name__)

CryptoCompare = 'CRYPTO_COMPARE_KEY'

moneda = []
nombre = ['Bitcoin','Ethereum','Tether','USD Coin','BNB','XRP','Binance USD','Cardano','Solana','Dogecoin']
precio_dolar = []
precio_peso = []

coins = cryptocompare.get_price(['BTC','ETH','USDT','USDC','BNB','XRP','BUSD','ADA','SOL','DOGE'], ['USD', 'MXN'])

for coin in coins:
    if coin == 'BTC':
        moneda.append(coin)
        precio_dolar.append('{:,.2f}'.format(coins['BTC']['USD']))
        precio_peso.append('{:,.2f}'.format(coins['BTC']['MXN']))
    if coin == 'ETH':
        moneda.append(coin)
        precio_dolar.append('{:,.2f}'.format(coins['ETH']['USD']))
        precio_peso.append('{:,.2f}'.format(coins['ETH']['MXN']))
    if coin == 'USDT':
        moneda.append(coin)
        precio_dolar.append('{:,.2f}'.format(coins['USDT']['USD']))
        precio_peso.append('{:,.2f}'.format(coins['USDT']['MXN']))
    if coin == 'USDC':
        moneda.append(coin)
        precio_dolar.append('{:,.2f}'.format(coins['USDC']['USD']))
        precio_peso.append('{:,.2f}'.format(coins['USDC']['MXN']))
    if coin == 'BNB':
        moneda.append(coin)
        precio_dolar.append('{:,.2f}'.format(coins['BNB']['USD']))
        precio_peso.append('{:,.2f}'.format(coins['BNB']['MXN']))
    if coin == 'XRP':
        moneda.append(coin)
        precio_dolar.append('{:,.2f}'.format(coins['XRP']['USD']))
        precio_peso.append('{:,.2f}'.format(coins['XRP']['MXN']))
    if coin == 'BUSD':
        moneda.append(coin)
        precio_dolar.append('{:,.2f}'.format(coins['BUSD']['USD']))
        precio_peso.append('{:,.2f}'.format(coins['BUSD']['MXN']))
    if coin == 'ADA':
        moneda.append(coin)
        precio_dolar.append('{:,.2f}'.format(coins['ADA']['USD']))
        precio_peso.append('{:,.2f}'.format(coins['ADA']['MXN']))
    if coin == 'SOL':
        moneda.append(coin)
        precio_dolar.append('{:,.2f}'.format(coins['SOL']['USD']))
        precio_peso.append('{:,.2f}'.format(coins['SOL']['MXN']))
    if coin == 'DOGE':
        moneda.append(coin)
        precio_dolar.append('{:,.2f}'.format(coins['DOGE']['USD']))
        precio_peso.append('{:,.2f}'.format(coins['DOGE']['MXN']))

def time():

    while True:
        for coin in coins:
            if coin == 'BTC':
                moneda.append(coin)
                precio_dolar.append('{:,.2f}'.format(coins['BTC']['USD']))
                precio_peso.append('{:,.2f}'.format(coins['BTC']['MXN']))
            if coin == 'ETH':
                moneda.append(coin)
                precio_dolar.append('{:,.2f}'.format(coins['ETH']['USD']))
                precio_peso.append('{:,.2f}'.format(coins['ETH']['MXN']))
            if coin == 'USDT':
                moneda.append(coin)
                precio_dolar.append('{:,.2f}'.format(coins['USDT']['USD']))
                precio_peso.append('{:,.2f}'.format(coins['USDT']['MXN']))
            if coin == 'USDC':
                moneda.append(coin)
                precio_dolar.append('{:,.2f}'.format(coins['USDC']['USD']))
                precio_peso.append('{:,.2f}'.format(coins['USDC']['MXN']))
            if coin == 'BNB':
                moneda.append(coin)
                precio_dolar.append('{:,.2f}'.format(coins['BNB']['USD']))
                precio_peso.append('{:,.2f}'.format(coins['BNB']['MXN']))
            if coin == 'XRP':
                moneda.append(coin)
                precio_dolar.append('{:,.2f}'.format(coins['XRP']['USD']))
                precio_peso.append('{:,.2f}'.format(coins['XRP']['MXN']))
            if coin == 'BUSD':
                moneda.append(coin)
                precio_dolar.append('{:,.2f}'.format(coins['BUSD']['USD']))
                precio_peso.append('{:,.2f}'.format(coins['BUSD']['MXN']))
            if coin == 'ADA':
                moneda.append(coin)
                precio_dolar.append('{:,.2f}'.format(coins['ADA']['USD']))
                precio_peso.append('{:,.2f}'.format(coins['ADA']['MXN']))
            if coin == 'SOL':
                moneda.append(coin)
                precio_dolar.append('{:,.2f}'.format(coins['SOL']['USD']))
                precio_peso.append('{:,.2f}'.format(coins['SOL']['MXN']))
            if coin == 'DOGE':
                moneda.append(coin)
                precio_dolar.append('{:,.2f}'.format(coins['DOGE']['USD']))
                precio_peso.append('{:,.2f}'.format(coins['DOGE']['MXN']))

monedas = moneda.copy()
nombres = nombre.copy()
dolares = precio_dolar.copy()
pesos = precio_peso.copy()

@app.route('/')
def index():

        return render_template('index.html', monedas=monedas, nombres=nombres, dolares=dolares, pesos=pesos)

if __name__ == '__main__':
    app.run(port=5000, debug=True)