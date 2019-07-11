import requests

import settings


def post_listing_to_discord(content):
    if content == "test":
        print("Success")
        return
    payload = {
        "username": "Apartment Tracker",
        "content": content
    }
    response = requests.post(
        settings.DISCORD_WEBHOOK_ADDRESS,
        data=payload)
