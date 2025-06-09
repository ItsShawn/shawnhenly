import os
import logging
from pymongo import MongoClient, ASCENDING
from pymongo.errors import PyMongoError

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AnimalShelter:
    """Enhanced CRUD operations for the Animal collection in MongoDB with secure and modular design."""

    def __init__(self,
                 username='aacuser',
                 password='CrossCrusaders707',
                 host='nv-desktop-services.apporto.com',
                 port=30434,
                 db_name='AAC',
                 collection_name='animals'):
        """
        Initialize the MongoDB connection with default credentials or environment variables.
        Creates indexes to improve query performance.
        """
        try:
            # Load from environment if available
            username = os.getenv('MONGO_USERNAME', username)
            password = os.getenv('MONGO_PASSWORD', password)
            host = os.getenv('MONGO_HOST', host)
            port = int(os.getenv('MONGO_PORT', port))

            self.client = MongoClient(f"mongodb://{username}:{password}@{host}:{port}/?authSource=admin")
            self.database = self.client[db_name]
            self.collection = self.database[collection_name]

            # Create indexes for high-use fields
            self.collection.create_index([("breed", ASCENDING)])
            self.collection.create_index([("location", ASCENDING)])
            self.collection.create_index([("adoption_status", ASCENDING)])

            logging.info("MongoDB connection established and indexes created.")
        except Exception as e:
            logging.error(f"Failed to initialize AnimalShelter: {e}")
            raise

    def create(self, data):
        """
        Insert a document into the collection.
        Returns True if successful, False otherwise.
        """
        try:
            if data and isinstance(data, dict):
                result = self.collection.insert_one(data)
                logging.info(f"Document inserted with _id: {result.inserted_id}")
                return result.acknowledged
            else:
                logging.warning("Invalid data provided to create().")
                return False
        except PyMongoError as e:
            logging.error(f"Create operation failed: {e}")
            return False

    def read(self, query={}):
        """
        Find documents matching a query and return them in a list.
        Returns an empty list if query is invalid or fails.
        """
        try:
            if not isinstance(query, dict):
                logging.warning("Invalid query passed to read(). Returning empty list.")
                return []
            results = list(self.collection.find(query))
            logging.info(f"Read operation successful. Returned {len(results)} documents.")
            return results
        except PyMongoError as e:
            logging.error(f"Read operation failed: {e}")
            return []

    def update(self, query, new_values):
        """
        Update document(s) matching query with new values.
        Returns number of documents updated.
        """
        try:
            if isinstance(query, dict) and isinstance(new_values, dict):
                result = self.collection.update_many(query, {"$set": new_values})
                logging.info(f"Updated {result.modified_count} documents.")
                return result.modified_count
            else:
                logging.warning("Invalid input to update(). No update performed.")
                return 0
        except PyMongoError as e:
            logging.error(f"Update operation failed: {e}")
            return 0

    def delete(self, query):
        """
        Delete document(s) matching query.
        Returns number of documents deleted.
        """
        try:
            if isinstance(query, dict):
                result = self.collection.delete_many(query)
                logging.info(f"Deleted {result.deleted_count} documents.")
                return result.deleted_count
            else:
                logging.warning("Invalid query for delete(). No deletion performed.")
                return 0
        except PyMongoError as e:
            logging.error(f"Delete operation failed: {e}")
            return 0
