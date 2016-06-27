import urllib
import numpy as np
import matplotlib.pyplot as plt


# http://earthquake.usgs.gov/earthquakes/feed/v1.0/csv.php
source = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/"

# Magnitude > 4.5
url = urllib.urlopen(source + "4.5_month.csv")
data = url.read().split('\n')[1:-1] #excluir cabecalho e ultima linha, pois esta' vazia
url.close()
# Algum codigo processando os dados lidos
dadosSeparados=[]
time = []
latitude = []
longitude = []
mag = []
place = []
tamanho = []
cor = []
aux = []
for row in data:
    dadosSeparados.append(row.split(','))

for row in dadosSeparados:
    if row[4] > "5":
        time.append(row[0])
        mag.append(float(row[4]))
        tamanho.append(float(row[4])**4)
        cor.append(float(row[4])/10.0)
        latitude.append(float(row[1]))
        longitude.append(float(row[2]))
        if "km" not in row[13]:
            place.append(row[13].replace('"', ''))
        else:
            place.append(row[14].replace('"', ''))
for row in time :
    print row
plt.figure(figsize=(14,10))
plt.axes([0.10, 0.17, 0.8, 0.73])
plt.xticks(index, time,rotation=90,size='small')
plt.plot(mag);
#plt.show()
# Restante do codigo para gerar o grafico
