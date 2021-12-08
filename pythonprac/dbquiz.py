from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

movie = db.movies.find_one({'title':'매트릭스'},{'_id':False})
target_star = movie['star']

same_star = list(db.movies.find({'star':'9.39'}, {'_id': False}))
for movie in same_star:
    print(movie['title'])

db.movies.update_one({'title':'매트릭스'},{'$set':{'star':'0'}})