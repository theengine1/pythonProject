import yagmail
import os

sender = 'alabivgoro3@Gmail.com'
receiver = 'victoralabi03@gmail.com'
subject = 'This is a test project'
content = "Here is a test content for the automated email using python"

yag = yagmail.SMTP(user=sender, password=os.getenv('Password'))
yag.send(to=receiver, subject=subject, contents=content)

print("Email sent!")

