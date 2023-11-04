import csv

import pandas
import yagmail
import datetime
import os
import time


df = pandas.read_csv(r"C:\Users\victoralabi\Desktop\EmailAddress.txt")
sender = 'alabivgoro3@Gmail.com'
subject = 'This is a test project'
yag = yagmail.SMTP(user=sender, password=os.getenv('Password'))
for index, row in df.iterrows():
    receiver = row['EmailAddress']
    content = "Hi, ", row['Name'], "Thanks for subscribing to our youtube channel!"
    yag.send(to=receiver, subject=subject, contents=content)

#while True:
    #currenttime = datetime.datetime.now()
    #if currenttime.hour == 19 and currenttime.minute == 26:
       # yag = yagmail.SMTP(user=sender, password=os.getenv('Password'))
       # yag.send(to=receiver, subject=subject, contents=content)
       # print("Email sent!")
       # time.sleep(30)
