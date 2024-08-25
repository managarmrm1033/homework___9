import json
import pymongo
import logging

class QuotesScraperPipeline:
    def open_spider(self, spider):
        logging.info("Opening spider and setting up MongoDB connection")
        self.quotes_data = []
        self.authors_data = []
        self.authors_seen = set()

        # MongoDB connection
        self.client = pymongo.MongoClient("mongodb+srv://managarm:506e29ff@cluster0.vkganap.mongodb.net/test?retryWrites=true&w=majority")
        self.db = self.client["test"]
        self.quotes_collection = self.db["quotes"]
        self.authors_collection = self.db["authors"]

    def close_spider(self, spider):
        logging.info("Closing spider and saving data to files and MongoDB")
        with open('quotes.json', 'w') as f:
            json.dump(self.quotes_data, f, ensure_ascii=False, indent=4)
        with open('authors.json', 'w') as f:
            json.dump(self.authors_data, f, ensure_ascii=False, indent=4)
        self.client.close()

    def process_item(self, item, spider):
        if "author_url" in item:  # It's a quote item
            logging.info(f"Processing quote item: {item}")
            self.quotes_data.append(item)
            self.quotes_collection.update_one(
                {"quote": item["quote"]},
                {"$set": dict(item)},
                upsert=True
            )
        else:  # It's an author item
            logging.info(f"Processing author item: {item}")
            if item["author"] not in self.authors_seen:
                self.authors_seen.add(item["author"])
                self.authors_data.append(item)
                self.authors_collection.update_one(
                    {"author": item["author"]},
                    {"$set": dict(item)},
                    upsert=True
                )
        return item
