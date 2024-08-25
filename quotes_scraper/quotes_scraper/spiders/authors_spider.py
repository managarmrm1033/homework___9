import scrapy

class AuthorsSpider(scrapy.Spider):
    name = "authors"
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response):
        authors_urls = response.css('div.quote small.author::attr(href)').getall()
        for url in authors_urls:
            yield response.follow(url, self.parse_author)

    def parse_author(self, response):
        yield {
            'fullname': response.css('h3.author-title::text').get(),
            'born_date': response.css('span.author-born-date::text').get(),
            'born_location': response.css('span.author-born-location::text').get(),
            'description': response.css('div.author-description::text').get().strip(),
        }
