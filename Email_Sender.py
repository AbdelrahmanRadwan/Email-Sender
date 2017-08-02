import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

#fromaddr = "YOUR ADDRESS"
fromaddr = "From"
#toaddr = "ADDRESS YOU WANT TO SEND TO"
toaddr = "To"

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "The subject here"

body = ""
msg.attach(MIMEText(body, 'plain'))
#Details about your server, if it's Gmail, don't change it
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "Your Password")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()