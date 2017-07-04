#coding = UTF-8
import pymongo
from pymongo import MongoClient
from gridfs import GridFS
from fileinput import filename
def createDB():
    client = MongoClient('localhost',27017)
    db =  client['file_db']
    file_table  = db['file_table']
    return (db,file_table)

def insertFile(db,table,filePath,fileName):
    fs = GridFS(db,'fileDepot')
    with open(filePath,'rb') as fileObj:
        data = fileObj.read()
        id = fs.put(data,filename = fileName)
        print(id) 
        fileObj.close()
        


# insertFile(db, fileTble, 'd:/48f31677a696329d6765cb6c77e8e799.mkv','temp1.mkv')

def delFile(db ,fileTable):
    fs = GridFS(db,'fileDepot')
    cursors =  fs.find()
    for cur in cursors:
        print(cur)
        
# delFile(db,fileTable)       

# path = 'D:/装机软件\办公软件/W.P.S.5559.60.1933.exe'
# fileName = path.split('/')[-1]
# print(fileName)
def  getFileName(filePath):
    return filePath.split('/')[-1]

db , fileTable = createDB()
filePath =  'D:/音乐/《草原》.mp3'
insertFile(db, fileTable,filePath,getFileName(filePath))