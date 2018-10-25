#Python3
import sys,requests,os
import sendgrid
from sendgrid.helpers.mail import *


mobile_list=['1234567890']
emails = ['test@perpule.com','test2@perpule.com']


sendGridclient = sendgrid.SendGridAPIClient(apikey="key")



def send_email(emails,subject, msg):
    from_email = Email("eodfeed@perpule.com")
    content = Content("text/plain", msg)
    for user in emails:
        to_email = Email(user)
        mail = Mail(from_email, subject, to_email, content)
        response = sendGridclient.client.mail.send.post(request_body=mail.get())
        print(response)


def send_sms(message):
    auth = 'qwerdsg'
    mobileStr = ','.join(mobile_list)
    request = 'http://api.msg91.com/api/sendhttp.php?authkey=' + auth + '&mobiles=' + mobileStr + '&message=' + message + '&sender=TEST&route=4&country=91'
    print("requesting: " + request)

