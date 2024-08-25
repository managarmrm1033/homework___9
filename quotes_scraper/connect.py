import pymongo
import json

# MongoDB Connection
client = pymongo.MongoClient("mongodb+srv://managarm:506e29ff@cluster0.vkganap.mongodb.net/test?retryWrites=true&w=majority")
db = client["test"]

# Load data from JSON files
with open('quotes.json', 'r') as quotes_file:
    quotes_data = json.load(quotes_file)
with open('authors.json', 'r') as authors_file:
    authors_data = json.load(authors_file)

# Insert data into MongoDB
quotes_collection = db["quotes"]
authors_collection = db["authors"]

# Insert quotes data
quotes_collection.insert_many(quotes_data)

# Insert authors data
authors_collection.insert_many(authors_data)

print("Data successfully uploaded to MongoDB.")

# Close the MongoDB connection
client.close()
