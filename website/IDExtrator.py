import json

new_mod_count = 0
originalIDList = []
with open('manifest.json') as manifestFile:
    manifestJson = json.load(manifestFile)
with open('ids_autoFilled.txt') as originalIDFile:
    fileReadLines = originalIDFile.readlines()
    for id in fileReadLines:
        originalIDList.append(id)
print(len(originalIDList))

print(originalIDList)
for item in manifestJson["files"]:
    
    if (str(item['projectID']) in originalIDList )== False:
        print("新增"+ str(item['projectID']))
        originalIDList.append(str(item['projectID'])+'\n')

    else:
        print("无新增")
    
with open('ids_autoFilled.txt','w+') as after_completed_file:
    formatList = list(set(originalIDList))
    formatList.sort(key=originalIDList.index)
    after_completed_file.writelines(formatList)
    print(len(formatList))