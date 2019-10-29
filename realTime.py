import json
import requests 
import matplotlib.pyplot as plt
import time
import threading

class main:
    def __init__(self):
        self.preco = []
        self.tempo = []

    def stonks(self):
        r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=PETR4.SA&interval=5min&apikey=238423')
        data = r.json()

        timeSeries = data["Time Series (5min)"]
        self.preco = [float(dado["1. open"]) for dado in timeSeries.values()]

        for i in range(len(self.preco)):
            self.tempo.append(i)

    def atualizaGrafico(self):
        while True:
            self.stonks()
            plt.plot(self.tempo, self.preco)
            plt.show()

investir = main()
investir.atualizaGrafico()

