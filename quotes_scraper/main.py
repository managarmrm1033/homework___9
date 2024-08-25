import scrapy
from scrapy.crawler import CrawlerProcess
import logging

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        logging.info("Parsing page: %s", response.url)
        for quote in response.xpath("//div[@class='quote']"):
            author_url = quote.xpath("span/small/a/@href").get()
            yield {
                "quote": quote.xpath("span[@class='text']/text()").get(),
                "author": quote.xpath("span/small/text()").get(),
                "keywords": quote.xpath("div[@class='tags']/a/text()").extract(),
                "author_url": response.urljoin(author_url)
            }

        next_link = response.xpath("//li[@class='next']/a/@href").get()
        if next_link:
            logging.info("Following next page: %s", response.urljoin(next_link))
            yield scrapy.Request(url=response.urljoin(next_link), callback=self.parse)

    def parse_author(self, response):
        author_name = response.xpath("//h3[@class='author-title']/text()").get()
        birthdate = response.xpath("//span[@class='author-born-date']/text()").get()
        bio = response.xpath("//div[@class='author-description']/text()").get()
        yield {
            "author": author_name,
            "birthdate": birthdate,
            "bio": bio
        }

# Configure logging
logging.basicConfig(level=logging.INFO)

# run spider
if __name__ == "__main__":
    process = CrawlerProcess(settings={
        'FEEDS': {
            'quotes.json': {
                'format': 'json',
                'overwrite': True
            },
            'authors.json': {
                'format': 'json',
                'overwrite': True
            }
        }
    })
    process.crawl(QuotesSpider)
    process.start()
