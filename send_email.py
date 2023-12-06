import os
import ssl
if os.path.isfile("env.py"):
    import env
import smtplib


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = os.environ.get("USERNAME")
    password = os.environ.get("PASSWORD")

    receiver = username

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


