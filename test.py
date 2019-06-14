import json
import pyrebase
import datetime

config = {
  "apiKey": "P7Fx3FCquDlCXdauc3Z91lgdRLu7VsFtyq51RU4R",
  "authDomain": "minimartpos.firebaseapp.com",
  "databaseURL": "https://minimartpos.firebaseio.com",
  "storageBucket": "minimartpos.appspot.com"
}

# firebase = pyrebase.initialize_app(config)
# db = firebase.database()

# now = datetime.datetime.now()
# date = now.strftime("%Y-%m-%d %H:%M:%S")
# data = {
#     "cost": "5.5",
#     "date": date,
#     "price": "6.6",
#     "product_NAME": "test pp",
#     "product_NUMBER": "1212312121"
# }
# arr = []
# jsonData = {}
# dat = db.child("data").get()
# for x in dat.each():
#   tmp ={
#       x.val().get("product_NUMBER"): {
#       "cost": x.val().get("cost"),
#       "date": x.val().get("date"),
#       "price": x.val().get("price"),
#       "product_NAME": x.val().get("product_NAME"),
#       "product_NUMBER": x.val().get("product_NUMBER")
#     }
#   }
#   db.child("datas").update(tmp)
# print("success")

with open('data.json',encoding='utf8') as json_file:  
  data = json.load(json_file)
  # for x in data:
  #   for y in x:
  #     print(y)
  if "188501510951156" in data:
    print(data["18850151095115"])
  else:
    print("not a")
  # for p in data:
  #   print(type(p))
