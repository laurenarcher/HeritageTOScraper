# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from scrapy.exceptions import DropItem
from scrapy.contrib.exporter import XmlItemExporter
from scrapy.contrib.exporter import CsvItemExporter
import csv


class DuplicatesPipeline(object):

    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        if item['url'] in self.ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ids_seen.add(item['url'])
            return item

class HeritagetoPipeline(object):
    def __init__(self):
        self.fields_to_export = [
            'url',
            'City',
            'Address',
            'Ward',
            'Status',
            'ListDate',
            'IntentionDate',
            'ByLaw',
            'PartIVDate',
            'PartVDate',
            'HeritageDistrict',
            'DistrictStatus',
            'HeritageEasement',
            'RegistrationDate',
            'BuildingType',
            'ArchitectBuilder',
            'ConstructionYear',
            'Details',
            'DemoDate',
            'PrimaryAddress',
            
        ]
        dispatcher.connect(self.spider_opened, signals.spider_opened)
        dispatcher.connect(self.spider_closed, signals.spider_closed)
        
    def spider_opened(self, spider):
        self.csv_exporter = CsvItemExporter(open(spider.name+".csv", "w"),
                                            fields_to_export=self.fields_to_export, quoting=csv.QUOTE_ALL)
       
        self.xml_exporter = XmlItemExporter(open(spider.name+".xml", "w"),
                                                    fields_to_export=self.fields_to_export,
                                                    root_element="structures", item_element="structure")
        self.csv_exporter.start_exporting()
        self.xml_exporter.start_exporting()
        
    def process_item(self, item, spider):
        self.csv_exporter.export_item(item)
        self.xml_exporter.export_item(item)
        return item
    
    def spider_closed(self, spider):
        self.csv_exporter.finish_exporting()
        self.xml_exporter.finish_exporting()
