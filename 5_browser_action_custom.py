from base64 import b64decode
from scrapy import Request, Spider
import custom_settings_config, json


class BrowserActionCustomSpider(Spider):
    name = "browser_action_custom"

    custom_settings = custom_settings_config.custom_settings

    def start_requests(self):
        pass # your code here

    def parse(self, response):
        pass # your code here

        if user_status == "Logout":
            print("Staus: User is currently Logged-in.")
        else:
            print("Status: User is currently Logged-out.")

