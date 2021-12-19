from logging import error
from flask import Flask,request,render_template,url_for

import pymongo


app = Flask (__name__)
client = pymongo.MongoClient('localhost', 27017)
db = client.uncursedforge
collection = db.modsinfo

@app.route("/")
def index():
    itemList = []
    modPage = []
    modThumbnailIcon = []
    modTitle = []
    modSummary = []
    modThumbnailIconURL_list = []
    indexPageList = []
    
    
    res = collection.aggregate([{"$sample":{"size":10}}])
    for item in res:
        modTitle.append(item['title'])
        modSummary.append(item['summary'])
        try:
            modThumbnailIcon.append(item['icon_file_name'])
        except KeyError:
            modThumbnailIcon.append('no_response.png')
        modPage.append("/mod/"+item['id'])
    for icon in modThumbnailIcon:
        num = 0
        
        modThumbnailIconURL_list.append(url_for('static',filename='thumbnails/'+icon))
        num += 1
    
    return render_template('public/index.html',modPage = modPage , modSummary = modSummary , modThumbnailIcon = modThumbnailIconURL_list , modTitle = modTitle)



@app.route('/mod/<addonID>/')
def modPage(addonID):
    infoDBRes = collection.find({"id": addonID})
    for item in infoDBRes:
        
        try:
            icon_file_name = item['icon_file_name']
        except KeyError:
            icon_file_name = 'no_response.png'
        
        modTitle = item['title']
        modDes = item['des']
    
    modIcon = url_for('static',filename='full_icons/'+icon_file_name)
    

    return render_template('public/modPage.html',modIcon = modIcon,modTitle = modTitle,modDes = modDes)

@app.errorhandler(404)
def page_unauthorized(error):
    return render_template('public/404.html'), 404


if __name__ == "__main__":
    app.run(port=8000)
    