import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def senddetails(arg1,arg2,arg3):
    fromaddr = "pavankalyan.d16@gmail.com"
    toaddr = "pavankalyan.d16@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = arg1+','+arg2+','+arg3
    body = "Message from Control Center"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "SUrya5412417")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()