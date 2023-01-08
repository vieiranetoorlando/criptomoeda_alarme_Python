import time
from datetime import datetime
import os
import yfinance as yf
from winotify import Notification, audio

symbols = ['btc-usd', 'eth-usd', 'aapl']
tickers = yf.Tickers(','.join(symbols))

#for symbol in symbols:
    #print(tickers.trickers[symbol.upper()].history(period='1d')['Close'][0])

upper_limits = [30000, 1500, 200]
lower_limits = [15000, 800, 100]

while True:
    last_prices = [tickers.tickers[symbol.upper()].history(period='1d')['Close'][0] for symbol in symbols]
    print(datetime.now())
    print(last_prices)
    time.sleep(2)
    for i in range(len(symbols)):
        if last_prices[i] > upper_limits[i]:
            #sell alert
            toast = Notification(app_id='Criptop Bot',
                title='Alerta de preco para ' + symbols[i].upper(),
                msg=f'{symbols[i].upper()} atingiu o preco de {last_prices[i]:.2f}. Voce talvez queira vender.',
                icon=os.path.join(os.getcwd(), 'sell.jpg'),
                duration='long',
                )
            toast.add_actions(label='Ir para Exchange', launch='https://www.binance.com')
            toast.set_audio(audio.LoopingAlarm6, loop=False)
            toast.show()   
        elif last_prices[i] > lower_limits[i]:
            #sell alert
            toast = Notification(app_id='Criptop Bot',
                title='Alerta de preco para ' + symbols[i].upper(),
                msg=f'{symbols[i].upper()} atingiu o preco de {last_prices[i]:.2f}. Voce talvez queira vender.',
                icon=os.path.join(os.getcwd(), 'buy.jpg'),
                duration='long',
                )
            toast.add_actions(label='Ir para Exchange', launch='https://www.binance.com')
            toast.set_audio(audio.LoopingAlarm6, loop=False)
            toast.show()   
        time.sleep(1) # evitar notificações simultaneas 