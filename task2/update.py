from bson.objectid import ObjectId

from inputValues import inputField, inputName, inputID, isChange
def update_all(db):
    pk = inputID()
    if pk is None:
        return None
    cats = db.cats.find_one({"_id": ObjectId(pk)})
    if cats is None:
        return None
    
    [new_name, new_age, new_features] = inputField(True)
    name = new_name if new_name else cats["name"]
    age = new_age if new_age else cats["age"]
    features = new_features if new_features else cats["features"]
    return db.cats.update_one(
        {"_id": ObjectId(pk)},
        {"$set": {"name": name, "age": age, "features": features}},
    )


def update_age(db):
    name = inputName()
    cat = db.cats.find_one({"name": name})
    if cat is None:
        return None
    while True:
        try:
            age = int(input("Enter new age (0 - for exit): "))
            if age == "exit":
                return None
            break
        except ValueError:
            print("Invalid age")
    if age:
        return db.cats.update_one(
            {"name": name},
            {"$set": {"age": age}},
        )


def update_features(db):
    name = inputName()
    cat = db.cats.find_one({"name": name})
    if cat is None:
        return None
    features_new = []
    while True:
        feature = str(input("Enter new features('exit' for exit): "))
        if feature == "exit":
            break
        if feature == '':
            print("Feature can't be empty. Try again or 'exit' to exit.")
            continue
        features_new.append(feature)
    isDelete = False
    if len(features_new) == 0:
        print(f'Do you want delete all {name} features?')
        isDelete = isChange('features')
    features = features_new if not isDelete else cat["features"]
    return db.cats.update_one(
        {"name": name},
        {"$set": {"features": features}}
        )
