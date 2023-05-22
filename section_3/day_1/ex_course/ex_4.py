# from pymongo import MongoClient

# category = input("Escolha uma categoria: ")

# with MongoClient as client:
#     db = client.library

#     books_by_category = db.books.find({"categories": category}, projection=["title"])

#     for book in books_by_category:
#         print(book["title"])

from pymongo import MongoClient


category = input("Escolha uma categoria: ")
with MongoClient() as client:
    db = client.library
    for book in db.books.find({"categories": category}, projection=["title"]):
        print(book["title"])
