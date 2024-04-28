import argparse
from bson.objectid import ObjectId

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb://localhost:27017"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi("1"))

db = client.hw3_task2

def isChange(title):
    while True:
        change = str(input(f"Change {title} Y/N: "))
        if change:
            change = change.lower()
            if  change == "y":
                return False
            elif change == "n":
                return True
        print("Wrong input. Try again or 'exit' to exit")

def inputField(update=False):
    change = False
    name = None
    age = None
    features = None
    if update:
        change = isChange('name')
    if not change:
        name = str(input("Enter name: "))

    if update:
        change = isChange("age")
    if not change:
            while True:
                try:
                    age = int(input("Enter age: "))
                    break
                except ValueError:
                    print("Invalid age")

    if update:
        change = isChange("all features")
    if not change:
        features = []
    while True and not change:
        feature = str(input("Enter features('exit' for exit): "))
        if feature == 'exit':
            break
        features.append(feature)
    return (name, age, features)


def read():
    cats = db.cats.find()
    return cats


def create():
    [name, age, features] = inputField()
    return db.cats.insert_one({"name": name, "age": age, "features": features})


def update():
    pk = str(input("Enter id: "))
    [new_name, new_age, new_features] = inputField(True)
    cats = db.cats.find_one({"_id": ObjectId(pk)})

    name = new_name if new_name  else cats['name']
    age = new_age if new_age else cats['age']
    features =new_features if new_features else cats['features']
    return db.cats.update_one(
        {"_id": ObjectId(pk)},
        {"$set": {"name": name, "age": age, "features": features}},
    )


def delete():
    pk = str(input("Enter id: "))
    return db.cats.delete_one({"_id": ObjectId(pk)})


if __name__ == "__main__":
    while True:
        print("""
              1. Create
              2. Read
              3. Update
              4. Delete
              5. Exit
              """
        )
        try:
            action = int(input("Enter number of action: "))
        except ValueError:
            print('Wrong action')
            continue
        
        match action:
            case 1:
                r = create()
                print(r.inserted_id)
            case 2:
                [print(cat) for cat in read()]
            case 3:
                r = update()
                print(r.modified_count)
            case 4:
                r = delete()
                print(r.deleted_count)
            case 5:
                print("Bye-bey my charry pie!")
                break
            case _:
                print("Wrong action")
