# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class HeritageTOItem(Item):
    url = Field()
    City = Field()
    Address = Field()
    Ward = Field()
    Status = Field()
    ListDate = Field()
    IntentionDate = Field()
    ByLaw = Field()
    PartIVDate = Field()
    PartVDate = Field()
    HeritageDistrict = Field()
    DistrictStatus = Field()
    HeritageEasement = Field()
    RegistrationDate = Field()
    BuildingType = Field()
    ArchitectBuilder = Field()
    ConstructionYear = Field()
    Details = Field()
    DemoDate = Field()
    PrimaryAddress = Field()
