# -*- encoding: utf-8 -*-

import smtplib
from password import EMAIL, EMAIL_PASSWORD, SECOND_ADDRESS, ACCOUNT_SID, AUTH_TOKEN
from email.mime.text import MIMEText
from email.header import Header
from twilio.rest import Client


def send_email(price=None, text=None, url=None):
    assunto = f"Subject: GeForce 3070 Ti Alert"
    texto = f"Text: {text}\nPrice: {price}\nURL: {url}"

    corpo = MIMEText(texto, 'plain', 'utf-8')
    corpo['From'] = EMAIL
    corpo['To'] = SECOND_ADDRESS
    corpo['Subject'] = Header(assunto, 'utf-8')

    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=SECOND_ADDRESS,
            msg=corpo.as_string())

def send_SMS(price=None):
    account_sid = ACCOUNT_SID
    auth_token = AUTH_TOKEN

    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=f"Ther is GeForce for {price} zł. Check email.",
        from_='+15095712532',
        to='+48603480991'
    )
    print(message.status)





#    servidor = smtplib.SMTP()
#    servidor.connect("smtp.mail.yahoo.com")
#    servidor.login(EMAIL, EMAIL_PASSWORD)
#
#    assunto = f"Subject: GeForce 3070 Ti Alert"
#
#    para = f"GeForce 3070 Ti Alert"
#    texto = f"Text: {text}\nPrice: {price}\nURL: {url}"
#
#    corpo = MIMEText(texto, 'plain', 'utf-8')
#    corpo['From'] = EMAIL
#    corpo['To'] = SECOND_ADDRESS
#    corpo['Subject'] = Header(assunto, 'utf-8')
#
#    servidor.sendmail(EMAIL, [para], corpo.as_string())
