from pymongo import MongoClient

MONGO_CLIENT = MongoClient('localhost', 27017)
NEWS_DB = MONGO_CLIENT['news']
NEWS_CONTENT_COLLECTION = NEWS_DB.news_content