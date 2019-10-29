import numpy as np
import matplotlib.pyplot as plt
import json

# x = []
valor = []
arq = open("Stock/intraday_5min_MGLU3.json", "r")
data = json.load(arq)
arq.close()

arq2 = open("techIndicators/intraday_5min_MGLU3.json", "r")
data2 = json.load(arq2)
arq2.close()

timeSeries = data["Time Series (5min)"]
mediaMovel = data2["Technical Analysis: SMA"]

preco = [float(dado["1. open"]) for dado in timeSeries.values()]
media = [float(dado["SMA"]) for dado in mediaMovel.values()]

print(len(preco))
print(len(media))

# for key, value in timeSeries.items():
#     valor.append(key)

# print(len(media))
# for i in range(0,100):
#     valor.append(i)

# plt.plot(valor, media)
# plt.plot(valor, preco)

# plt.show()

# x = [int(i) for i in range(10)] # uma outra fora de dar append em uma lista