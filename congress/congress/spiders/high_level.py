from scrapy import Spider
from scrapy.selector import Selector
from congress.items import CongressItem

class HighLevelSpider(Spider):
    name = "high_level"
    allowed_domains = ["congress.gov"]
    start_urls = [
        "https://www.congress.gov/search?q={%22source%22:%22legislation%22}&page=1",
    ]

    def parse(self, response):
        legislations = Selector(response).xpath('// *[ @ id = "download-csv-650"]')
        # legislations = Selector(response).xpath('//*[@id="main"]/ol/li')
        #
        # for legislation in legislations:
        #     item = CongressItem()
        #     item['code'] = legislation.xpath('/span[1]/text()').extract()[0]
        #     item['title'] = legislation.xpath('/span[2]/text()').extract()[0]
        #     yield item
        yield legislations
