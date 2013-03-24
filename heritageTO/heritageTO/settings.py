# Scrapy settings for heritageTO project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'heritageTO'

SPIDER_MODULES = ['heritageTO.spiders']
NEWSPIDER_MODULE = 'heritageTO.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Friendly Neighbourood @laurenarcher'

# Pipeline
ITEM_PIPELINES = ['heritageTO.pipelines.DuplicatesPipeline',
                  'heritageTO.pipelines.HeritagetoPipeline',]

# Log file.

LOG_FILE = 'heritageTO.log'
