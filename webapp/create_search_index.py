import pymongo
import sys 
from pymongo.mongo_client import MongoClient
from pymongo.operations import SearchIndexModel


sys.path.insert(1, '../config/')
from config_database import mongo_uri, db, collection



# Connect to your Atlas deployment

client = MongoClient(mongo_uri)
# Access your database and collection
database = client[db]
collection = database[collection]
# Create your index model, then create the search index
search_index_model = SearchIndexModel(
  definition = {
    "fields": [ 
              {
                "numDimensions": 768,
                "path": "imageVector",
                "similarity": "cosine",
                "type": "vector"
              },
              {
                "path": "price",
                "type": "filter"
              },
              {
                "path": "averageRating",
                "type": "filter"
              },
              {
                "path": "discountPercentage",
                "type": "filter"
              }
      ]
  },
  name="default",
  type="vectorSearch",
)
result = collection.create_search_index(model=search_index_model)
print(result)
