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
treta = []

for row in data:
    dadosSeparados.append(row.split(','))

for row in dadosSeparados:
#    latitude.append(row[1])
#    longitude.append(row[2])
#    time.append(row[0])
    if row[4] > "5":
        mag.append(int(float(row[4])))
        if "km" not in row[13]:
            place.append(row[13].replace('"', ''))
        else:
            place.append(row[14].replace('"', ''))

index = [x for x in range(len(mag))]
print mag

# Algum codigo para continuar configurando o grafico

# Restante do codigo para gerar o grafico
plt.axes([0.10, 0.25, 0.8, 0.65])
plt.xticks(index, place,rotation=90,size='small')
plt.title('Distribuicao diaria de terremotos nos ultimos 31 dias')
plt.xlabel('Localizacao')
plt.ylabel('Numero de Terremotos')
plt.bar(index, mag,color='g')
plt.show()
