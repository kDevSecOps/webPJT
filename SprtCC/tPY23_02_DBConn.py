# 11. mongoDB 연결하기
# 1) mongoDB - Atlas 연결하기

# 3) pymongo로 조작하기

from pymongo import MongoClient
client = MongoClient('mongodb+srv://mgDBusr:<password>@cluster0.bllxi.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = client.dbsparta

# raise ConfigurationError(
# pymongo.errors.ConfigurationError: The "dnspython" module must be installed to 
# use mongodb+srv:// URIs. To fix this error install pymongo with the srv extra: