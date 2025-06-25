from __future__ import annotations

from scrapy.utils.reactor import install_reactor

# Install Twisted's asyncio reactor before importing any other Twisted or
# Scrapy components.
install_reactor("twisted.internet.asyncioreactor.AsyncioSelectorReactor")

import os

from apify.scrapy import initialize_logging, run_scrapy_actor

# Import your main Actor coroutine here.
from .main import main

# Ensure the location to the Scrapy settings module is defined.
os.environ["SCRAPY_SETTINGS_MODULE"] = "books_scraper.settings"


if __name__ == "__main__":
    initialize_logging()
    run_scrapy_actor(main())
