from flask import Flask,request,render_template,url_for
from flask_sqlalchemy import SQLAlchemy
import pymongo


app = Flask (__name__)

@app.route("/")
def index():
    itemList = []
    modPage = []
    modThumbnailIcon = []
    modTitle = []
    modSummary = []
    modThumbnailIconURL_list = []
    indexPageList = []

    client = pymongo.MongoClient('localhost', 27017)
    db = client.uncursedforge
    collection = db.modsinfo
    res = collection.aggregate([{"$sample":{"size":10}}])
    for item in res:
        modTitle.append(item['title'])
        modSummary.append(item['summary'])
        modThumbnailIcon.append(item['icon_file_name'])
    for icon in modThumbnailIcon:
        num = 0
        
        modThumbnailIconURL_list.append(url_for('static',filename='thumbnails/'+icon))
        num += 1
    
    return render_template('public/index.html',modPage = modPage , modSummary = modSummary , modThumbnailIcon = modThumbnailIconURL_list , modTitle = modTitle)

@app.route('/mod/<addonID>/')
def modPage(addonID):
    print(addonID)
    return addonID
if __name__ == "__main__":
    app.run(port=8000)