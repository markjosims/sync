import pymongo
import dns
import pprint
import json

client = pymongo.MongoClient("mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false")
db = client['bookdb']
Book = db['books']
    
    
def insert_docs():
    book_list = [
    {"title" : "Software Engineering", "_id" : "1"},
    {"title" : "Algorithm Design", "_id" : "2"},
    {"title" : "Architecture", "_id" : "3"},
    {"title" : "Python", "_id" : "4"},
    {"title": ["Intro to SQL 1", "Intro to SQL 2"],"_id": "5"}
    ]
    Book.insert_many(book_list)

def query_books():
    # print all documents in the book collection
    for i in db.Book.find():
        print(i)

def query_books_no_id():
# exclude the _id field
    for i in db.Book.find({}, {"_id" : 0}):
        print(i)
        
def regex_query():    
    A_query = {"title" : {"$regex": "^A"}}
    for i in db.Book.find(A_query):
        print(i)


insert