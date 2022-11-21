import json
from base64 import b64decode
from scrapy import Request, Spider
import custom_settings_config

class BrowserActionCustomSpider(Spider):
    name = "browser_action_custom"

    custom_settings = custom_settings_config.custom_settings

    def start_requests(self):
        yield Request(
            "http://quotes.toscrape.com/",
            meta={
                "zyte_api_automap": {
                    "browserHtml": True,
                    "screenshot": True,
                    "screenshotOptions": {"fullPage": True},
                    "actions": [
                        {
                            "action": "click",
                            "selector": {
                                "type": "css",
                                "value": ".header-box .col-md-4 a",
                            },
                        },
                        {
                            "action": "waitForResponse",
                            "urlPattern": "/login",
                        },
                        {
                            "action": "type",
                            "text": "username",
                            "selector": {
                                "type": "css",
                                "value": "#username",
                            },
                        },
                        {
                            "action": "type",
                            "text": "password",
                            "selector": {
                                "type": "css",
                                "value": "#password",
                            },
                        },
                        {
                            "action": "click",
                            "selector": {
                                "type": "css",
                                "value": "*[type=\"submit\"]",
                            },
                        },
                        {
                            "action": "waitForResponse",
                            "urlPattern": "/",
                        },
                    ],
                },
            },
        )

    def parse(self, response):
        with open("output_login.jpg", "wb") as output:
            output.write(b64decode(response.raw_api_response["screenshot"]))
        
        user_status: str = response.css('.header-box .col-md-4 a::text').get()

        if user_status == "Logout":
            print("Staus: User is currently Logged-in.")
        else:
            print("Status: User is currently Logged-out.")

