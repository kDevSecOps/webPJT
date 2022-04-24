# 11. mongoDB 연결하기
# 1) mongoDB - Atlas 연결하기

# 3) pymongo로 조작하기

from pymongo import MongoClient
client = MongoClient(
    'mongodb+srv://mgDBusr:<password>@cluster0.bllxi.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = client.dbsparta

# raise ConfigurationError(
# pymongo.errors.ConfigurationError: The "dnspython" module must be installed to
# use mongodb+srv:// URIs. To fix this error install pymongo with the srv extra:


doc = {
    'name': 'bob',
    'age': 27
}

db.users.insert_one(doc)

# pymongo로 DB조작하기
# 1) pymongo로 mongoDB 조작하기

# 'users'라는 collection에 {'name':'bobby','age':21}를 넣습니다.
db.users.insert_one({'name':'bobby','age':21})
db.users.insert_one({'name':'kay','age':27})
db.users.insert_one({'name':'john','age':30})

# pymongo(find)
same_ages = list(db.users.find({},{'_id':False}))

# 모든 데이터 뽑아보기
all_users = list(db.users.find({},{'_id':False}))

print("0th item: ",all_users[0])         # 0번째 결과값을 보기
print("Name of 0th item: ",all_users[0]['name']) # 0번째 결과값의 'name'을 보기

for user in all_users:      # 반복문을 돌며 모든 결과값을 보기
    print(user)

