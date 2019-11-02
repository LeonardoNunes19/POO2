import json
import requests 
import matplotlib.pyplot as plt
import time
import threading

tot = 0

def stonks():
    global tot
    global tempo, preco
    tempo = []
    preco = []
    r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=PETR4.SA&interval=5min&apikey=238423')
    data = r.json()

    timeSeries = data["Time Series (5min)"]
    preco = [float(dado["4. close"]) for dado in timeSeries.values()]
    preco.reverse()
    
    for i in range(len(preco)):
        tempo.append(i)
    tot += 1
    

def atualizaGrafico():
    while True:
        stonks()
        print(len(preco))
        print('--------------------------------------')
        print(len(tempo))
        plt.plot(tempo, preco)
        plt.savefig('images/'+'c'+str(tot)+'books_read.png')
        # plt.show()
        time.sleep(5)

atualizaGrafico()