import scrapy


class BookItem(scrapy.Item):
    title = scrapy.Field()
    rating = scrapy.Field()
    price = scrapy.Field()
    in_stock = scrapy.Field()
