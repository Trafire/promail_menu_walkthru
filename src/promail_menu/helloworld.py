# src/promail_menu/helloworld.py
"""Hello World Example for sending and recieving emails"""
import time

from promail.clients import GmailClient
from promail_template.templates.full import HelloWorld

# constants
MENU_EMAIL = "promail.tests@gmail.com"
AUTHORIZED_EMAILS = ("antoinewood@gmail.com",)

# set up client
client = GmailClient(MENU_EMAIL, credentials="../.credentials/gmail_credentials.json")


@client.register(name="helloworld", subject="Hello Promail", sender=(AUTHORIZED_EMAILS,))
def reply_hello(email):
    template = HelloWorld({"name": "Antoine"})
    client.send_email(
        recipients=email.sender,
        subject="Hello World",
        htmltext=template.html,
        plaintext=template.plaintext,
    )


while True:
    client.process()
    time.sleep(1)
