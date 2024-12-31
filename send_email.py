import smtplib
import os

# creates SMTP session
s = smtplib.SMTP('smtp.protonmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
# Use an App Password stored in an environment variable for security
email_password = os.getenv('PROTONMAIL_APP_PASSWORD')
s.login("aromanos@gmail.com", email_password)

# message to be sent
message = "Message_you_need_to_send"

# sending the mail
s.sendmail("sender_email_id", "receiver_email_id", message)

# terminating the session
s.quit()