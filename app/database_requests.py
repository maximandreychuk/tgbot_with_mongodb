import pymongo


cluster = pymongo.MongoClient("mongodb://localhost:27017/")
base = cluster.shop
collection = base.registration

one_mov = collection.find_one({})

qt_mov = collection.find({"director": "Quentin Tarantino"}, {"title"})

