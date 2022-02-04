
from getpass import getpass
import smtplib as sm 
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os.path import basename
from email.mime.application import MIMEApplication

# Before using the bot you have to lower the security in your email - Desctivate 2FA and Activate less secure
# Copy your mails receiver in emails text file 

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




with open('emails.txt') as f:
    lines = f.readlines()
mails = "".join(lines).replace("\n","+").split("+")



# Define the mail content object and file : 
Content = ''' Copy the Content Here '''
Subject = "Subject Here"
Sender = input("Your Email : ")
Password = getpass("Email Password : ")
filePath = "path"




for mail in mails:
    sendMail(Password,Sender,mail,filePath,Content,Subject)
    time.sleep(5)





