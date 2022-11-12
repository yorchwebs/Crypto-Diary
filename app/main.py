from flask import Flask, render_template

# Importamos el Módulo CryptoCompare.
import cryptocompare

# Iniciamos la Aplicación.
app = Flask(__name__)

# Llave para accesar a los datos de CryptoCompare.
CryptoCompare = 'CRYPTO_COMPARE_KEY'

# Ruta y función para obtener datos.
@app.route('/')
def index():

    # Obtenemos los datos de CryptoCompare de cada una de las monedas indicadas, así como los precios en Dolares y Pesos Mexicanos.
    # Éstos los gardamos en la variable 'coins'.
    coins = cryptocompare.get_price(['BTC','ETH','USDT','USDC','BNB','XRP','BUSD','ADA','SOL','DOGE'], ['USD', 'MXN'])

    # Por medio de un ciclo While, repetimos la acción de obtener los precios de cda moneda, éste se repetirá infinitamente,
    # Siempre y cuando el valor obtenido sea verdadero (True).
    while True:

        # Por medio de un ciclo for, recorremos los elementos obtenidos en la variable 'coins'. Por medio de if condicionamos cada una
        # de los recorridos, obteniendo valores y guardándolos en nuevas variables específicas.
        for coin in coins:
            
            if coin == 'BTC':
                # Nueva variable moneda_btc con el precio del Bitcoin.
                moneda_btc = (coin)
                # Obtnemos el precio en Dólares.
                precio_dolar_btc = ('{:,.2f}'.format(coins['BTC']['USD']))
                # Obtenemos el precio en Pesos Mexicanos.
                precio_peso_btc = ('{:,.2f}'.format(coins['BTC']['MXN']))

            if coin == 'ETH':
                # Nueva variable moneda_btc con el precio del Ethereum.
                moneda_eth = (coin)
                # Obtnemos el precio en Dólares.
                precio_dolar_eth = ('{:,.2f}'.format(coins['ETH']['USD']))
                # Obtenemos el precio en Pesos Mexicanos.
                precio_peso_eth = ('{:,.2f}'.format(coins['ETH']['MXN']))

            if coin == 'USDT':
                # Nueva variable moneda_btc con el precio del Tether.
                moneda_usdt = (coin)
                # Obtnemos el precio en Dólares.
                precio_dolar_usdt = ('{:,.2f}'.format(coins['USDT']['USD']))
                # Obtenemos el precio en Pesos Mexicanos.
                precio_peso_usdt = ('{:,.2f}'.format(coins['USDT']['MXN']))

            if coin == 'USDC':
                # Nueva variable moneda_btc con el precio del USD Coin.
                moneda_usdc = (coin)
                # Obtnemos el precio en Dólares.
                precio_dolar_usdc = ('{:,.2f}'.format(coins['USDC']['USD']))
                # Obtenemos el precio en Pesos Mexicanos.
                precio_peso_usdc = ('{:,.2f}'.format(coins['USDC']['MXN']))

            if coin == 'BNB':
                # Nueva variable moneda_btc con el precio del Binance Coin.
                moneda_bnb = (coin)
                # Obtnemos el precio en Dólares.
                precio_dolar_bnb = ('{:,.2f}'.format(coins['BNB']['USD']))
                # Obtenemos el precio en Pesos Mexicanos.
                precio_peso_bnb = ('{:,.2f}'.format(coins['BNB']['MXN']))

            if coin == 'XRP':
                # Nueva variable moneda_btc con el precio del XRP.
                moneda_xrp = (coin)
                # Obtnemos el precio en Dólares.
                precio_dolar_xrp = ('{:,.2f}'.format(coins['XRP']['USD']))
                # Obtenemos el precio en Pesos Mexicanos.
                precio_peso_xrp = ('{:,.2f}'.format(coins['XRP']['MXN']))

            if coin == 'BUSD':
                # Nueva variable moneda_btc con el precio del Binance USD.
                moneda_busd = (coin)
                # Obtnemos el precio en Dólares.
                precio_dolar_busd = ('{:,.2f}'.format(coins['BUSD']['USD']))
                # Obtenemos el precio en Pesos Mexicanos.
                precio_peso_busd = ('{:,.2f}'.format(coins['BUSD']['MXN']))

            if coin == 'ADA':
                # Nueva variable moneda_btc con el precio del Cardano.
                moneda_ada = (coin)
                # Obtnemos el precio en Dólares.
                precio_dolar_ada = ('{:,.2f}'.format(coins['ADA']['USD']))
                # Obtenemos el precio en Pesos Mexicanos.
                precio_peso_ada = ('{:,.2f}'.format(coins['ADA']['MXN']))

            if coin == 'SOL':
                # Nueva variable moneda_btc con el precio del Solana.
                moneda_sol = (coin)
                # Obtnemos el precio en Dólares.
                precio_dolar_sol = ('{:,.2f}'.format(coins['SOL']['USD']))
                # Obtenemos el precio en Pesos Mexicanos.
                precio_peso_sol = ('{:,.2f}'.format(coins['SOL']['MXN']))

            if coin == 'DOGE':
                # Nueva variable moneda_btc con el precio del Dogecoin.
                moneda_doge = (coin)
                # Obtnemos el precio en Dólares.
                precio_dolar_doge = ('{:,.2f}'.format(coins['DOGE']['USD']))
                # Obtenemos el precio en Pesos Mexicanos.
                precio_peso_doge = ('{:,.2f}'.format(coins['DOGE']['MXN']))

        # Las variables que reciben todos los datos de los símbolos y las distintas monedas.
        monedas = [moneda_btc, moneda_eth, moneda_usdt, moneda_usdc, moneda_bnb, moneda_xrp, moneda_busd, moneda_ada, moneda_sol, moneda_doge]
        nombres = ['Bitcoin','Ethereum','Tether','USD Coin','Binance Coin','XRP','Binance USD','Cardano','Solana','Dogecoin']
        dolares = [precio_dolar_btc, precio_dolar_eth, precio_dolar_usdt, precio_dolar_usdc, precio_dolar_bnb, precio_dolar_xrp, precio_dolar_busd, precio_dolar_ada, precio_dolar_sol, precio_dolar_doge]
        pesos = [precio_peso_btc, precio_peso_eth, precio_peso_usdt, precio_peso_usdc, precio_peso_bnb, precio_peso_xrp, precio_peso_busd, precio_peso_ada, precio_peso_sol, precio_peso_doge]

        # Enviamos la información a la plantilla 'index.html', creando una conexión entre la APP y la Plantilla.
        # Desde la plantilla podemos acceder a ésta información.
        return render_template('index.html', monedas=monedas, nombres=nombres, dolares=dolares, pesos=pesos)

# Indicamos que en éste modulo debe iniciar la aplicación.
if __name__ == '__main__':
    app.run()