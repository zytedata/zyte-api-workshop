from scrapy import Request, Spider
import custom_settings_config, json

class GeolocationSpider(Spider):
    name = 'geolocation'
    
    custom_settings = custom_settings_config.custom_settings

    def start_requests(self):
        yield Request(
            "http://ip-api.com/json",
            meta = {
                "zyte_api": {
                    "geolocation": "AU"
                }
            }
        )    
    
    def parse(self, response):
        response_data = json.loads(response.body) # fetch JSON response body
        country: str = response_data["country"]
        print("You are accessing this website from: ", country)
