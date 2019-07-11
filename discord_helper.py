import json
import urllib
import requests

import settings


def post_listing_to_discord(content):
    if content == "test":
        print("Success")
        return
    payload = {
        "username": "Apartment Tracker",
        "embeds": [
            {
                "title": "Apartment in " + content["where"],
                "url": content["url"],
                "description": content["name"],
                "fields": [
                    {
                        "name": "Price",
                        "value":  content["price"]
                    }
                ],
            }
        ]
    }
    response = requests.post(
        settings.DISCORD_WEBHOOK_ADDRESS,
        data=json.dumps(payload), headers={"Content-Type": "application/json"})
