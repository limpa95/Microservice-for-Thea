# Name: Patrick Lim
# OSU Email: limpa@oregonstate.edu
# Course: CS361 - Software Engineering
# Assignment: 9: Microservice Implementation
# Due Date: 2/26/24
# Description:
# This program tests the microservice by taking user information as input and communicates with a separate microservice
# to store this information on MongoDB.

import time
import pymongo
from bson.objectid import ObjectId

while True:
    client = pymongo.MongoClient('mongodb+srv://limpa:3EdzbRf1XLsWBv50@microservice.yamy7n5.mongodb.net/'
                                 '?retryWrites=true&w=majority&appName=Microservice')

    db = client.microservice

    accounts_collection = db.test

    read_txt = open('pat-microservice.txt', 'r+', encoding="utf-8")
    read_txt.seek(0)
    read_txt.truncate()
    read_txt.write("standby")
    read_txt.close()

    name_prompt = input('Please enter your name:')
    id_prompt = input('Please enter your id number:')
    line_list = [name_prompt + "\n", id_prompt + "\n"]

    read_txt = open('pat-microservice.txt', 'r+', encoding="utf-8")
    read_txt.seek(0)
    read_txt.truncate()
    read_txt.writelines(line_list)
    read_txt.close()

    time.sleep(8)
    read_txt = open('pat-microservice.txt', 'r+', encoding="utf-8")
    read_txt.seek(0)
    document_id = read_txt.read()
    print(document_id)
    find_document = {"_id": ObjectId(document_id)}
    result = accounts_collection.find_one(find_document)
    print(result)


    read_txt.close()