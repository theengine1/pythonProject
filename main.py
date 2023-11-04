import yagmail
import datetime
import os
import time

sender = 'alabivgoro3@Gmail.com'
receiver = 'victoralabi03@gmail.com'
subject = 'This is a test project'
content = "Thanks for subscribing to our youtube channel!"
while True:
    currenttime = datetime.datetime.now()
    if currenttime.hour == 19 and currenttime.minute == 26:
        yag = yagmail.SMTP(user=sender, password=os.getenv('Password'))
        yag.send(to=receiver, subject=subject, contents=content)
        print("Email sent!")
        time.sleep(30)
