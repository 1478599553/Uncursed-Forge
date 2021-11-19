from flask import Flask,request,render_template
from flask_sqlalchemy import SQLAlchemy
import pymongo


app = Flask (__name__)

@app.route("/")
def index():
    itemList = []

    client = pymongo.MongoClient('localhost', 27017)
    db = client.uncursedforge
    collection = db.modsinfo
    res = collection.aggregate([{"$sample":{"size":1}}])
    for item in res:
        itemList.append(item['title'])
    return render_template('index.html',name=itemList)
    
if __name__ == "__main__":
    app.run(port=8000)