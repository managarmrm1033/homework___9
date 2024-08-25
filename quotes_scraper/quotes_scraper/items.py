import scrapy

class QuoteItem(scrapy.Item):
    text = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()
    author_name = scrapy.Field()
    author_birthdate = scrapy.Field()
    author_bio = scrapy.Field()

class AuthorItem(scrapy.Item):
    name = scrapy.Field()
    birthdate = scrapy.Field()
    bio = scrapy.Field()
