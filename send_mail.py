import smtplib
import ssl


def send_mail_user(message):
    gmail_server = "smtp.gmail.com"
    port = 465
    user_name = "kiranjojan455@gmail.com"
    user_password = "gxvelsxemruixzsg"

    mail_receiver = "kiranjojan455@gmail.com"
    my_context = ssl.create_default_context()
    with smtplib.SMTP_SSL(gmail_server, port, context=my_context) as server:
        server.login(user_name, user_password)
        server.sendmail(user_name, mail_receiver, message)
