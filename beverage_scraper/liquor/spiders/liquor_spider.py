from scrapy import Spider
from scrapy.selector import Selector

from liquor.items import LiquorItem

class LiquorSpider(Spider):
    name = "liquor"
    allowed_domains = ["liquorconnect.com"]
    start_urls = [
        "http://www.liquorconnect.com/Products/Pages/SearchResults.aspx?k=lcproductcategory%3A%22Beer%22",
    ]

    def parse(self, response):
        products = Selector(response).xpath('//div[@class="result-item"]/h3')

        for product in products:
            item = LiquorItem()
            item['title'] = product.xpath(
                'a[@id="ctl00_PlaceHolderMain_g_f343e31d_104f_4b04_a34e_2bd83943fbeb_ctl00_ResultsListView_CustomLayout_ctrl5_ctl00_ProductLink"]/text()').extract()[0]
            yield item
