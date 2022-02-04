
from getpass import getpass
import smtplib as sm 
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os.path import basename
from email.mime.application import MIMEApplication

# Before using the bot you have to lower the security in your email - Desctivate 2FA and Activate less secure
# Copy your mails receiver in emails text file 
# Past your email content text to Mail Content Text File
def sendMail(password,sender,receiver,filePath,mailContent,mailSubject):
    mail_content = mailContent
    
    sender_address = sender
    sender_pass = Password
    receiver_address = receiver
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = mailSubject
    #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain')) 
    file = filePath
    with open(file, "rb") as fil:
        part = MIMEApplication(
            fil.read(),
            Name=basename(file)
            )
        # After the file is closed
    part['Content-Disposition'] = 'attachment; filename="%s"' % basename(file)
    message.attach(part)

    #Create SMTP session for sending the mail
    session = sm.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent to : '+ receiver_address)


# Read List of Mails and Mail Content
with open('emails.txt',) as f:
    lines = f.readlines()
mails = "".join(lines).replace("\n","+").split("+")

with open('MailContent.txt',encoding='utf8') as f:
     Content = f.read()


# Define the mail content object and file : 
Subject = input("Email Subject : ")
Sender = input("Your Email : ")
Password = getpass("Email Password : ")
filePath = input("File to send  : (Example C:/file.pdf) ")



# Send Mails
for mail in mails:
    sendMail(Password,Sender,mail,filePath,Content,Subject)
    time.sleep(5)





