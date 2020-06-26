# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector

from hknews.items import HknewsItem


"""
curl 'https://news.rthk.hk/rthk/webpageCache/services/loadModNewsShowSp2List.php?lang=zh-TW&cat=3&newsCount=60&dayShiftMode=1&archive_date=' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0' -H 'Accept: */*' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' -H 'Referer: https://news.rthk.hk/rthk/ch/latest-news/local.htm' -H 'Cookie: _sp_id.6ac0=7991fbfa-6c21-4f08-9486-e3df60dd9951.1593150936.1.1593153342.1593150936.637c648b-2496-438f-822b-03a16a52cfd7; fontSize=100; WT_FPC=id=2de121879c85446c76f1593151188343:lv=1593155725847:ss=1593155725847' -H 'TE: Trailers'

"""

class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['rthk.hk']
    start_urls = ['https://news.rthk.hk/rthk/webpageCache/services/loadModNewsShowSp2List.php?lang=zh-TW&cat=2&newsCount=60&dayShiftMode=1&archive_date=',
                  'https://news.rthk.hk/rthk/webpageCache/services/loadModNewsShowSp2List.php?lang=zh-TW&cat=3&newsCount=60&dayShiftMode=1&archive_date=',
                  'https://news.rthk.hk/rthk/webpageCache/services/loadModNewsShowSp2List.php?lang=zh-TW&cat=4&newsCount=60&dayShiftMode=1&archive_date=',
                  'https://news.rthk.hk/rthk/webpageCache/services/loadModNewsShowSp2List.php?lang=zh-TW&cat=5&newsCount=60&dayShiftMode=1&archive_date=']

    def parse(self, response):

        sl = Selector(response=response)
        rows = sl.xpath('//h4[@class="ns2-title"]')
        for row in rows:
            item = HknewsItem()
            item['title'] = row.css('a::text').extract_first()
            item['url'] = row.css('a::attr(href)').extract_first()
            yield item
