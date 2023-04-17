import os

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

class MorningMail(Mail):
    def __init__(self, to_emails=None, subject=None, html_content=None):
        from_email = "liuydt@hotmail.com"
        if subject is None:
            subject = "Morning Greeting"
        super().__init__(from_email = from_email, to_emails = to_emails, subject = subject, html_content=html_content)

    def sendMorningMail(self):
        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(self)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e.message)

