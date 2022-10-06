import urllib 
import pymongo

# %% Class for holding NoSQL (fx MongoDB) data base
class Mongo:
    def __init__(self, db_name: str,
                 collection_name: str,
                 db_cfg: dict) -> None:
        """
        Prepare the class by reading YAML file

        Parameters
        ----------
        db_name: str
            Name of the DB
        collection_name: str
            Name of the collection    
        db_cfg : dict
            dict with DB definitions
            Keys: user, password, host: all str            

        Returns
        -------
        None.

        """
        self.get_db(db_name, db_cfg)
        self.get_collection(collection_name)

    def get_db(self, db_name: str, db_cfg: dict) -> object:
        """
        Get a hook to the DB of name 'db_name'

        Parameters
        ----------
        db_name : string, optional
            Optional name. If None the name form YAML file is taken

        Returns
        -------
        db

        """
        self.cfg = db_cfg
        self.name = db_name
        if db_cfg['host'] == 'local':
            self.CONNECTION_STRING = \
                'mongodb://localhost:27017/?retryWrites=true&w=majority'
        else:
            USR = db_cfg["user"]
            PW = urllib.parse.quote_plus(db_cfg["password"])
            HOST = db_cfg["host"]
            self.CONNECTION_STRING = \
                f'mongodb+srv://{USR}:{PW}@{HOST}/?retryWrites=true&w=majority'
        self.client = pymongo.MongoClient(self.CONNECTION_STRING)
        self.db = self.client.get_database(db_name)

        return self.db

    def get_collection(self, collection_name: str) -> object:
        self.collection = self.db.get_collection(collection_name) \
            if collection_name else None
        return self.collection

    def get_all_records(self) -> object:
        """
        Get all records of a collection

        Returns
        -------
        object
            DESCRIPTION.

        """
        return self.get_records(None)

    def get_one(self) -> object:
        """
        Get first record in collection

        Returns
        -------
        object
            first record.

        """
        return self.collection.find_one()

    def get_id(self, id) -> object:
        """
        Get record with '_id' = id

        Parameters
        ----------
        id : TYPE of _id fiels

        Returns
        -------
        object
            record with '_id' = id.

        """
        return self.collection.find({"_id": id}).next()

    def get_all_collections(self) -> list:
        return [c['name'] for c in self.db.list_collections()]

    def get_records(self, filter_dict: dict) -> list:
        return [r for r in self.collection.find(filter_dict)]

    def insert_one(self, item) -> None:
        self.collection.insert_one(item)

    def insert_many(self, list_of_dicts: list) -> None:
        self.collection.insert_many(list_of_dicts)

    def delete_one(self, filter_dict: dict) -> None:
        self.collection.delete_one(filter_dict)

    def delete_many(self, filter_dict: dict) -> None:
        self.collection.delete_many(filter_dict)
