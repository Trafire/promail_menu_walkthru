# src/promail_menu/meal_suggestions.py
"""Meal Recommendations"""
from promail.clients import GmailClient
from promail_template.templates.full import ImageDescriptionTemplate

# constants
MENU_EMAIL = "promail.tests@gmail.com"
AUTHORIZED_EMAILS = ("my_email@example.com", "someone_else@example.com")

# set up client
client = GmailClient(MENU_EMAIL, credentials="../.credentials/gmail_credentials.json")

template = HelloWorld({"name": "Antoine"})

client.send_email(
    recipients="my_email@example.com",
    subject="Hello from Promail",
    htmltext=template.html,
    plaintext=template.plaintext
)