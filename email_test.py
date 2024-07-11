import ssl
import smtplib
from email.message import EmailMessage

gmail = "SENDER EMAIL"
password_gmail = "PASSWORD SENDER EMAIL" 
app_password_email_gmail = "APP PASSWORD"

getter_gmail = "GETTER EMAIL"

subject = "Test"

body = """
<!DOCTYPE html>
<html>
<body>

<p><a href="https://youtu.be/EZEfN5z8Mlg/">Look at me!</a></p>

</body>
</html>
"""

em = EmailMessage()

em["From"] = gmail 
em["To"] = getter_gmail
em["Subject"] = subject
#em.set_content(body)
em.add_alternative(body, subtype='html')

context = ssl.create_default_context()

# Log in and send the email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(gmail, app_password_email_gmail)
    #print(em.as_string())
    smtp.sendmail(gmail, getter_gmail, em.as_string())