
from scrapy.spiders import Spider
import scrapy
from pricescrapy.items import marketPriceItem


class DmozSpider(Spider):
    name = "consumer"
    allowed_domains = ["consumer.org.hk"]
    start_urls = [
        # "https://www3.consumer.org.hk/pricewatch/supermarket/detail.php?itemcode"
        "https://www3.consumer.org.hk/pricewatch/supermarket/index.php?view=0&filter1=004&filter2=007&filter3=001"
    ]

    def parse(self, response):
        sel = scrapy.Selector(response)
        print 'begin to crawl data'
        href = sel.xpath('//div[@id="theMainContent"]/table[@border=1]/tr/td/a/@href').extract()
        hrefLen = len(href)
        items = []
        for iter_i in range(0, hrefLen):
            item = marketPriceItem()
            item['link'] = 'https://www3.consumer.org.hk/pricewatch/supermarket/' + href[iter_i]
            items.append(item)

        for _item in items:
            yield scrapy.http.Request(url=_item['link'], callback=self.parse_secondary_link)


    def parse_secondary_link(self, response):
        sel = scrapy.Selector(response)
        print 'detal info of every item'
        items = []
        for site in sel.xpath('//td[@valign="top"]/table'):
            item = marketPriceItem()
            index = 0
            market_name = ''
            priceHistory = []
            for detail in site.xpath('tr'):
                psDetail = detail.xpath('td[@width=95]/remark/text()').extract()
                if index == 0:
                    market_name = detail.xpath('td[@class="tableheader"]/text()').extract()
                    index += 1
                else:
                    tmp = []
                    tmp.append(detail.xpath('td[@width=90]/text()').extract())
                    tmp.append(detail.xpath('td[@width=95]/text()').extract())
                    tmp.append(psDetail)
                    priceHistory.append(tmp)


            item['market_name'] = market_name
            item['price_history'] = priceHistory
            items.append(item)
        print items
        return items
