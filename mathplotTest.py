import numpy as np
import matplotlib.pyplot as plt
import json

# x = []
valor = []
arq = open("intraday_5min_MSFT.json", "r")
data = json.load(arq)
arq.close()

timeSeries = data["Time Series (5min)"]
preco = [float(dado["1. open"]) for dado in timeSeries.values()]

# for key, value in timeSeries.items():
#     valor.append(key)

for i in range(0,1101):
    valor.append(i)

plt.plot(valor, preco)

plt.show()

# x = [int(i) for i in range(10)] # uma outra fora de dar append em uma lista