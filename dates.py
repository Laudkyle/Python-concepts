import datetime 

print(datetime.datetime.now())
print(datetime.datetime.now().date().strftime("%d-%m-%y"))
print(datetime.datetime.now().time())
print(datetime.datetime.now().time().strftime("%H : %M : %S"))

