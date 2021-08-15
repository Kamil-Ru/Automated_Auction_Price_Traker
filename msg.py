import smtplib
from password import EMAIL, EMAIL_PASSWORD, SECOND_ADDRESS


def send_email(price=None, text=None, url=None):
    quote = f"Text: {text}\nPrice: {price}\nURL: {url}"

    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=SECOND_ADDRESS,
            msg=f"Subject: GeForce 3070 Ti Alert\n\n{quote}")
