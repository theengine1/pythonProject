import yagmail
import datetime
import time
import os

sender = 'alabivgoro3@Gmail.com'
receiver = 'victoralabi03@gmail.com'
subject = 'This is a test project'
date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
content = "This message was sent at ", date
yag = yagmail.SMTP(user=sender, password=os.getenv('Password'))

while True:
    yag.send(to=receiver, subject=subject, contents=content)
    print("Email sent!")
    time.sleep(30)


