#PREPARANDO CONEXÃO COM TWITTER

# Importando os módulos Tweepy, Datetime e Json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from datetime import datetime
import json
# Importando do PyMongo o módulo MongoClient
from pymongo import MongoClient 
# Importando o módulo Pandas para trabalhar com datasets em Python
import pandas as pd

# Adicione aqui sua Consumer Key
consumer_key = "62vP2XbCQCARr45T1eRfujFRj"

# Adicione aqui sua Consumer Secret 
consumer_secret = "Kn7egXFl3rXDey4lNwDnI8Z15z5ns8HcRFVs4K3SpC7l5Cw9EQ"

# Adicione aqui seu Access Token
access_token = "38415536-PDDBURjESabE3v0QCoO985jLYgepgbkjC1ebKWi9H"

# Adicione aqui seu Access Token Secret
access_token_secret = "plhW2jtEazLERfCESoOsgZdpTPu3DCVQ5Anf3k8RAv8A6"

# Criando as chaves de autenticação
auth = OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

# Criando uma classe para capturar os stream de dados do Twitter e 
# armazenar no MongoDB
class MyListener(StreamListener):
    def on_data(self, dados):
        tweet = json.loads(dados)
        created_at = tweet["created_at"]
        id_str = tweet["id_str"]
        text = tweet["text"]
        obj = {"created_at":created_at,"id_str":id_str,"text":text,}
        tweetind = col.insert_one(obj).inserted_id
        print (obj)
        return True

# Criando o objeto mylistener
mylistener = MyListener()

# Criando o objeto mystream
mystream = Stream(auth, listener = mylistener)

#PREPARANDO CONEXÃO COM MONGODB

# Criando a conexão ao MongoDB
client = MongoClient('localhost', 27017)

# Criando o banco de dados twitterdb
db = client.twitterdb

# Criando a collection "col"
col = db.tweets 

# Criando uma lista de palavras chave para buscar nos Tweets
keywords = ['Sebrae', 'Sebrae Minas', 'Sebrae/MG', 'Sebrae-MG']

#COLETANDO OS TWEETS
# Iniciando o filtro e gravando os tweets no MongoDB
mystream.filter(track=keywords)

# Verificando um documento no collection
#col.find_one()
#teste = col.find_one()
#teste = str(teste)

#print(teste)

mystream.disconnect()

# criando um dataset com dados retornados do MongoDB
dataset = [{"created_at": item["created_at"], "text": item["text"],} for item in col.find()]

# Criando um dataframe a partir do dataset 
df = pd.DataFrame(dataset)

# Imprimindo o dataframe
#df
print(df["text"])

print('terminou')