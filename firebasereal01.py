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
    #print(ref.get())                 
    return(ref.get())

def update(dateset,datenames,date):##建立 位置/檔名/資料/
    ref=db.reference(dateset)
    ref.update({datenames:date})

def deldate(dateset):#刪除位置
    ref=db.reference(dateset)
    ref.set({})

temp=[1,2,3,4,5,6,7,8,9]
Atemp=[]
total=0


#update('/temp','use1',temp)


Atemp=readdate('temp/use1')

for i in range(len(Atemp)):
    total=total+int(Atemp[i])

print(total)













    

