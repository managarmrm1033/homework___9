# Scrapy settings for quotes_scraper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "quotes_scraper"

SPIDER_MODULES = ["quotes_scraper.spiders"]
NEWSPIDER_MODULE = "quotes_scraper.spiders"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = "quotes_scraper (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 1  # Зменшення кількості одночасних запитів

# Configure a delay for requests for the same website (default: 0)
DOWNLOAD_DELAY = 2  # Затримка 2 секунди між запитами

# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#     "Accept-Language": "en",
# }

# Enable or disable spider middlewares
# SPIDER_MIDDLEWARES = {
#     "quotes_scraper.middlewares.QuotesScraperSpiderMiddleware": 543,
# }

# Enable or disable downloader middlewares
# DOWNLOADER_MIDDLEWARES = {
#     "quotes_scraper.middlewares.QuotesScraperDownloaderMiddleware": 543,
# }

# Enable or disable extensions
# EXTENSIONS = {
#     "scrapy.extensions.telnet.TelnetConsole": None,
# }

# Configure item pipelines
ITEM_PIPELINES = {
    'quotes_scraper.pipelines.QuotesScraperPipeline': 1,
}

# Enable and configure the AutoThrottle extension (disabled by default)
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1  # Початкова затримка
AUTOTHROTTLE_MAX_DELAY = 10   # Максимальна затримка
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0  # Цільове число одночасних запитів
AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

# Configure the JSON output for quotes and authors
FEEDS = {
    'quotes.json': {
        'format': 'json',
        'overwrite': True,
    },
    'authors.json': {
        'format': 'json',
        'overwrite': True,
    }
}
