import scrapy
from scrapy import Request


class G2aSpider(scrapy.Spider):
    name = "CodeScraperG2A"
    allowed_domains = ["www.g2a.com"]
    start_urls = ["https://www.g2a.com/"]

    def search_game(self, game, response):
        # get the search query
        search_url = f'https://www.g2a.com/search?query={game}'
        yield response.follow(url=search_url, callback=self.find_price)

    def find_price(self, response):
        # get the search query
        price = response.css('span.sc-ksluID.kFmqyc::text').get()
        return price
