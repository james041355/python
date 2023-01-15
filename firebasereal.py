# 引用必要套件
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import db


# 引用私密金鑰
# path/to/serviceAccount.json 請用自己存放的路徑
cred = credentials.Certificate('/pythontest-64730-firebase-adminsdk-kywz2-4580bb3d0d.json')

# 初始化firebase，注意不能重複初始化
firebase_admin.initialize_app(cred,{
	'databaseURL':'https://pythontest-64730-default-rtdb.firebaseio.com'})


def readdate(dateset):#讀取
    ref=db.reference(dateset)
    print(ref.get())                 

def update(dateset,datenames,date):##建立 位置/檔名/資料
    ref=db.reference(dateset)
    ref.update({datenames:date})

def deldate(dateset):#刪除位置
    ref=db.reference(dateset)
    ref.set({})





ref=db.reference('/')
#ref.set({'kk':5678})##建立
#ref.push({'/test/ui':1234})
ref.update({'kk':129957678})#修改
ref=db.reference('/kk')
print(ref.get())#讀取
#ref.push({'ui':1234})

ref=db.reference('/')

ref.update({'kk6622':1222995780000})
ref=db.reference('/kk6622')

readdate('/test2/james')

update('/test2','ewan',660421)
update('/test2','vivian',891126)

update('/test3','gary',910317)
update('/test3','ga',17)
update('/test3','ry',9103)


deldate('/test3/ry')

readdate('/kk6622')

