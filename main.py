from scrapy import cmdline

cmdline.execute("scrapy crawl news".split())

# request for items on scrapinghub
#items/:project_id[/:spider_id][/:job_id][/:item_no][/:field_name]¶
#curl -u accesskey: https://storage.scrapinghub.com/items/459589/1/2