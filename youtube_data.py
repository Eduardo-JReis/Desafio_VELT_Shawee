## Importando as libs
import youtube_dl
import pandas as pd
import numpy as np

import time
import json
import matplotlib as mp


# Definindo as queries para pesquisar
queries = ["day-trade", "como+investir"]

ydl = youtube_dl.YoutubeDL({"ignoreerrors": True})

# Buscando os vídeos no Youtube
# podemos alterar a quantidade de videos baixados no ytsearchdate100, neste caso
# irá baixar 100 vídeos de cada query
resultados = []
for query in queries:
    r = ydl.extract_info("ytsearchdate100:{}".format(query), download=False)
    for entry in r['entries']:
        if entry is not None:
            entry['query'] = query
    resultados += r['entries']  



resultados = [e for e in resultados if e is not None]
# verificando a quantidade de vídeos baixados
len(resultados)



df = pd.DataFrame(resultados)

# As colunas que iremos utilizar
colunas = ['title', 'upload_date', 'view_count']
df['upload_date'] = pd.to_datetime(df["upload_date"])

# Calculando o tempo desde a publicação
df['tempo_desde_pub'] = (pd.to_datetime("2020-11-14") - df["upload_date"]) / np.timedelta64(1, 'D')



pd.set_option("display.max_columns", 65)
df[colunas].head()

# Pegando apenas os videos que tem mais do que 100 visualizações
df_views_maior_que_cem = df[df['view_count'] > 10]
df_views_maior_que_cem[colunas]


# Convertendo o Dataframe em Json e salvando o arquivo
df_views_maior_que_cem[colunas].to_json(r"./json/parsed_videos.json")


# Abrindo o arquivo Json
with open("./json/parsed_videos.json") as f:
   data = json.load(f)
print(data)

# Lendo o arquivo Json
print(pd.DataFrame(data))

# A proxima etapa será a apresentação dos gráficos
# e aplicação das features para predição e análise dos dados
# usando técnicas de Machine Learning 


