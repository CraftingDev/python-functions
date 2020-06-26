#!/usr/bin/env python3
import os.path
import mimetypes
import smtplib
import getpass

from email.message import EmailMessage

message = EmailMessage()
sender = "profengbrazil@gmail.com"
recipient = "prof.morten@hotmail.com"
message['From'] = sender
message['recipient'] = recipient
message['Subject'] = 'Greetings from {} to {}!'.format(sender, recipient)
message.set_content("Hello i am the body of the email")

# attachment_path = "C:/Users/User/Desktop/folder/1.jpg"
# attachment_filename = os.path.basename(attachment_path)
# mime_type, _ = mimetypes.guess_type(attachment_path)
# mime_type, mime_subtype = mime_type.split('/', 1)

mail_server = smtplib.SMTP('smtp.gmail.com', 587)
# mail_server = smtplib.SMTP('localhost', 25)
mail_pass = getpass.getpass('Professor1976')

# with open(attachment_path, 'rb') as ap:
# 	message.add_attachment(ap.read(),
# 												 maintype=mime_type,
# 												 subtype=mime_subtype,
# 												 filename=os.path.basename(attachment_path))

try:
	mail_server.ehlo()  # Can be omitted
	mail_server.starttls()  # Secure the connection
	mail_server.login(sender, mail_pass)
	mail_server.sendmail(sender, recipient, message)
except Exception as e:
	# Print any error messages to stdout
	print(e)
finally:
	mail_server.close()

# print(mime_type)
# print(mime_subtype)
# print(message)
# print(mail_pass)
