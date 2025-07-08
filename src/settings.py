BOT_NAME = "books_scraper"
LOG_LEVEL = "INFO"

# Set depth limit to 50 since there are 50 pages of books on the books.toscrape.com
DEPTH_LIMIT = 50

SPIDER_MODULES = ["src.spiders"]
NEWSPIDER_MODULE = "src.spiders"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

ITEM_PIPELINES = {
    "src.pipelines.CleaningPipeline": 100,
}
