from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
import random
from datetime import datetime
import json

app=FastAPI()

origins=["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

class details(BaseModel):
    student_name: str
    age: int
    srn: str
    comments:str

@app.get("/")
def first():
    return "Welcome to our first app"

@app.get('/hello')
def basic():
    return 'hello world'

@app.get('/date')
def return_date():
    dateTimeObj = datetime.now()
    return 'date '+str(dateTimeObj.year)+'/'+str(dateTimeObj.month)+'/'+str(dateTimeObj.day)+'     '+\
    ' time '+str(dateTimeObj.hour)+':'+str(dateTimeObj.minute)+':'+str(dateTimeObj.second)


@app.post('/details')
def det(det:details):
    enc=jsonable_encoder(det)
    s_name=enc['student_name']
    age=enc['age']
    srn=enc['srn']
    com=enc['comments']
    d={
        "student_name":s_name,
        "age":age,
        "srn":srn,
        "comments":com
    }
    print("i m in")
    f=open("docx.txt",'a')
    #f=open('D:/Downloads/details.txt','a')
    f.write(f'{s_name},{str(age)},{srn}, {com} \n')
    f.close

    with open('D:/Downloads/funfacts.txt') as f:
        lines = f.readlines()
        a=(random.choice(lines).strip())

    return 'hello '+s_name+' you are '+str(age)+f' old, and your data has been noted,\
     Did you know:- {a}'

@app.get('/data/{dig}')
def data(dig):
    f=open('docx.txt','r')
    rea=f.readlines()
    count= 0
    a=[]
    for i in rea:
        a.append(i.split(','))
        if dig in a[count][0]:
            return a[count]
        else:
            count+=1

