import urllib
import numpy as np
import matplotlib.pyplot as plt


# http://earthquake.usgs.gov/earthquakes/feed/v1.0/csv.php
source = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/"

# Magnitude > 4.5
url = urllib.urlopen(source + "4.5_month.csv")

data = url.read().split('\n')[1:-1] #excluir cabecalho e ultima linha, pois esta' vazia

# Algum codigo processando os dados lidos

plt.figure(figsize=(14,10))
plt.axes([0.10, 0.17, 0.8, 0.73])

# Restante do codigo para gerar o grafico
