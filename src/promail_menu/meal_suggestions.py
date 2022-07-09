# src/promail_menu/meal_suggestions.py
"""Meal Recommendations"""
from promail.clients import GmailClient
from promail_template.template import PromailTemplate
from promail_template.templates.full import ImageDescriptionTemplate
from promail_template.templates.full import HelloWorld

# constants
from src.promail_menu.recipes import Api

MENU_EMAIL = "promail.tests@gmail.com"
AUTHORIZED_EMAILS = ("my_email@example.com", "someone_else@example.com")

# set up client
client = GmailClient(MENU_EMAIL, credentials="../.credentials/gmail_credentials.json")


def create_suggestion_template(n: int = 5) -> PromailTemplate:
    """Will Create Promailtemplate object including n recipes."""
    title = "Meal Suggestions"
    # same rules as CSS
    header_background = "AliceBlue"
    odd_row_colour = "#eddbcd"
    even_row_colour = "#f4f4f4"
    rows = []
    # create n meal suggestions
    for i in range(n):
        meal = Api().random()
        rows.append(
            {
                "thumbnail": meal.thumbnail,
                "title": meal.name,
                "description": ", ".join(x for x, y in meal.ingredients),
            }
        )
    template_data = {
        "style": {
            "header_background": header_background,
            "odd_row_colour": odd_row_colour,
            "even_row_colour": even_row_colour,
        },
        "title": title,
        "rows": rows,
    }
    return ImageDescriptionTemplate(template_data)


@client.register(
    name="suggestions", subject="meal suggestions", sender=(AUTHORIZED_EMAILS,)
)
def meal_suggestions(email):
    template = create_suggestion_template(5)
    client.send_email(
        recipients=email.sender,
        subject="Re: Meal Suggestions",
        htmltext=template.html,
        plaintext=template.plaintext,
    )
