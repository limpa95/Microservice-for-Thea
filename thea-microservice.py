# Name: Patrick Lim
# OSU Email: limpa@oregonstate.edu
# Course: CS361 - Software Engineering
# Assignment: 9: Microservice Implementation
# Due Date: 2/26/24
# Description:
# This microservice communicates via txt file and stores user information on MongoDB. It returns the document ID
# through the txt file so that the user information can be accessed by another microservice.

import time
import pymongo
import os
from dotenv import load_dotenv

while True:
    read_txt = open('pat-microservice.txt', 'r+', encoding="utf-8")
    read_txt.seek(0)
    if read_txt.read() != "standby":
        load_dotenv()
        my_id = os.getenv("ID")
        my_key = os.getenv("KEY")
        client = pymongo.MongoClient(f'mongodb+srv://{my_id}:{my_key}@microservice.yamy7n5.mongodb.net/'
                                     '?retryWrites=true&w=majority&appName=Microservice')

        db = client.microservice

        accounts_collection = db.test

        account_info = read_txt.read()

        for db_name in client.list_database_names():
            print(db_name)

        read_txt.seek(0)
        lines = [line.strip() for line in read_txt.readlines()]

        name = lines[0]
        id = lines[1]
        dob = lines[2]
        email = lines[3]

        new_account = {
            "name": name,
            "account_id": id,
            "dob": dob,
            "email": email
        }

        result = accounts_collection.insert_one(new_account)

        document_id = result.inserted_id
        read_txt.seek(0)
        read_txt.truncate()
        read_txt.write(str(document_id))
        read_txt.close()
        print("_id of inserted document:", document_id)
        time.sleep(10)


        client.close()
    else:
        read_txt.close()
        continue
