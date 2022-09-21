from email.message import EmailMessage
import ssl
import smtplib

times = 1
#times you want to send the gmail
email_sender = 'anygmail.com'
#change the sender
email_password = ''

email_reciever = 'anygmail.com'
#change the reciever

subject = 'PLEAAAAAASEEEEE'
body = """
   Hello
"""
#message over here

email = EmailMessage()
email['From'] = email_sender
email['To'] = email_reciever
email['Subject'] = subject
email.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    for i in range(0, times):
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_reciever, email.as_string())


