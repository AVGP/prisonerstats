# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class BOPItem(Item):
    # define the fields for your item here like:
    # name = Field()
    age = Field()
    sex = Field()
    race = Field()
    location = Field()
