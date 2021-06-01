import smtplib
from email.mime.text import MIMEText

body = "This is a test email. How are you"
msg = MIMEText(body)
msg['From'] = "brunomilitzer.work@gmail.com"
msg['To'] = "brunomilitzer.work@gmail.com"
msg['Subject'] = "Hello"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("brunomilitzer.work@gmail.com", "")
server.send_message(msg)

print("Main sent")

server.quit()
