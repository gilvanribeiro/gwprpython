import urllib
import numpy as np
import matplotlib.pyplot as plt

# http://earthquake.usgs.gov/earthquakes/feed/v1.0/csv.php
source = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/"

# Magnitude > 4.5
url = urllib.urlopen(source + "4.5_month.csv")

data = url.read().split('\n')[1:-1] #excluir cabecalho e ultima linha, pois esta' vazia
url.close()
#Algum codigo processando os dados lidos

dadosSeparados=[]
time = []
latitude = []
longitude = []
mag = []
place = []
tamanho = []
cor = []
for row in data:
    dadosSeparados.append(row.split(','))

for row in dadosSeparados:
#    time.append(row[0])
    if row[4] > "5":
        mag.append(float(row[4]))
        tamanho.append(float(row[4])**4)
        cor.append(float(row[4])/10.0)
        latitude.append(float(row[1]))
        longitude.append(float(row[2]))
        if "km" not in row[13]:
            place.append(row[13].replace('"', ''))
        else:
            place.append(row[14].replace('"', ''))

plt.figure(figsize=(14, 10))
plt.subplot(1, 1, 1)
plt.scatter(longitude, latitude, marker='o', color=cor, s=tamanho)
plt.grid(True, linestyle="-", color='0.75',linewidth=0.75)
# Restante do codigo para gerar o grafico
plt.title('Terremotos com magnitude > 4.5 nos ultimos 30 dias')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()