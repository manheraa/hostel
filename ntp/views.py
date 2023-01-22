from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector as sql
from django.contrib.messages import constants as messages
from django.contrib import messages
import hashlib
from datetime import date
# Create your views here.
userid=""
username=""
password=""
Email=""
student_id=""
passwd=""
fname=""
lname=""
phone=""
sex=""
age=""
course=""
address=""
messy=0
fees=0
mess_validity=""
arrival=""
departure=""
booked="NONE"
bulding_id="NONE"
room_id="NONE"
x=""
y=""
def add_years(start_date, years):
    try:
        return start_date.replace(year=start_date.year + years)
    except ValueError:
        #  preseve calendar day (if Feb 29th doesn't exist, set to 28th)
        return start_date.replace(year=start_date.year + years, day=28)

def applymess(request):
    global Email,passwd, userid ,username,password,student_id,fname,lname,phone,sex,age,course,address,messy,fees
    std_id=student_id
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="sssachetar1234@",database="manu")
        cursor=m.cursor()
        
        d=request.POST
        for k,v in d.items():
            
            if(k=="exampleRadios1"):
                messy=int(v)
                fees=3000
            if(k=="exampleRadios6"):
                messy=int(v)
                fees=18000
            if(k=="exampleRadios12"):
                messy=int(v)
                fees=36000
        c="select mess_validity from fees where student_id='{}'".format(std_id)
    cursor.execute(c)
    t=cursor.fetchall()
    print(t)
    
    if t==[(None,)]:
        c="update fees set mess_fees=%s,mess_validity=%s where student_id=%s"
        l=[fees,messy,std_id]
        
        cursor.execute(c,l)
        if(sex=="male"):
            c="insert into mess(student_id,bulding_id) values(%s,'01')"
        else:
            c="insert into mess(student_id,bulding_id) values(%s,'02')"
        l=[std_id]
        cursor.execute(c,l)
        m.commit()
    
        messages.success(request,"you mess validity is {} months .You can check in mydetails".format(messy))
        
        return render(request,"login.html")

    else:
        messages.error(request,"You have already registered.You can check in mydetails")
        return render(request,"login.html")
    
def gobackuser(request):
    global Email,passwd, userid ,username,password,student_id,fname,lname,phone,sex,age,course,address
    return render(request,"user.html",{"email":Email,"password":passwd,"student_id":student_id,"fname":fname,"lname":lname,"phone":phone,"sex":sex,"age":age,"address":address,"course":course})
def mess(request):
    return render(request,"mess.html")
def jamun(request):
    return render(request,'login.html')
def home(request):
    return render(request,"user.html")

def register(request):
    return render(request,'register.html')
def login(request):
    
    global Email,passwd, userid ,username,password,student_id,fname,lname,phone,sex,age,course,address,booked,room_id,mess_validity,arrival,departure,bulding_id
   
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="sssachetar1234@",database="manu")
        cursor=m.cursor()
        
        d=request.POST
        print(d)
        
        for key,value in d.items():
            
            if(key=="Email"):
                Email=value
            
            if(key=="password"):
                passwd=value
    x=hashlib.sha224(passwd.encode())
    passwd=x.hexdigest()
    x=Email
    y=passwd
    c="select * from student where Email='{}' and passwd='{}'".format(x,y)
    cursor.execute(c)
    t=cursor.fetchall()
    
    
    
    if t==():
            return HttpResponse("ERROR")
    else:
        
        messages.success(request,"WELCOME TO HOSTEL")
        Email,passwd,student_id,fname,lname,phone,sex,age,address,course=t[0]
        c="select student_id,room_id from booked where student_id='{}'".format(student_id)
        cursor.execute(c)
        f=cursor.fetchall()
        print(f)
        if(f==[]):
            pass
        else:
            booked,room_id=f[0]
        c="select mess_validity,arrival_date,departure_date from fees where student_id='{}'".format(student_id)
        cursor.execute(c)
        f=cursor.fetchall()
        print(f)
        if(f==[]):
            pass
        else:
            mess_validity,arrival,departure=f[0]
        c="select bulding_id from bulding where room_id='{}'".format(room_id)
        cursor.execute(c)
        f=cursor.fetchall()
        if(f==[]):
            pass
        else:
            bulding_id=f[0]
        
        
        return render(request,"user.html",{"email":Email,"password":passwd,"student_id":student_id,"fname":fname,"lname":lname,"phone":phone,"sex":sex,"age":age,"address":address,"course":course,"arrival":arrival,"departure":departure})
    
    
def registering(request):
     global Email,passwd,student_id,fname,lname,phone,sex,age,address,course
   
     if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="sssachetar1234@",database="manu")
        cursor=m.cursor()
        
        d=request.POST
        
        for key,value in d.items():
            
            if(key=="email"):
                Email=value
            if(key=='studentid'):
                student_id=value
            if(key=="password"):
                passwd=value
            if(key=='fname'):
                 fname=value
            if(key=="lname"):
                lname=value
            if(key=="phonenumber"):
                phone=value
            if(key=="sex"):
                sex=value     
            if(key=="age"):
                age=value
            if(key=="address"):
                address=value
            if(key=="course"):
                course=value
        
        age=int(age)
        x=hashlib.sha224(passwd.encode())
        passwd=x.hexdigest()
        c="INSERT INTO student(Email,passwd,student_id,fname,lname,phone,sex,age,address,course)""VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        b1=(Email,passwd,student_id,fname,lname,phone,sex,age,address,course)
        cursor.execute(c,b1)
        
        x="insert into fees(student_id) values(%s)"
        l=[student_id]
        cursor.execute(x,l)
        m.commit()
        messages.success(request,"your input have been taken!")
        
        
        return render(request,"register.html")

def bookroom(request):
     global Email,passwd,student_id,fname,lname,phone,sex,age,course,address
     return render(request,"bookroom.html")
def booked(request):
    global Email,passwd,student_id,fname,lname,phone,sex,age,course,address,x,y
    Emailz,passwdz,student_idz,fnamez,lnamez,phonez,sexz,agez,coursez,addressz,xz,yz=Email,passwd,student_id,fname,lname,phone,sex,age,course,address,x,y
    return render(request,"confirm.html",{"email":Email,"password":passwd,"student_id":student_id,"fname":fname,"lname":lname,"phone":phone,"sex":sex,"age":age,"course":course,"address":address})
def confirmbooking(request):
    global Email,passwd, userid ,username,password,student_id,fname,lname,phone,sex,age,course,address,x,y,booked,room_id 
    
    x=date.today()
    z=add_years(x,1)
    db=sql.connect(host="localhost",passwd="sssachetar1234@",user="root",database="manu")
    cnx=db.cursor()

    if(booked==student_id): 
            messages.error(request,"Your room is already booked check my details")
            return render(request,"login.html")
    else:
        if(sex=="male"): 
         c="select sum(no_of_students) from rooms where gender='M'"
         cnx.execute(c)
         t=cnx.fetchall()
         num,=t[0]
         if(num<40 and t!=[(None,)]):
             c="select ROOM_ID,no_of_students from rooms where gender='M' and no_of_students<4 limit 1"
             cnx.execute(c)
             t=cnx.fetchall()
             room,no=t[0]
             if(no<4):
                 c="insert into booked(student_id,room_id) values(%s,%s)"
                 l=[student_id,room]
                 cnx.execute(c,l)
                 print(room)
                 c="update bulding set no_of_students=no_of_students+1  where room_id='{}'".format(room)
                 cnx.execute(c)
                 c="update rooms set no_of_students=no_of_students+1 where ROOM_ID='{}'".format(room)
                 cnx.execute(c)

                 c="update fees set room_fees='{}',arrival_date='{}',departure_date='{}' where student_id='{}'".format(36000,x,z,student_id)
                 cnx.execute(c)
                 db.commit()
                 messages.error(request,"You have successfully booked the room")
                 return render(request,"login.html")
        if(sex=="female"): 
         c="select sum(no_of_students) from rooms where gender='F'"
         cnx.execute(c)
         t=cnx.fetchall()
         num,=t[0]
         if(num<40 and t!=[(None,)]):
             c="select ROOM_ID,no_of_students from rooms where gender='F' and no_of_students<4 limit 1"
             cnx.execute(c)
             t=cnx.fetchall()
             room,no=t[0]
             if(no<4):
                 c="insert into booked(student_id,room_id) values(%s,%s)"
                 l=[student_id,room]
                 cnx.execute(c,l)
                 print(room)
                 c="update bulding set no_of_students=no_of_students+1  where room_id='{}'".format(room)
                 cnx.execute(c)
                 c="update rooms set no_of_students=no_of_students+1 where ROOM_ID='{}'".format(room)
                 cnx.execute(c)

                 c="update fees set room_fees='{}',arrival_date='{}',departure_date='{}' where student_id='{}'".format(36000,x,z,student_id)
                 cnx.execute(c)
                 db.commit()
                 messages.error(request,"You have successfully booked the room")
                 return render(request,"login.html")
def mydetails(request):
    global Email,passwd, userid ,username,password,student_id,fname,lname,phone,sex,age,course,address,room_id,arrival,departure,mess_validity,bulding_id
    
    
    arrival=str(arrival)
    departure=str(departure)
    
    return render(request,"mydetails.html",{"email":Email,"student_id":student_id,"fname":fname,"lname":lname,"phone":phone,"sex":sex,"age":age,"address":address,"course":course,"arrival":arrival,"departure":departure,"room_id":room_id,"mess_validity":mess_validity,"bulding_id":bulding_id[0]})