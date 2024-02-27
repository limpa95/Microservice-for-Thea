Communication Contract

* To fully implement this microservice, you will need access to my MongoDB database. I have stored the credential information in a .env file that has not been uploaded to GitHub for security. You will need the id and password to connect to MongoDB and access the stored data.

Clear instructions for how to programmatically REQUEST data from the microservice you implemented. Include an example call.
  
  * To request data from this microservice, a program must communicate through a txt file and also connect to a specified MongoDB database where data will be stored. Recommended modules include, time, pymongo, bson.objectID, os, and dotenv.
  It is required to first write the string "standby" in a txt file named pat-microservice.txt in order for the program to loop properly. 
  The program will start implementing the request when the contents of the txt file change to anything besides "standby". For example, if a program wanted to make a request to store data on a database using this microservice, it would having to first write "standby" to pat-microservice.txt before 
  running the microservice locally in terminal, start the microservice, then write the information it wants to store to the txt file as a dictionary so that MongoDB can process the create/insertion operation correctly. The program will then automatically provide the document id through the txt file
  so that the program can receive data from the MongoDB server. Finally, the program will need to again write the string "standby" to the txt file so that the microservice does not continously run.

Clear instructions for how to programmatically RECEIVE data from the microservice you implemented.

  * To receive data from this microservice, a program must save the document id communicated through the pat-microservice.txt file, likely as a variable in a list or dictionary. The id can be used to make a read operation to MongoDB and retrieve the specified document's data.
  For example, this can be done using pymongo by creating a variable such as find_document = {"_id": ObjectId(document_id)}. Then, this variable can be passed as a parameter to .find_one(), ex: .find_one(find_document). The value from this operation will be
  the data stored in the specified document on MongoDB, which will be in the form of a dictionary.

UML sequence diagram showing how requesting and receiving data works. Make it detailed enough that your partner (and your grader) will understand

![uml-diagram](https://github.com/limpa95/Microservice-for-Thea/assets/122480059/93421c29-a34f-4b5c-92d4-2495fce5aad3)

