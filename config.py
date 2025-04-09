import pymongo
import certifi


con_str = "mongodb+srv://test:1234@cluster0.omnza6q.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())


db = client.get_database("test")
