import smtplib
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
#import tools
import io

MAIL_USERNAME = 'care@oyacharge.com'
MAIL_PASSWORD = '2ca44ef0-9dc2-4b11-803b-9b1001848d39'
MAIL_SENDER = 'hello@kumarabhi.com'


def send_email(mail_id):
    # SMTP settings
    sender = MAIL_SENDER
    username = MAIL_USERNAME
    password = MAIL_PASSWORD
    # Prepare email's message
    # Date of the event
    date = datetime.datetime.now()
    SUBJECT = "Hybrid Cryptography Decryption Key %s" % date.strftime(
        '%d %b %Y %H:%M:%S')
    body = """
<p><strong><em>Dear Viewer, </em></strong><br /><em>Thanks for testing the Python Hybrid Cryptography Application. </em></p>
<p><em>Your file is uploaded safely on our platform, and it can only </em>be access<em> through the hybrid key file(attached with the mail).</em></p>
<p><em>Be </em>Rememeber<em> you can only able to get your file with the help of this <span style="text-decoration: underline; color: #000080;">hybrid_cryptography.pem</span> file, so keep this file safe and limited to you only. </em></p>
<p><em>Thanks for </em>suing<em> our platform. </em></p>
<p><strong><em>Best Regards,</em></strong><br /><strong><em>Abhishek Kumar</em></strong></p>
    """

    TO = mail_id
    FROM = sender
    # instance of MIMEMultipart
    msg = MIMEMultipart()
    msg['Subject'] = SUBJECT
    msg['To'] = TO
    msg['From'] = FROM

    msg.attach(MIMEText(body, 'html'))

    # Sending file as attachments.
    filename = "hybrid_cryptography.pem"
    attachment = open("./key/hybrid_cryptography.pem", "rb")
    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')
    # To change the payload into encoded form
    p.set_payload((attachment).read())
    # encode into base64
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    # attach the instance 'p' to instance 'msg'
    msg.attach(p)

    # Login to SMTP server
    server = smtplib.SMTP('smtp.elasticemail.com', 587)
    server.starttls()
    server.login(username, password)

    # attachment_filename = "REDBUS-AJAB_.pdf"
    # msg.attach(attachment_filename)
    # Converts the Multipart msg into a string
    text = msg.as_string()
    # Send email to receivers
    server.sendmail(FROM, mail_id, text)
    # Close connection with SMTP server
    server.quit()
