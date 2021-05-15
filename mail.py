import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

subject = "An email with attachment from Python"
body = "This is an email with attachment sent from Python"
sender_email = "anujojo181215@gmail.com"
receiver_email = "anujojo181215@gmail.com"
password = "An181215*"


message = MIMEMultipart()
message["From"] = "anujojo181215@gmail.com"
message["To"] = "anujojo181215@gmail.com"
message["Subject"] =" Minor Project!!!"
message["Bcc"] = ""  


message.attach(MIMEText(body, "plain"))

filename = "/home/anu/Desktop/file.log"  


with open(filename, "rb") as attachment:


    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())


encoders.encode_base64(part)

part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

message.attach(part)
text = message.as_string()

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)
