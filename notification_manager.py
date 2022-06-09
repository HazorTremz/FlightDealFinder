import os
from twilio.rest import Client
from smtplib import SMTP

AUTH_TOKEN = os.environ.get("AUTH_T1")
AUTH_SID = os.environ.get("AUTH_S1")
from_number = os.environ.get("FRM_NO")
my_number = os.environ.get("TO_NO")
my_mail = os.environ.get("MAIL")
password = os.environ.get("PASS")


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def send_message(self, price, from_, from_iata, to_, to_iata, date_f, date_t):
        client = Client(AUTH_SID, AUTH_TOKEN)
        message = client.messages \
            .create(
            body=f"Low price alert! Only {price} to fly from {from_}-{from_iata} to {to_}-{to_iata},"
                 f"from {date_f} to {date_t}",
            from_=from_number,
            to=my_number,
        )
        print(message.status)

    def send_email(self, price, from_, from_iata, to_, to_iata, date_f, date_t,mail):
        with SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_mail, password=password)
            connection.sendmail(
                from_addr=my_mail,
                to_addrs=mail,
                msg=f"Subject:New Low Price Flight!\n\nLow price alert! only £{price} to fly"
                    f" from{from_}-{from_iata} to {to_}-{to_iata},from {date_f} to {date_t}\n"
                    f"https://www.google.co.uk/flights?hl=en#flt="
                    f"{from_iata}.{to_iata}.{date_f}*{to_iata}.{from_iata}.{date_t}".encode('utf-8'))
