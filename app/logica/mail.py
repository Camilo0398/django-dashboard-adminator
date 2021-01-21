import smtplib  
import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def enviarmail(RECIPIENT,SUBJECT,BODY_HTML):

    SENDER = 'noreply@teella.com'  
    SENDERNAME = 'teella'
    USERNAME_SMTP = "AKIARP6D4SYX6T6UBOYA"
    PASSWORD_SMTP = "BITtvNUZ+LBQi9UBCC3A0jZ/KTbiKohZcWIYw7dDIbQJ"
    HOST = "email-smtp.us-east-1.amazonaws.com"
    PORT = 587
    msg = MIMEMultipart('alternative')
    msg['Subject'] = SUBJECT
    msg['From'] = email.utils.formataddr((SENDERNAME, SENDER))
    msg['To'] = RECIPIENT
    part2 = MIMEText(BODY_HTML, 'html')
    msg.attach(part2)
    try:  
        server = smtplib.SMTP(HOST, PORT)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(USERNAME_SMTP, PASSWORD_SMTP)
        server.sendmail(SENDER, RECIPIENT, msg.as_string())
        server.close()
    except Exception as e:
        print ("Error: ", e)
    else:
        print ("Email sent!")