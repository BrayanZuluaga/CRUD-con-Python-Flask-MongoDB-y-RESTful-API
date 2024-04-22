from pymongo import MongoClient
import certifi

MONGO_URI = 'mongodb+srv://bbrayandavid2001:15kspzD2UQ1H6rdb@cluster0.sagniom.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["db_app_users"]
    except ConnectionError:
        print('Error de conexión con la base de datos')
    return db

#bbrayandavid2001
#15kspzD2UQ1H6rdb
#python -m pip install "pymongo[srv]"
#mongodb+srv://bbrayandavid2001:<password>@cluster0.sagniom.mongodb.net/
#mongodb+srv://bbrayandavid2001:15kspzD2UQ1H6rdb@cluster0.sagniom.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0