import scrapy
from scrapy.selector import HtmlXPathSelector
from datetime import datetime
from scrapy_scraper.items import ScrapyScraperItem

ROOT = "https://beta.congress.gov/legislation?q={%22bill-status%22%3A%22law%22}&pageSize=500"

class LawSpider(scrapy.Spider):
  name = "law_scraper"
  allowed_domains = ["beta.congress.gov"]
  start_urls = [
    "https://beta.congress.gov/legislation?q={%22bill-status%22%3A%22law%22}&pageSize=500&page=1",
    "https://beta.congress.gov/legislation?q={%22bill-status%22%3A%22law%22}&pageSize=500&page=2",
    "https://beta.congress.gov/legislation?q={%22bill-status%22%3A%22law%22}&pageSize=500&page=3",
    "https://beta.congress.gov/legislation?q={%22bill-status%22%3A%22law%22}&pageSize=500&page=4",
    "https://beta.congress.gov/legislation?q={%22bill-status%22%3A%22law%22}&pageSize=500&page=5",
    "https://beta.congress.gov/legislation?q={%22bill-status%22%3A%22law%22}&pageSize=500&page=6",
    "https://beta.congress.gov/legislation?q={%22bill-status%22%3A%22law%22}&pageSize=500&page=7",
    "https://beta.congress.gov/legislation?q={%22bill-status%22%3A%22law%22}&pageSize=500&page=8",
    "https://beta.congress.gov/legislation?q={%22bill-status%22%3A%22law%22}&pageSize=500&page=9",
    "https://beta.congress.gov/legislation?q={%22bill-status%22%3A%22law%22}&pageSize=500&page=10",
    "https://beta.congress.gov/legislation?q={%22bill-status%22%3A%22law%22}&pageSize=500&page=11",
    "https://beta.congress.gov/legislation?q={%22bill-status%22%3A%22law%22}&pageSize=500&page=12",
    "https://beta.congress.gov/legislation?q={%22bill-status%22%3A%22law%22}&pageSize=500&page=13",
    "https://beta.congress.gov/legislation?q={%22bill-status%22%3A%22law%22}&pageSize=500&page=14",
    "https://beta.congress.gov/legislation?q={%22bill-status%22%3A%22law%22}&pageSize=500&page=15",
    "https://beta.congress.gov/legislation?q={%22bill-status%22%3A%22law%22}&pageSize=500&page=16",
    "https://beta.congress.gov/legislation?q={%22bill-status%22%3A%22law%22}&pageSize=500&page=17",
    "https://beta.congress.gov/legislation?q={%22bill-status%22%3A%22law%22}&pageSize=500&page=18",
    "https://beta.congress.gov/legislation?q={%22bill-status%22%3A%22law%22}&pageSize=500&page=19",
    "https://beta.congress.gov/legislation?q={%22bill-status%22%3A%22law%22}&pageSize=500&page=20",
    "https://beta.congress.gov/legislation?q={%22bill-status%22%3A%22law%22}&pageSize=500&page=21",
    "https://beta.congress.gov/legislation?q={%22bill-status%22%3A%22law%22}&pageSize=500&page=22",
    "https://beta.congress.gov/legislation?q={%22bill-status%22%3A%22law%22}&pageSize=500&page=23"
  ]

  def parse(self, response):
  
    for law in response.xpath('//ul/li/h3/text()'):
      item = ScrapyScraperItem()
      item['law'] = law.extract()
      yield item
