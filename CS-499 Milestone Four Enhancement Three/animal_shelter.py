from pymongo import MongoClient

class AnimalShelter:
    """CRUD operations for the Animal collection in MongoDB."""

    def __init__(self, username='aacuser', password='CrossCrusaders707',
                 host='nv-desktop-services.apporto.com', port=30434,
                 db='AAC', collection='animals'):
        self.client = MongoClient(f"mongodb://{username}:{password}@{host}:{port}/?authSource=admin")
        self.database = self.client[db]
        self.collection = self.database[collection]

    def create(self, data):
        """Insert a document into the collection."""
        if data and isinstance(data, dict):
            result = self.collection.insert_one(data)
            return result.acknowledged
        return False

    def read(self, query={}):
        """Find documents matching a query and return them in a list."""
        return list(self.collection.find(query))

    def update(self, query, new_values):
        """Update document(s) matching query with new values."""
        if isinstance(query, dict) and isinstance(new_values, dict):
            result = self.collection.update_many(query, {"$set": new_values})
            return result.modified_count
        return 0

    def delete(self, query):
        """Delete document(s) matching query."""
        if isinstance(query, dict):
            result = self.collection.delete_many(query)
            return result.deleted_count
        return 0
