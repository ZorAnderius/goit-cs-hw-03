from bson.objectid import ObjectId

from inputValues import inputID, inputName

def delete(db):
    pk = inputID()
    return db.cats.delete_one({"_id": ObjectId(pk)})


def delete_by_name(db):
    name = inputName()
    return db.cats.delete_one({"name": name})


def delete_all(db):
    return db.cats.delete_many({})
