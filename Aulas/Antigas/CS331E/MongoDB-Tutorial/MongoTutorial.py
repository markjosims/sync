import pymongo
import dns
import pprint
import json

client = pymongo.MongoClient("mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false")

def main():
    pp = pprint.PrettyPrinter(indent=2)
    db = client['bookdb']
    books = db['books']
    add_books(books)
    result = books.aggregate([
        { "$unwind": "$tags" },
        { "$project": { "_id": 0, "name": 1, "tags": 1, "author": 1 } }
    ])
    for obj in result:
        print(obj)
    #result = find_and_project(books)

def add_books(books):
    books.delete_many({})
    with open('books.json', 'r') as f:
        data = json.load(f)
    books.insert_many(data['books'])

def find_all_books(books):
    return [b for b in books.find({})]
    
def find_and_project(books):
    return result
    
def unwind_tags(books):
    pass
    
def courses_aggregate():
    pp = pprint.PrettyPrinter(indent=2)
    db = client['playground']
    courses = db['courses']
    result = courses.aggregate([
        { "$match": {"author": "Mark", "isPublished": True} },
        #{ "$addFields": { "users": 20 } },
        { "$project": {"_id": 0, "name": 1, "price": 1 , "tags": 1} },
        #{ "$group": {"_id": "$price", "totaldocs": { "$sum": 1 } } },
        #{ "$out": "aggResults" },
        { "$unwind": "$tags" },
        { "$sort": { "price": 1 } },
        { "$limit": 5 }
    ])
    for item in result:
        pp.pprint(item)
        
if __name__ == '__main__':
    main()