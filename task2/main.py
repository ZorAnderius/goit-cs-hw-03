from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from create import create, initialize_db
from read import read, readByName
from update import update_all, update_age, update_features
from delete import delete, delete_by_name, delete_all

template = """
              1. Create
              
              2. Show all cats
              3. Show cat by name
              
              4. Update all fields by ID
              5. Update cat's age by name
              6. Update cat's features by name
              
              7. Delete by ID
              8. Delete by name
              9. Delete all
              
              10. Initialize database with 10 random cats
              0. Exit
              """

def main():
    uri = "mongodb://localhost:27017"

    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi("1"))

    db = client.hw3_task2
    while True:
        print(template)
        try:
            action = int(input("Enter number of action: "))
        except ValueError:
            print("Wrong action")
            continue

        match action:
            case 1:
                r = create(db)
                print(r.inserted_id)
            case 2:
                cats = read(db)
                [print(cat) for cat in cats]
            case 3:
                cat = readByName(db)
                print(cat if cat else "Cat not found")
            case 4:
                r = update_all(db)
                print(r.modified_count if r else "Cat was not found")
            case 5:
                r = update_age(db)
                print(r.modified_count if r else "Cat was not found or update was cancelled")
            case 6:
                r = update_features(db)
                print(r.modified_count if r else "Cat was not found")
            case 7:
                r = delete(db)
                print(r.deleted_count)
            case 8:
                r = delete_by_name(db)
                print(r.deleted_count)
            case 9:
                r = delete_all(db)
                print(r.deleted_count)
            case 10:
                initialize_db(db)
            case 0:
                print("Bye-bey my charry pie!")
                break
            case _:
                print("Wrong action")


if __name__ == "__main__":
    main()
