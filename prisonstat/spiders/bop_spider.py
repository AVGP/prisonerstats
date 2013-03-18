from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from prisonstat.items import InmateItem

class BOPSpider(BaseSpider):
    name = "BOP"

    def __init__(self):
    	self.start_urls = []
       	base_url = "http://www.bop.gov/iloc2/InmateFinderServlet?Transaction=IDSearch&needingMoreList=false&IDType=IRN&IDNumber=10378-01"
	for i in list(xrange(10)):
	    self.start_urls.append(base_url + str(i))
    	

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        age, race, sex = hxs.select("//td[@class='data-cell']/text()")[2].extract().strip().split("-")
	location = hxs.select("//td[@class='data-cell']/text()")[4].extract().strip()
	
        item = InmateItem()
	item["age"] = age
	item["race"] = race
	item["sex"] = sex
	item["location"] = location
	return item
