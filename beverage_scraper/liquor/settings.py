# -*- coding: utf-8 -*-

# Scrapy settings for liquor project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'liquor'

SPIDER_MODULES = ['liquor.spiders']
NEWSPIDER_MODULE = 'liquor.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'liquor (+http://www.yourdomain.com)'

ITEM_PIPELINES = ['liquor.pipelines.MongoDBPipeline', ]

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "liquorconnect"
MONGODB_COLLECTION = "products"
