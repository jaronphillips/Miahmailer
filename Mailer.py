import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Files to use
Addresses="Addresses.txt"
Message="Message.txt"

#smtp user settings
user='username@gmail.com'
passwd='password1234!'
serverandport='smtp.gmail.com:587'

#open Files
Addresses=open(Addresses, "r")
Addresses=Addresses.read().splitlines()

Message=open(Message, "r")
Message=Message.read()

#Email Function
def send_mail(EmailAddress,Message):
    server = smtplib.SMTP(serverandport)
    from_addr = user
    to_addr = EmailAddress
    text = Message

    msg = MIMEMultipart()

    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = 'Outage'
    msg.attach(MIMEText(text))

    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(user,passwd)
    server.sendmail(from_addr,to_addr,msg.as_string())
    server.quit()

#Main Script
for EmailAddress in Addresses:
    send_mail(EmailAddress,Message)


