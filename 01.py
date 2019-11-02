import json
import requests
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import time
import threading
from datetime import datetime

tot = 0
r = None

def gerador():
    global tot
    global r
    global stock
    if r != None:
        valor = []
        data = r.json()
        now = datetime.now()
        timeSeries = data["Time Series (5min)"]
        open = [float(dado["1. open"]) for dado in timeSeries.values()]

        # print("gerador =>           " + str(open))
        # print("{} {} {}".format(now.hour,now.minute,now.second))


        for i in range(len(open)):
            valor.append(i)

        plt.figure(num=None, figsize=(6, 2.85), dpi=100, facecolor='w', edgecolor='k')
        plt.plot(valor,open[::-1])

        if stockvalue == "ABEV3":
            plt.savefig('stocks/ABEV3/'+'c'+str(tot)+'books_read.jpeg')
        if stockvalue == "MGLU3":
            plt.savefig('stocks/MGLU3/' + 'c' + str(tot) + 'books_read.jpeg')
        if stockvalue == "PETR4":
            plt.savefig('stocks/PETR4/' + 'c' + str(tot) + 'books_read.jpeg')
        if stockvalue == "ITUB4":
            plt.savefig('stocks/ITUB4/' + 'c' + str(tot) + 'books_read.jpeg')

        tot += 1

def atualizaRequest(stock):
    global r
    global stockvalue
    stockvalue = stock
    while True:
        if stock == "ABEV3":
            r = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=ABEV3.SA&interval=5min&apikey=234234")
        if stock == "MGLU3":
            r = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MGLU3.SA&interval=5min&apikey=224234")
        if stock == "PETR4":
            r = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=PETR4.SA&interval=5min&apikey=284234")
        if stock == "ITUB4":
            r = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=ITUB4.SA&interval=5min&apikey=234834")

        data = r.json()
        now = datetime.now()

        timeSeries = data["Time Series (5min)"]
        open = [float(dado["1. open"]) for dado in timeSeries.values()]

        # print("atualizaRequest =>   " + str(open))
        # print("{} {} {}".format(now.hour,now.minute,now.second))

        gerador()

        time.sleep(295)
print(0)
thread1 = threading.Thread(target=atualizaRequest("MGLU3"))
thread1.start()


    # thread3 = threading.Thread(target=atualizaRequest("PETR4"))
    # thread3.start()
    #
    # thread4 = threading.Thread(target=atualizaRequest("ITUB4"))
    # thread4.start()
