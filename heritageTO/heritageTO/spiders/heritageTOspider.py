# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

from scrapy.contrib.spiders import CrawlSpider, Rule
from heritageTO.items import HeritageTOItem
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http.request.form import FormRequest
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from scrapy import log
import sys

class HeritageTOSpider(CrawlSpider):
    name = "heritageTO"
    allowed_domains = ["toronto.ca"]
    start_urls = [
        "http://app.toronto.ca/HeritagePreservation/setup.do?action=init"
    ]
    rules = [
        Rule(SgmlLinkExtractor(allow=r'/search\.do.+'),),
        Rule(SgmlLinkExtractor(allow=r'/navigate\.do.+'), process_request='process_request'),
        Rule(SgmlLinkExtractor(allow=r'/details\.do.+'), follow=True, callback='parse_heritage'),
    ]
    download_delay = 1

    def process_request(self, request):
        if 'method=prev' in request.url or 'method=next' in request.url:
            return request.replace(dont_filter=True)
        else:
            request
            
    def make_requests_from_url(self, url):
        return Request(url, dont_filter=True, callback=self.parse_start_url)

    def parse_start_url(self, response):
        if 'init' in response.url:
            yield FormRequest.from_response(response, formnumber=1)

    def parse_heritage(self, response):
        self.log("crawling.")
    
        hxs = HtmlXPathSelector(response)
        item = HeritageTOItem()
        
        item['url'] = response.url
        item['City'] = "Toronto"
        item['Address'] = str(hxs.select('//*[@id="listTbl"]/table/tbody/tr[4]/td[2]/b/text()').extract()[0]).strip()
        item['Ward'] = str(hxs.select('//*[@id="listTbl"]/table/tbody/tr[6]/td[2]/text()').extract()[0]).strip()
        item['Status'] = str(hxs.select('//*[@id="listTbl"]/table/tbody/tr[7]/td[2]/text()').extract()[0]).strip()
        item['ListDate'] = str(hxs.select('//*[@id="listTbl"]/table/tbody/tr[8]/td[2]/text()').extract()[0]).strip()
        item['IntentionDate'] = str(hxs.select('//*[@id="listTbl"]/table/tbody/tr[9]/td[2]/text()').extract()[0]).strip()
        item['ByLaw'] = str(hxs.select('//*[@id="listTbl"]/table/tbody/tr[10]/td[2]/text()').extract()[0]).strip()
        item['PartIVDate'] = str(hxs.select('//*[@id="listTbl"]/table/tbody/tr[11]/td[2]/text()').extract()[0]).strip()
        item['PartVDate'] = str(hxs.select('//*[@id="listTbl"]/table/tbody/tr[12]/td[2]/text()').extract()[0]).strip()
        item['HeritageDistrict'] = str(hxs.select('//*[@id="listTbl"]/table/tbody/tr[13]/td[2]/text()').extract()[0]).strip()
        item['DistrictStatus'] = str(hxs.select('//*[@id="listTbl"]/table/tbody/tr[14]/td[2]/text()').extract()[0]).strip()
        item['HeritageEasement'] = str(hxs.select('//*[@id="listTbl"]/table/tbody/tr[15]/td[2]/text()').extract()[0]).strip()
        item['RegistrationDate'] = str(hxs.select('//*[@id="listTbl"]/table/tbody/tr[16]/td[2]/text()').extract()[0]).strip()
        item['BuildingType'] = str(hxs.select('//*[@id="listTbl"]/table/tbody/tr[17]/td[2]/text()').extract()[0]).strip()
        item['ArchitectBuilder'] = str(hxs.select('//*[@id="listTbl"]/table/tbody/tr[18]/td[2]/text()').extract()[0]).strip()
        item['ConstructionYear'] = str(hxs.select('//*[@id="listTbl"]/table/tbody/tr[19]/td[2]/text()').extract()[0]).strip()
        item['Details'] = str(hxs.select('//*[@id="listTbl"]/table/tbody/tr[20]/td[2]/text()').extract()[0]).strip()
        item['DemoDate'] = str(hxs.select('//*[@id="listTbl"]/table/tbody/tr[21]/td[2]/text()').extract()[0]).strip()
        item['PrimaryAddress'] = str(hxs.select('//*[@id="listTbl"]/table/tbody/tr[22]/td[2]/text()').extract()[0]).strip()
        return item
