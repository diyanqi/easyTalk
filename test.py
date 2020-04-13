import TobyDB,transaction
db=TobyDB.MyZODB('dat.db')
db.dbroot['listname']=[]
db.dbroot['listtext']=[]
transaction.commit()
db.close()