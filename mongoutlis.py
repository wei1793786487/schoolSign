import datetime
import time

import pymongo


myclient = pymongo.MongoClient("your mongo url")
mydb = myclient["school"]
mycol = mydb["sign"]
signcol=mydb["log"]


def getlist():
    return mycol.find()


def add(id,qq,name):
    mydict = {"id": id, "qq": qq,"name":name}
    x = mycol.insert_one(mydict)
    print(x.inserted_id)

def add_log(name,result,strftime):
    mydict = { "name": name, "time": strftime,"result":result}
    x = signcol.insert_one(mydict)
    print(x.inserted_id)

# add_log("demo","true")

