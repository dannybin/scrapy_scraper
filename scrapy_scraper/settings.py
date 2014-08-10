# -*- coding: utf-8 -*-

# Scrapy settings for scrapy_scraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'scrapy_scraper'

SPIDER_MODULES = ['scrapy_scraper.spiders']
NEWSPIDER_MODULE = 'scrapy_scraper.spiders'
ITEM_PIPELINES = {
  'scrapy_scraper.pipelines.ScrapyScraperPipeline': 500,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapy_scraper (+http://www.yourdomain.com)'
