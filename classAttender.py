###################################################################
#Change the Time when class begins and ends in the time(00,00,00) in place of the zeros
#Put your class links in the function blocks below
#according to the timetable, place the function name of whatever class you want
#Run this in A terminal or CMD shell
#Made By FoxSinOfGreed1729

import webbrowser
from datetime import date
import datetime
import calendar
import time
import os

now = datetime.datetime.now().time()
print(now)
tdate=date.today()
print(tdate)
tdate=str(tdate)
tdate=tdate.split('-')
a=int(tdate[0])
b=int(tdate[1])
c=int(tdate[2])
#print(a)
#print(b)
#print(c)
tday=calendar.weekday(a,b,c)
time1= datetime.time(00,00,00)
time2= datetime.time(00,00,00)
tday=calendar.weekday(a,b,c)
def opensched():
    if tday==0: #MONDAY
        time1= datetime.time(00,00,00) #Time When the class begins
        time2= datetime.time(00,00,00) #Time When the class ends
        if now<time2 and now>time1:
            #name of class function

        time1= datetime.time(00,00,00) #Time When the class begins
        time2= datetime.time(00,00,00) #Time When the class ends
        if now<time2 and now>time1:
            #name of class function

        time1= datetime.time(00,00,00) #Time When the class begins
        time2= datetime.time(00,00,00) #Time When the class ends
        if now<time2 and now>time1:
            #name of class function

        time1= datetime.time(00,00,00) #Time When the class begins
        time2= datetime.time(00,00,00) #Time When the class ends
        if now<time2 and now>time1:
            #name of class function
    if tday==1: #TUESDAY
        time1= datetime.time(00,00,00) #Time When the class begins
        time2= datetime.time(00,00,00) #Time When the class ends
        if now<time2 and now>time1:
            #name of class function

        time1= datetime.time(00,00,00) #Time When the class begins
        time2= datetime.time(00,00,00) #Time When the class ends
        if now<time2 and now>time1:
            #name of class function

        time1= datetime.time(00,00,00) #Time When the class begins
        time2= datetime.time(00,00,00) #Time When the class ends
        if now<time2 and now>time1:
            #name of class function

        time1= datetime.time(00,00,00) #Time When the class begins
        time2= datetime.time(00,00,00) #Time When the class ends
        if now<time2 and now>time1:
            #name of class function

    if tday==2: #WEDNESDAY
        time1= datetime.time(00,00,00) #Time When the class begins
        time2= datetime.time(00,00,00) #Time When the class ends
        if now<time2 and now>time1:
            #name of class function

        time1= datetime.time(00,00,00) #Time When the class begins
        time2= datetime.time(00,00,00) #Time When the class ends
        if now<time2 and now>time1:
            #name of class function

        time1= datetime.time(00,00,00) #Time When the class begins
        time2= datetime.time(00,00,00) #Time When the class ends
        if now<time2 and now>time1:
            #name of class function

        time1= datetime.time(00,00,00) #Time When the class begins
        time2= datetime.time(00,00,00) #Time When the class ends
        if now<time2 and now>time1:
            #name of class function

    if tday==3: #THURSDAY
        time1= datetime.time(00,00,00) #Time When the class begins
        time2= datetime.time(00,00,00) #Time When the class ends
        if now<time2 and now>time1:
            #name of class function

        time1= datetime.time(00,00,00) #Time When the class begins
        time2= datetime.time(00,00,00) #Time When the class ends
        if now<time2 and now>time1:
            #name of class function

        time1= datetime.time(00,00,00) #Time When the class begins
        time2= datetime.time(00,00,00) #Time When the class ends
        if now<time2 and now>time1:
            #name of class function

        time1= datetime.time(00,00,00) #Time When the class begins
        time2= datetime.time(00,00,00) #Time When the class ends
        if now<time2 and now>time1:
            #name of class function

    if tday==4: #FRIDAY
        time1= datetime.time(00,00,00) #Time When the class begins
        time2= datetime.time(00,00,00) #Time When the class ends
        if now<time2 and now>time1:
            #name of class function

        time1= datetime.time(00,00,00) #Time When the class begins
        time2= datetime.time(00,00,00) #Time When the class ends
        if now<time2 and now>time1:
            #name of class function

        time1= datetime.time(00,00,00) #Time When the class begins
        time2= datetime.time(00,00,00) #Time When the class ends
        if now<time2 and now>time1:
            #name of class function

        time1= datetime.time(00,00,00) #Time When the class begins
        time2= datetime.time(00,00,00) #Time When the class ends
        if now<time2 and now>time1:
#put class links in the functions
def class1():
    webbrowser.open('class1link')
def class2():
    webbrowser.open('class2link')
def class3():
    webbrowser.open('class3link')
def class4():
    webbrowser.open('class4link')
def class5():
    webbrowser.open('class5link')
def class6():
    webbrowser.open('class6link')

opensched()
