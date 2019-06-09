import smtplib
import datetime
from email.mime.text import MIMEText
import tools
import io

MAIL_USERNAME = 'care@oyacharge.com'
MAIL_PASSWORD = '2ca44ef0-9dc2-4b11-803b-9b1001848d39'
MAIL_SENDER = 'Abhishek.ricky88@gmail.com'


def send_email(mail_id):
    # SMTP settings
    sender = MAIL_SENDER
    username = MAIL_USERNAME
    password = MAIL_PASSWORD
    # Prepare email's message
    # Date of the event
    date = datetime.datetime.now()
    SUBJECT = "Hybrid Cryptography Decryption Key %s" % date.strftime('%d %b %Y %H:%M:%S')
    msg = """
    Dear User, 
    Kindly keep the file very safe in order to retrieve your secret file. 
    From our platform.      
    """

    TO = mail_id
    FROM = sender
    msg = MIMEText(msg)
    msg['Subject'] = SUBJECT
    msg['To'] = TO
    msg['From'] = FROM

    # Login to SMTP server
    server = smtplib.SMTP('smtp.elasticemail.com:2525')
    server.ehlo()
    server.starttls()
    server.login(username, password)

    # Sending file as attachments.
    list_directory = tools.list_dir('key')
    filename = './key/' + list_directory[0]
    attachment_filename = filename
    msg.attach(attachment_filename)

    # Send email to receivers
    server.sendmail(FROM, mail_id, msg.as_string())
    # Close connection with SMTP server
    server.quit()

