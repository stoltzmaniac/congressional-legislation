from scrapy.item import Item, Field


class CongressItem(Item):
    title = Field()
    code = Field()
