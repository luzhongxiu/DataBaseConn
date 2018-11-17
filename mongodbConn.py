from  pymongo import MongoClient
import numpy as np
from pandas import Series,DataFrame

conn=MongoClient(host='localhost',port=27017)
testdb=conn.testdb
coll=testdb.items
item={
   "type":"operation",
   "itemno":"10000",
   "contents":{
   "python":"2.7.11", 
   "spark":"2.0"
   },
   "date":"201611"
   }
coll.insert_one(item)
coll.find_one()

item1=[{'contents': {'HBase': '2.0', 'Hadoop': '2.7.0'},
  'date': '201611',
  'itemno': '20000',
  'type': 'operation'},
 {'contents': {'Jave': '1.8.0', 'Scala': '2.10.0'},
  'date': '201611',
  'itemno': '30000',
  'type': 'operation'}]
coll.insert_many(item1)
for doc in coll.find({"type":"operation"}):
    print(doc)
query1=coll.find({"type":"operation"})	 ##定义查询结果
column=['type','itemno','contents','date']	 ##定义显示列名（关键字）
df1=DataFrame(list(query1),columns=column)
print(df1)
